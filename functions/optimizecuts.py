import functions.preprocess_data as ppd
import numpy as np

def main(cutting_list, storage):

    [filtered_cutting_list, filtered_storage] = ppd.main(cutting_list, storage)
    # Sort the cutting list in decreasing order of size
    filtered_cutting_list.sort(key=lambda x: x[0], reverse=True)
    # Initialize the result table and storage usage count
    result_table = []
    storage_usage_count = {}
    storage_cut_lengths = {}
    cumulative_loss = 0
    remaining_lengths = {}
    
    # Initialize filtered_storage with the storage list
    filtered_storage = [[length, number, length] for length, number in filtered_storage]  # Add original length to each storage piece

    # Solve the cutting stock problem using First Fit Decreasing (FFD) algorithm
    for piece in filtered_cutting_list:
        size, number = piece
        for _ in range(number):
            fitted = False
            best_fit_index = -1
            best_fit_diff = float('inf')
            exact_match_found = False

            # First, check for exact matches
            for storage_index, storage_piece in enumerate(filtered_storage):
                storage_length, storage_number, original_length = storage_piece
                if storage_length == size and storage_number > 0:
                    storage_piece[0] -= size
                    storage_piece[1] -= 1
                    if storage_index not in storage_usage_count:
                        storage_usage_count[storage_index] = 0
                    storage_usage_count[storage_index] += 1
                    if storage_index not in storage_cut_lengths:
                        storage_cut_lengths[storage_index] = 0
                    storage_cut_lengths[storage_index] += size
                    result_table.append([original_length, storage_usage_count[storage_index], size, storage_piece[0], 0])
                    fitted = True
                    exact_match_found = True
                    break

            # If no exact match is found, check for the closest match within the threshold
            if not exact_match_found:
                for storage_index, storage_piece in enumerate(filtered_storage):
                    storage_length, storage_number, original_length = storage_piece
                    if storage_length >= size and storage_number > 0:
                        diff = storage_length - size
                        if diff < 20 and diff < best_fit_diff:
                            best_fit_diff = diff
                            best_fit_index = storage_index

                if best_fit_index != -1:
                    storage_piece = filtered_storage[best_fit_index]
                    storage_piece[0] -= size
                    storage_piece[1] -= 1
                    if best_fit_index not in storage_usage_count:
                        storage_usage_count[best_fit_index] = 0
                    storage_usage_count[best_fit_index] += 1
                    if best_fit_index not in storage_cut_lengths:
                        storage_cut_lengths[best_fit_index] = 0
                    storage_cut_lengths[best_fit_index] += size
                    individual_loss = best_fit_diff
                    result_table.append([storage_piece[2], storage_usage_count[best_fit_index], size, storage_piece[0], individual_loss])
                    remaining_lengths[best_fit_index] = storage_piece[0]
                    fitted = True
                else:
                    for storage_index, storage_piece in enumerate(filtered_storage):
                        storage_length, storage_number, original_length = storage_piece
                        if storage_length >= size and storage_number > 0:
                            storage_piece[0] -= size
                            storage_piece[1] -= 1
                            if storage_index not in storage_usage_count:
                                storage_usage_count[storage_index] = 0
                            storage_usage_count[storage_index] += 1
                            if storage_index not in storage_cut_lengths:
                                storage_cut_lengths[storage_index] = 0
                            storage_cut_lengths[storage_index] += size
                            individual_loss = storage_length - size
                            result_table.append([original_length, storage_usage_count[storage_index], size, storage_piece[0], individual_loss])
                            remaining_lengths[storage_index] = storage_piece[0]
                            fitted = True
                            break
                if not fitted:
                    filtered_storage.append([size, 1, size])
                    storage_index = len(filtered_storage) - 1
                    storage_usage_count[storage_index] = 1
                    storage_cut_lengths[storage_index] = size
                    result_table.append([size, 1, size, 0, 0])
                    remaining_lengths[storage_index] = 0

    # Calculate the cumulative loss based on the final remaining lengths
    cumulative_loss = sum(remaining_lengths.values())

    # Remove empty storage pieces
    filtered_storage = [row for row in filtered_storage if row[0] > 0]

    # Add a final row with the total cumulative loss
    result_table.append(["Total", "", "", "", cumulative_loss])

    return result_table


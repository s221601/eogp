import functions.preprocess_data as ppd
import numpy as np

def main(cutting_list, storage):

    [filtered_cutting_list, filtered_storage] = ppd.main(cutting_list, storage)
    # Sort the cutting list in decreasing order of size
    filtered_cutting_list.sort(key=lambda x: x[0], reverse=True)
    # Initialize the result table and storage usage count
    result_table = []
    storage_usage_count = {}
    
    # Initialize filtered_storage with the storage list
    filtered_storage = [[length, number, length] for length, number in filtered_storage]  # Add original length to each storage piece

    # Solve the cutting stock problem using First Fit Decreasing (FFD) algorithm
    for piece in filtered_cutting_list:
        size, number = piece
        for _ in range(number):
            fitted = False
            for storage_index, storage_piece in enumerate(filtered_storage):
                storage_length, storage_number, original_length = storage_piece
                if storage_length >= size:
                    storage_piece[0] -= size
                    if storage_index not in storage_usage_count:
                        storage_usage_count[storage_index] = 0
                    storage_usage_count[storage_index] += 1
                    result_table.append([original_length, storage_usage_count[storage_index], size, storage_piece[0]])
                    fitted = True
                    break
            if not fitted:
                filtered_storage.append([size, 1, size])
                storage_index = len(filtered_storage) - 1
                storage_usage_count[storage_index] = 1
                result_table.append([size, 1, size, 0])

    # Remove empty storage pieces
    filtered_storage = [row for row in filtered_storage if row[0] > 0]

    # Sort the result table based on the original storage length and usage count
    result_table.sort(key=lambda x: (x[0], x[1]))

    return result_table

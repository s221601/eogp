def main(cutting_list, storage):
    # Find the indices of the columns that contain "Length" or "Amount" in cutting_list
    cutting_length_indices = []
    cutting_amount_indices = []

    for i, row in enumerate(cutting_list):
        for j, value in enumerate(row):
            if value == "Length":
                cutting_length_indices.append(j)
            elif value == "Amount":
                cutting_amount_indices.append(j)

    # Combine the indices and remove duplicates for cutting_list
    cutting_relevant_indices = list(set(cutting_length_indices + cutting_amount_indices))

    # Filter the cutting_list to only include the relevant columns
    filtered_cutting_list = [[row[i] for i in cutting_relevant_indices] for row in cutting_list]

    # Find the indices of the columns that contain "Length" or "Amount" in storage
    storage_length_indices = []
    storage_amount_indices = []

    for i, row in enumerate(storage):
        for j, value in enumerate(row):
            if value == "Length":
                storage_length_indices.append(j)
            elif value == "Amount":
                storage_amount_indices.append(j)

    # Combine the indices and remove duplicates for storage
    storage_relevant_indices = list(set(storage_length_indices + storage_amount_indices))

    # Filter the storage to only include the relevant columns
    filtered_storage = [[row[i] for i in storage_relevant_indices] for row in storage]
    print(filtered_cutting_list)


    return filtered_cutting_list, filtered_storage
def main(cutting_list, storage):
    import re

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
    
    # Function to remove non-numeric characters and convert to number
    def clean_and_convert(value):
        cleaned_value = re.sub(r'\D', '', value)
        if cleaned_value:
            return int(cleaned_value) if cleaned_value.isdigit() else float(cleaned_value)
        return 0  # Default value if cleaned_value is empty

    # Remove text, convert to numbers, and filter out zeros in filtered_cutting_list
    filtered_cutting_list = [[clean_and_convert(value) for value in row] for row in filtered_cutting_list]
    filtered_cutting_list = [row for row in filtered_cutting_list if any(value != 0 for value in row)]

    # Remove text, convert to numbers, and filter out zeros in filtered_storage
    filtered_storage = [[clean_and_convert(value) for value in row] for row in filtered_storage]
    filtered_storage = [row for row in filtered_storage if any(value != 0 for value in row)]
    

    return filtered_cutting_list, filtered_storage


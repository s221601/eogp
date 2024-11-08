import functions.preprocess_data as ppd

def main(cutting_list, storage):
    [filtered_cutting_list, filtered_storage] = ppd.main(cutting_list, storage)


    print(filtered_cutting_list)
    return filtered_cutting_list, filtered_storage
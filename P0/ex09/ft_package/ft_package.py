def count_in_list(list_to_count, string) -> int:
    count = 0
    for i in range(len(list_to_count)):
        if (list_to_count[i] == string):
            count += 1
    return count

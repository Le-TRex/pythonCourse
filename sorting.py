

def smallest_number_and_index(list_to_evaluate):
    if not list_to_evaluate:
        return None
    smallest_number = list_to_evaluate[0]
    index_of_smallest_number = 0
    for i in range(len(list_to_evaluate)):
        if list_to_evaluate[i] < smallest_number:
            smallest_number = list_to_evaluate[i]
            index_of_smallest_number = i
    return index_of_smallest_number, smallest_number


def swap(listToEvaluate, i, j):
    auxilary = listToEvaluate[i]
    listToEvaluate[i] = listToEvaluate[j]
    listToEvaluate[j] = auxilary


def sort_selection(list_to_be_sorted):
    for i in range(len(list_to_be_sorted)):
        index, value = smallest_number_and_index(list_to_be_sorted[i:])
        swap(list_to_be_sorted, index + i, i)
        # print(list_to_be_sorted)


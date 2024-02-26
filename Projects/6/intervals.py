# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:EPY82

# Input: tuples_list is an unsorted list of interval tuples
# Output: A sorted and merged list of interval tuples, where
#         no interval in the merged list has any overlap.
def merge_tuples (tuples_list):

    #Insertion sort by lower bound
    for i in range(len(tuples_list)):
        j = i
        while j > 0 and tuples_list[j][0] < tuples_list[j-1][0]:
            tuples_list[j], tuples_list[j-1] = tuples_list[j-1], tuples_list[j]
            j -= 1

    #merge
    i = 0
    while i < len(tuples_list)-1:
        #checks if mergable
        if tuples_list[i][1] >= tuples_list[i+1][0]:
            tuples_list[i] = list(tuples_list[i])

            #merges by complete overlap or partial overlap
            if tuples_list[i][1] < tuples_list[i+1][1]:
                tuples_list[i][1] = tuples_list[i+1][1]
            
            tuples_list[i] = tuple(tuples_list[i])
            tuples_list.pop(i+1)
        i += 1
    return tuples_list #THE BUG It's the right list but the main method doesn't print it out right#


# Input: tuples_list is a list of tuples of denoting intervals
# Output: A list of tuples sorted by ascending order of the size
#         of the interval. If two intervals have the size then it breaks
#         ties putting the interval with the lower starting number first
def sort_by_interval_size (tuples_list):
    for i in range(len(tuples_list)):
        j = i
        while j > 0 and length(tuples_list[j]) < length(tuples_list[j-1]):
            tuples_list[j], tuples_list[j-1] = tuples_list[j-1], tuples_list[j]
            j -= 1
    return tuples_list

def length(tuple):
    return tuple[1]-tuple[0]


def main():
    """
    Uses input redirection to read the data and create a list of tuples
    """
    num_cases = int(input())

    tuples_list = []
    for i in range(num_cases):
        line = input()
        start, end = line.split()
        tuples_list.insert(i, (int(start), int(end)))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()

# Name 1:
# EID 1:

# Name 2:
# EID 2:

import time


#done
def sum_series(lines_before_coffee, prod_loss):
    total_lines = lines_to_add = lines_before_coffee
    i = 1
    while lines_to_add > 0:
        lines_to_add = lines_before_coffee//(prod_loss**i)
        total_lines += lines_to_add
        i += 1
    return total_lines


#done
def linear_search(total_lines, prod_loss):
    count = 0
    guessed_lines = 0
    while sum_series(guessed_lines, prod_loss) < total_lines:
        guessed_lines += 1
        count += 1
    return (guessed_lines, count)


def binary_search(total_lines, prod_loss):
    count = 1
    high = total_lines
    low = 0
    while low <= high:
        answer = (high + low + 1) // 2
        print(answer)
        if sum_series(answer, prod_loss) >= total_lines and sum_series(answer-1, prod_loss) < total_lines:
            return (answer, count)
        elif sum_series(answer, prod_loss) < total_lines:
            low = answer
            count += 1
        elif sum_series(answer, prod_loss) > total_lines:
            high = answer
            count += 1
    return (-1, count)


def main():
    print(sum_series(54, 9))
    # input_file = open("work.in", "r")
    # num_cases = int(input_file.readline())
    num_cases = 1

    # TODO: Iterate for the number of test cases
    for i in range(num_cases):

        # line = input_file.readline()
        line = "59 9"
        data = line.split(" ")
        total_lines = int(data[0])  # total number of lines of code
        prod_loss = int(data[1])  # read productivity loss factor

        print("=====> Case #", i + 1)

        # Binary Search
        start = time.time()
        print("Binary Search:")
        lines, count = binary_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        binary_time = finish - start
        print(f"Elapsed Time: {binary_time:0.8f} seconds")
        print()

        # Linear Search
        start = time.time()
        print("Linear Search:")
        lines, count = linear_search(total_lines, prod_loss)
        print("Ideal lines of code before coffee:", lines)
        print("sum_series called", count, "times")
        finish = time.time()
        linear_time = finish - start
        print(f"Elapsed Time: {linear_time:0.8f} seconds")
        print()

    #     # Comparison
    #     binary_time = 0.0
    #     comparison = linear_time / binary_time if binary_time else 1
    #     print(f"Binary Search was {comparison:0.1f}",
    #           "times faster.")
    #     print()
    #     print()


if __name__ == "__main__":
    main()

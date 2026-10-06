"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    arr = lst.copy()
    n = len(arr)

    for i in range(n):
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left, right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")
    dataset1 = [9, 3, 7, 1, 8, 2, 5]
    print("Original:", dataset1)
    print("Bubble Sort:", bubble_sort(dataset1))
    print("Merge Sort:", merge_sort(dataset1))

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")
    dataset2 = [42, 17, 23, 99, 8, 8, -5]
    print("Original:", dataset2)
    print("Bubble Sort:", bubble_sort(dataset2))
    print("Merge Sort:", merge_sort(dataset2))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    empty = []
    print("Empty list:", empty)
    print("Bubble Sort:", bubble_sort(empty))
    print("Merge Sort:", merge_sort(empty))

    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready sorted:", sorted_list)
    print("Bubble Sort:", bubble_sort(sorted_list))
    print("Merge Sort:", merge_sort(sorted_list))

    reverse_list = [5, 4, 3, 2, 1]
    print("\nReverse sorted:", reverse_list)
    print("Bubble Sort:", bubble_sort(reverse_list))
    print("Merge Sort:", merge_sort(reverse_list))

    single = [10]
    print("\nSingle element:", single)
    print("Bubble Sort:", bubble_sort(single))
    print("Merge Sort:", merge_sort(single))


if __name__ == "__main__":
    main()

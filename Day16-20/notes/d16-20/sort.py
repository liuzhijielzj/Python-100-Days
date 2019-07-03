def select_sort(origin_items, comp = lambda x, y: x < y):
    ''' simple selection sort '''
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_idx = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_idx]):
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items


def bubble_sort(origin_items, comp = lambda x, y: x < y):
    ''' bubble sort '''
    items = origin_items[:]
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items

def merge_sort(items, comp=lambda x, y: x <= y):
    ''' merge sort '''
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    l = merge_sort(items[:mid], comp)
    r = merge_sort(items[mid:], comp)
    return merge(l, r, comp)

def merge(left, right, comp):
    items = []
    idx1, idx2 = 0, 0
    while idx1 < len(left) and idx2 < len(right):
        if comp(left[idx1], right[idx2]):
            items.append(left[idx1])
            idx1 += 1
        else:
            items.append(right[idx2])
            idx2 += 1
    items += left[idx1:]
    items += right[idx2:]
    return items


def bin_search(items, key):
    """折半查找"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1

def main():
    items = [
        [1, 2, 3, 4, 5, 6, 7],
        [2, 5, 4, 3, 6, 7, 1],
        [7, 6, 5, 4, 3, 2, 1]
    ]
    print('simple selection sort:')
    for arr in items:
        print(select_sort(arr))
    print('bubble sort:')
    for arr in items:
        print(bubble_sort(arr))
    print('mrege sort:')
    for arr in items:
        print(merge_sort(arr))


if __name__ == '__main__':
    main()
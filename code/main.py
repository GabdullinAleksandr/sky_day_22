def quick_sort(items):
    if len(items) <= 1:
        return items
    elem = items[0]
    left = list(filter(lambda x: x < elem, items))
    mid = [i for i in items if i == elem]
    right = list(filter(lambda x: x > elem, items))
    return quick_sort(left) + mid + quick_sort(right)




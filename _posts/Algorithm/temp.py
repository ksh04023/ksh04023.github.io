array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    #pivot보다 작은 값은 left_side로, 큰 값은 right_side로 나눔
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    #left_side와 right_side를 각각 재귀적으로 quick sorting을 해줌
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


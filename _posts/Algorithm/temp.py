array = [7,5,9,0,3,1,6,2,4,8]

#start와 end는 각 시작과 끝의 index임
def quick_sort(array, start, end):
    #해당 리스트에 원소가 1개이면 종료
    if start >= end:
        return

    #첫번째 원소가 pivot
    pivot = start
    left = start + 1
    right = end

    #pivot보다 큰 수와 작은 수가 뒤바뀔 때까지 반복문 수행
    while left <= right:
        #pivot보다 큰 데이터 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        #pivot보다 작은 데이터 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        #순서가 뒤바뀌면
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

        #처음부터 현재 pivot의 앞자리까지
        quick_sort(array, start, right - 1)
        #현재 pivot의 뒷자리부터 끝까지
        quick_sort(array, right + 1, end)

quick_sort(array,0,len(array) - 1)
print(array)


---  
layout: post  
title:  "퀵 정렬(Quick Sort)"  
date:   2021-01-15 14:50:00  
category: Github
use_math: true
comments: true
---  


### 퀵 정렬이란?
대부분의 상황에서 가장 빠르다고 알려진 정렬 알고리즘이다.
(삽입 정렬 포스트에서도 언급했지만 거의 정렬된 상태의 배열이라면 삽입 정렬이 더 효율적일 수 있다.)\
\
여기서는 Pivot 이라는 개념이 사용되는데 (엑셀 피벗 테이블이나 선형대수에서 보았던 단어), 중심 축이라는 뜻이다.
퀵 정렬을 두 가지 파트로 나누어 살펴보자. 교재에서는 3개의 파트로 나누었으나 굳이 그럴 필요는 없을 것 같다.

### PART1
1.1 첫 번째 데이터를 Pivot으로 설정한다.\
1.2 왼쪽에서부터는 5보다 큰 데이터를 선택하고, 오른쪽에서부터는 5보다 작은 데이터를 선택한다.\
<img src="https://i.ibb.co/V3y5Zm6/quick1.png" alt="quick1" border="0">

1.3 둘의 자리를 바꾼다.
<img src="https://i.ibb.co/1v9cb9D/quick2.png" alt="quick2" border="0">
\

1.4 이를 계속하다 보면 Pivot보다 다음과 같이 큰 데이터와 작은 데이터가 순서가 뒤바뀌는 상황이 오게된다. 
<img src="https://i.ibb.co/Sm0xQs3/quick3.png" alt="quick3" border="0">
\

1.5 이 때는 선택한 두 데이터의 순서를 바꾸는 것이 아니라, 선택한 작은 수와 Pivot의 자리를 바꾼다.
그러면 Pivot의 왼쪽에는 모두 Pivot보다 작은 수가 오게 되고 오른쪽에는 모두 Pivot보다 큰 수가 오게 된다.
<img src="https://i.ibb.co/W3nhJbr/quick4.png" alt="quick4" border="0">

### PART2
2.1 다음과 같이 Pivot을 중심으로 나누어진 두 리스트에 대해 재귀적으로 다시 PART1을 수행한다.
<img src="https://i.ibb.co/r0q3dFf/quick5.png" alt="quick5" border="0">

#### 📌 재귀를 멈추는 조건
현재 리스트의 원소가 1개라면 정렬을 수행하지 않고 멈춘다. 


### 선택정렬 구현하기
```python
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

```
✅결과
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```


하지만 위와 같이 하나씩 세세히 구현하는 방법도 있는가하면, 파이썬의 특징을 이용해 아주 간결하게 코드를 짤 수도 있다고 한다.

```python
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
```

위의 코드와 같은 결과가 나온다.
간단하고 아주 좋다!
---  
layout: post  
title:  "삽입 정렬(Insertion Sort) 기초와 구현"  
date:   2021-01-13 17:14:00  
category: Github
use_math: true
comments: true
---  


### 삽입정렬(Insertion Sort)이란?
- 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입하는 방법
- 필요할 때만 자리를 바꾸므로 데이터가 거의 정렬되어 있을 때 효율적임
- 첫번째 데이터는 이미 정렬되었다고 판단하고, 두번째부터 시작

<img src="https://i.ibb.co/PcR0FpT/insertionsort.png" alt="insertionsort" border="0">

이미지는 중간 단계 중 하나만 만들어 보았다. 앞에 파란 카드들은 이미 정렬된 후이다. 이번에는 3이 적힌 카드를 정렬할 차례이다.\
이미 정렬된 카드들과 비교해 한 칸 씩 자리를 옮긴다. 비교만 하고 넘어가는 것이 아니라 실제로 위치를 옮기는 것이 특징이다.
왼쪽 수와 비교하다가 자신보다 작은 수인 0을 만나면 그 자리에서 멈춘다.

   
#### 삽입정렬 구현하기
```python
array = [7,5,9,0,3,1,6,2,4,8]

#첫번째 카드는 뛰어넘은 range
for i in range(1, len(array)):
    #자신부터 1까지 1씩 감소함
    for j in range(i, 0, -1):
        #자신보다 수가 크면 한 칸 옮기고,
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        #아니면 멈춤
        else:
            break
```
결과
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
\
반복문이 두 번 중첩되어 있기 때문에 O(N^2)의 시간 복잡도를 가지는 것은 선택 정렬과 같으나, 주어진 데이터가 거의 정렬되어 있다면 최선의 경우 O(N)까지도 가능.
이런 경우에는, 퀵 정렬 보다도 빠르다!
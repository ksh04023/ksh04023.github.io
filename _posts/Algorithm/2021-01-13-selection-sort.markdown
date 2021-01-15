---  
layout: post  
title:  "선택 정렬(Selection Sort)"  
date:   2021-01-13 17:14:00  
category: Github
use_math: true
comments: true
---  


### 선택정렬이란?
매번 가장 작은 것을 **선택**한다는 의미

- 전체 데이터에서 가장 작은 것을 맨 앞의 것과 자리를 바꿈
- 이중 반복문 필요, 시간 복잡도는 $$O(N)$$

#### 선택정렬 구현하기
```python
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #swap

print(array)
```
결과
```
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

파이썬의 너무나 간단한 swap 코드는 내가 코테에서 파이썬을 선택하게 된 큰 이유 중 하나이다. 물론 다른 언어에서 엄청나게 어렵다는 것은 아니지만, 파이썬을 처음 공부할 때 이런 것에 너무 빠져버린 것....😂 어떻게 이렇게 가능한 것인지는 메모리 측면에서 나중에 설명해보도록 하겠다.
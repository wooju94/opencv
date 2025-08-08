import numpy as np
# np.lexsort()
# 여러 개의 키 배열을 전달할 때, 맨 마지막 배열을 1차 기준, 그 앞의 배열을 그 다음
# 맨 뒤에 있는 배열이 가장 우선순위가 높음
# 결과는 정렬된 순서의 인덱스 배열
# np.lexsort((키2, 키1)) 키 1부터 정렬 그다음 키 2로 정렬

ndarr1 = np.array([1,5,1,4,4])
ndarr2 = np.array([9,4,0,4,0])
result = np.lexsort((ndarr2,ndarr1))

# 1,1,4,4,5
# 인덱스 : 0,2,3,4,1
# ndarr1 값이 같은 경우 ndarr2로 비교 
# [2,0,4,3,1] => ndarr2의 값을 따라서 ndarr1의 인덱스 순서를 바꿈

print(result)

surnames = ('Hertz', 'Galilei', 'Hertz')
first_names = ('Heinrich', 'Galileo', 'Gustav')
result = np.lexsort((first_names,surnames))

print(result)

# 1, 2, 0

x = [
    [1,2,3,4],
    [4,3,2,1,],
    [2,1,4,3,]
    ]
y = [
    [2,2,1,1],
    [1,2,1,2],
    [1,1,2,1]
]
print(np.lexsort((x,y),axis=1))

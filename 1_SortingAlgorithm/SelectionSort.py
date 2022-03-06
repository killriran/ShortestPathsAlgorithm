# 선택 정렬(Selection Sort)
# 무작위로 정렬된 데이터가 있을 때, 가장 작은 데이터를 선별해 가장 앞의 인덱스 위치에 놓고
# 그 다음으로 작은 데이터를 선별해 두 번째 인덱스 위치에 놓고... 
# 계속적으로 하여 N-1번 반복하는 알고리즘이다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[j] < array[min_idx]:
            min_idx = j
    # 위치 스와핑 하기
    array[i], array[min_idx] = array[min_idx], array[i]

print(array) 
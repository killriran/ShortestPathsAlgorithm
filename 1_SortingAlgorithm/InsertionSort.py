# 삽입 정렬(Insertion Sort)
# 데이터를 하나씩 확인하면서 그 데이터의 적절한 위치에 삽입
# 데이터의 가장 첫 번째에 위치한 데이터는 정렬되었다고 가정하고 시작

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):    # 0번째 데이터는 정렬된 것으로 가정
    for j in range(i, 0, -1):     # i번째 부터 1번째 idx까지 왼쪽으로 이동
        if array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break

print(array)
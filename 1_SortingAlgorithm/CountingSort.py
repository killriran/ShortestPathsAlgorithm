array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

# 데이터 범위만큼의 빈 리스트 정의 => array의 길이만큼이라는 뜻은 아님!!! 왜냐면 중복된 값이 있을 수 있기 때문!
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')
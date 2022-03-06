# 퀵 정력(Quick Sort)
# 기준 데이터를 설정하고 그 기준보다 큰 데이터, 작은 데이터의 위치를 바꾸는 아이디어
# 피벗(Pivot)

# 나동분 10분 강좌 : https://www.youtube.com/watch?v=O-O-90zX-U4&t=2s

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:    # 원소 개수가 1개이거나 end가 -1일 경우 멈추기
        return
    # 얘네들은 index 위치를 나타냄!
    pivot = start
    left = start + 1
    right = end
    # 왼,오른쪽이 엇갈리지 않을 경우 계속 반복
    while left <= right:
        while left <= end and array[left] < array[pivot]:
            left += 1
        while right > start and array[right] > array[pivot]:
            right -= 1
        # 왼, 오 이동하다가 엇갈릴 때 -> right와 pivot 교체
        if right < left:
            array[pivot], array[right] = array[right], array[pivot]
        # 왼, 오 엇갈리지 않으면 -> right, left 값 교체
        else:
            array[left], array[right] = array[right], array[left]
    # 엇갈린 다음엔 파티션이 이루어지고 피벗을 기준으로 왼, 오 퀵정렬 재귀적으로 수행
    quick_sort(array, start, right-1)  # right자리에 pivot이 있기 때문!
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)


# 재귀함수 이용

def quick_sort(array):
    # 재귀함수 종단 조건
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    # Pivot값 기준으로 왼쪽은 모두 Pivot보다 작은 값. 오른쪽은 큰 값들
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

res = quick_sort(array)
print(res)

# 데이터가 무작위로 입력될 경우 퀵 정렬을 사용하면 빠르게 동작할 확률이 높다. 
# 하지만 이미 데이터가 정렬되어 있는 경우(이럴 때 삽입 정렬을 사용하는 게 적절하다고 위에서 언급했었다!)
# 매우 느리게 동작하게 된다
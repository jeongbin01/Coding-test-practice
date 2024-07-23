def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    # (음식 시간, 인덱스)를 저장하는 리스트를 만듭니다.
    food_with_index = [(time, idx + 1) for idx, time in enumerate(food_times)]
    
    # 음식 시간을 기준으로 정렬합니다.
    food_with_index.sort()
    
    total_time = 0  # 총 경과 시간
    previous_time = 0  # 이전 음식 시간
    length = len(food_times)  # 남은 음식 개수

    for i, (time, idx) in enumerate(food_with_index):
        # 현재 가장 적은 음식 시간
        current_time = time - previous_time
        
        if total_time + current_time * length > k:
            # 남은 시간 동안 먹을 음식 찾기
            remaining_foods = sorted(food_with_index[i:], key=lambda x: x[1])
            return remaining_foods[(k - total_time) % length][1]

        total_time += current_time * length
        previous_time = time
        length -= 1

    return -1

# 예제 사용
food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))  # 출력: 1
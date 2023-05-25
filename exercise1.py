def calculate_water(heights):
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    left_max[0] = heights[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i-1], heights[i])
    right_max[n-1] = heights[n-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(right_max[i+1], heights[i])
    total_water = 0
    for i in range(n):
        water = min(left_max[i], right_max[i]) - heights[i]
        if water > 0:
            total_water += water
    return total_water
print(calculate_water([4, 2, 0, 3, 2, 5]))
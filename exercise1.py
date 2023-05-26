def water(heights):
    left_max, right_max, left_max[0], right_max[len(heights)-1], total_water = [0] * len(heights), [0] * len(heights), heights[0], heights[len(heights) - 1], 0
    for i in range(1, len(heights)):
        left_max[i] = max(left_max[i-1], heights[i])
        right_max[len(heights) - i - 1] = max(right_max[len(heights) - i], heights[len(heights) - i - 1])
    for i in range(len(heights)):
        total_water += min(left_max[i], right_max[i]) - heights[i] if min(left_max[i], right_max[i]) - heights[i] > 0 else + 0
    return total_water
print(water([4, 2, 0, 3, 2, 5]))
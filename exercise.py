import time
nums = [1,2,3,2]
class Solution:
    def containsDuplicate(self, nums: list[int]):
        num = []
        for i in range(len(nums)):
            if nums[i] in num:
                return True
                break
            else:
                num.append(nums[i])
        return False
############################Проверка############################
st = time.time()
print(Solution.containsDuplicate(None, nums))             # -> True
et = time.time()
print(f"Время выполнения кода: {et-st} секунд")
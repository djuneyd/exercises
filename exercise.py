import time
class Solution:
    def containsDuplicate(self, nums: list[int]):
        return True if len(nums) != len(set(nums)) else False
############################Проверка############################
st = time.time()
print(Solution.containsDuplicate(None, [1,2,3,1]))             # -> True
print(Solution.containsDuplicate(None, [1,2,3,4]))             # -> False
print(Solution.containsDuplicate(None, [1,1,1,3,3,4,3,2,4,2])) # -> True
et = time.time()
print(f"Время выполнения кода: {et-st} секунд")
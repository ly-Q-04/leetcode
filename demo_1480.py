class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        dp = len(nums)*[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + dp[i -1]
        return dp

# 调用函数并打印结果
if __name__ == "__main__":
    # 创建Solution实例
    solution = Solution()
    # 定义测试用例
    nums = [1, 2, 3, 4]
    # 调用runningSum方法
    result = solution.runningSum(nums)
    # 打印结果
    print("输入:", nums)
    print("输出:", result)

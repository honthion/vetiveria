# coding:utf-8
#
# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。
#
# 你可以无限次地完成交易，但是你每次交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。
#
# 返回获得利润的最大值。
#
# 示例 1:
#
# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 注意:
#
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
class Solution(object):

    # https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
    def maxProfit121(self, prices):
        max_cur, maxs = 0, 0
        for i in xrange(1, len(prices)):
            max_cur += prices[i] - prices[i - 1]
            max_cur = max(max_cur, 0)
            maxs = max(max_cur, maxs)
        return maxs

    def maxProfit122(self, prices):
        sum([b - a for (a, b) in zip(prices, prices[1:]) if b - a > 0])
        return sum(max(prices[i] - prices[i - 1], 0) for i in xrange(1, len(prices) - 1))

    def maxProfit123(self, prices):
        buy_one, sell_one, buy_two, sell_two = float('inf'), 0, float('inf'), 0
        for p in prices:
            buy_one = min(buy_one, p)
            sell_one = max(sell_one, p - buy_one)
            buy_two = min(buy_two, p - sell_one)
            sell_two = max(sell_two, p - buy_two)
        return sell_two

    def maxProfit188(self, k, prices):
        length = len(prices)
        if k >= length / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i > j)
        global_max = [[0] * length for _ in xrange(k + 1)]
        for i in xrange(1, k + 1):
            # The max profit with i transations and selling stock on day j.
            local_max = [0] * length
            for j in xrange(1, length):
                profit = prices[j] - prices[j - 1]
                local_max[j] = max(
                    # We have made max profit with (i - 1) transations in (j - 1) days.
                    # For the last transation, we buy stock on day (j - 1)  and sell it on day j.
                    global_max[i - 1][j - 1] + profit,
                    # We have made max profit with (i - 1) transations in (j - 1) days.
                    # For the last transation, we buy stock on day j and sell it on the same day, so we have 0 profit,
                    # apparently we do not have to add it.
                    global_max[i - 1][j - 1],
                    # We have made profit in (j - 1) days.
                    # We want to cancel the day (j - 1) sale and sell it on day j.
                    local_max[j - 1] + profit)

                global_max[i][j] = max(global_max[i][j - 1], local_max[j])
        return global_max[k][-1]

    def maxProfit188_01(self, k, prices):
        length = len(prices)
        if k >= length / 2:
            return sum(i - j for i, j in zip(prices[1:], prices[:-1]) if i > j)
        local_max = [0] * (k + 1)
        global_max = [0] * (k + 1)

        for i in range(1, length):
            diff = prices[i] - prices[i - 1]
            for j in range(k, 0, -1):
                local_max[j] = max(local_max[j], global_max[j - 1]) + diff
                global_max[j] = max(local_max[j], global_max[j])
        return global_max[k]

    @staticmethod
    def quickSolve(prices):
        profit, length = 0, len(prices)
        for i in xrange(1, length):
            profit += max(prices[i] - prices[i - 1], 0)
        return profit

    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        countx, sumx = 0, 0
        max, min = prices[-1], prices[-1]
        for i in xrange(len(prices) - 1, 0, -1):
            max = prices[i] > max and prices[i] or max
            min = prices[i - 1] < min and prices[i - 1] or min
            if max - min > fee:
                countx += 1
                sumx += max - min
                if i - 2 > 0:
                    max = prices[i - 2]
                    min = prices[i - 2]
        return sumx - countx * fee


minprice = float("inf")
print minprice - 0
prices = [3, 3, 5, 0, 0, 3, 1, 4]
fee = 2
# sumsx = Solution().maxProfit123(prices)
sumsx = Solution().maxProfit188(2, prices)

print sumsx

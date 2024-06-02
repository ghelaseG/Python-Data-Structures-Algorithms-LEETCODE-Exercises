"""
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:



Each element of the input list is a positive integer representing the stock price for a specific day.



Function signature: def max_profit(prices):

Example:

Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""

def max_profit(prices):
    #we set min_price to infinity, because every price in the list will be less than this, so we can updated in the first iteration
    min_price = float('inf')
    #here we initiliaze and update the max profit
    max_profit = 0
    
    for price in prices:
        #this update the min value between min price and curretnt stock price
        min_price = min(min_price, price)
        #here we calculate the profit that could be made by buying the stock at the minimum price
        profit = price - min_price
        max_profit = max(max_profit, profit)
        
    return max_profit
    
    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")
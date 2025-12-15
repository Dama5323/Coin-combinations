#Breaking the Problem into Subproblems -to count the number of ways to make sum x using the given coins without considering order.
#1. Skip the current coin - Move to the next coin
#2. Pick the current coin (if possible) - Reduce the sum

# dp[s] represents the number of ways to form sum s using the coins processed so far
#Looping over coins first ensures:

    #Each combination is counted once
    #Order is ignored
    #avoid permutations like (2,3) and (3,2) being counted separately

# Transition Formula - If we include the current coin, then the number of ways to make sum s increases by the number of ways
#Base Case - There is exactly one way to make sum 0: by choosing no coins.
# MOD = The modulo controls the size of the output,but the constraints control how fast and memory-efficient our solution must be.


def coin_combinations_ii(n, x, coins):
    """
    Returns the number of distinct combinations to form sum x
    using unlimited coins, where order does not matter.
    """
    MOD = 10**9 + 7

    dp = [0] * (x + 1)
    dp[0] = 1  # Base case

    for coin in coins: #We pick one coin type at a time (loop over coins first)
        if coin > x: #No need to process coins larger than x (coin is bigger than the sum we want to form)
            continue 
        for s in range(coin, x + 1): #form all sums where this coin can be used
            dp[s] = (dp[s] + dp[s - coin]) % MOD #combinations using current and previous coins and Modulo keeps values within limits

    return dp[x]


"""
Variables: 
n - number of different coin types
x - target sum to form
map (read input and convert to integers)
input() → reads a line of text, e.g. "2 3 5"
.split() → splits it into a list of strings: ["2", "3", "5"]
list(...) → collects into a list [2, 3, 5]
coins = ... → stores that list in the variable coins
.sort() → sorts the list of coins in ascending order (prevents duplicate counting)
"""
n, x = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()

print(coin_combinations_ii(n, x, coins))


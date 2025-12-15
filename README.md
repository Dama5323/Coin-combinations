# Coin Combinations II

A Python implementation to count the **number of distinct combinations** to form a target sum `X` using unlimited coins, where **order does not matter**. This solution uses **dynamic programming** for efficiency and handles large numbers with modulo arithmetic.

---

## Problem Statement

Given `n` types of coins with positive integer values and a target sum `X`, calculate the **number of ways to form the sum** using any number of coins.  
**Important:** The order of coins does **not** matter (combinations, not permutations).

**Constraints:**

- \( 1 \le n \le 100 \)
- \( 1 \le x \le 10^6 \)
- \( 1 \le c_i \le 10^6 \)  

**Example:**

Input:
3 11
2 3 5

Output:
3

```yaml

Explanation: There are 3 ways to make 11 using coins [2, 3, 5] ignoring order.

---

## Solution

This problem is solved using **Dynamic Programming (DP)**:

1. **Subproblems**: Count ways to make sum `s` using coins seen so far.
2. **Decisions**:
   - Skip the current coin → move to next coin
   - Pick the current coin (if sum allows) → reduce the sum
3. **DP Array**: `dp[s]` = number of ways to make sum `s`.
4. **Transition Formula**:  
```

### dp[s] += dp[s - coin] (mod 10^9 + 7)
``` yaml
5. **Base Case**: `dp[0] = 1` → One way to make sum 0 (use no coins).

---

## Usage

```bash
# Run the program
python coin_combinations.py

# Example input (stdin):
3 11
2 3 5

# Expected output:
3
```

### Features

- Efficient O(n * X) solution.
- Handles large sums with modulo 
- Ignores order of coins to avoid duplicate combinations.


### Author

Damaris Chege
GitHub: https://github.com/Dama5323
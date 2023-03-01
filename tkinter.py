def min_coin_change(coins, amount, excluded_coins=[]):
    coins = sorted([c for c in coins if c not in excluded_coins], reverse=True)
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            if min_coins[i - coin] != float('inf'):
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
    return min_coins[amount]

# Example usage:
coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 123
excluded_coins = [2, 100]
min_coins = min_coin_change(coins, amount, excluded_coins)
print(f"Minimum coins needed to make {amount}p (excluding {excluded_coins}p coins): {min_coins}")

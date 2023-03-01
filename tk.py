import tkinter as tk

# Define the coin denominations
COINS = [1, 2, 5, 10, 20, 50, 100, 200]

class MinCoinChangeGUI:

    def __init__(self, master):
        self.master = master
        master.title("Minimum Coin Change Calculator")

        # Create the GUI elements
        self.coin_vars = [tk.IntVar() for _ in COINS]
        self.exclude_vars = [tk.BooleanVar() for _ in COINS]
        self.amount_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Create the coin denomination checkboxes
        coin_frame = tk.Frame(self.master)
        coin_frame.pack()
        for i, coin in enumerate(COINS):
            tk.Checkbutton(coin_frame, text=f"{coin}p", variable=self.coin_vars[i]).grid(row=i//4, column=i%4)

        # Create the exclude checkboxes
        exclude_frame = tk.Frame(self.master)
        exclude_frame.pack()
        for i, coin in enumerate(COINS):
            tk.Checkbutton(exclude_frame, text=f"{coin}p", variable=self.exclude_vars[i]).grid(row=i//4, column=i%4)

        # Create the amount entry and result label
        amount_frame = tk.Frame(self.master)
        amount_frame.pack()
        tk.Label(amount_frame, text="Target Amount:").pack(side=tk.LEFT)
        tk.Entry(amount_frame, textvariable=self.amount_var).pack(side=tk.LEFT)
        tk.Label(amount_frame, text="p").pack(side=tk.LEFT)

        result_frame = tk.Frame(self.master)
        result_frame.pack()
        tk.Label(result_frame, text="Minimum Coins Needed:").pack(side=tk.LEFT)
        tk.Label(result_frame, textvariable=self.result_var).pack(side=tk.LEFT)

        # Create the calculate button
        tk.Button(self.master, text="Calculate", command=self.calculate).pack()

    def calculate(self):
        # Get the user inputs
        coins = [COINS[i] for i, var in enumerate(self.coin_vars) if var.get() == 1]
        amount = int(self.amount_var.get())
        excluded_coins = [COINS[i] for i, var in enumerate(self.exclude_vars) if var.get() == 1]

        # Calculate the minimum coins needed
        min_coins = self.min_coin_change(coins, amount, excluded_coins)

        # Display the result
        self.result_var.set(str(min_coins))

    def min_coin_change(self, coins, amount, excluded_coins=[]):
        coins = sorted([c for c in coins if c not in excluded_coins], reverse=True)
        min_coins = [float('inf')] * (amount + 1)
        min_coins[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if min_coins[i - coin] != float('inf'):
                    min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)
        return min_coins[amount]


root = tk.Tk()
gui = MinCoinChangeGUI(root)
root.mainloop()

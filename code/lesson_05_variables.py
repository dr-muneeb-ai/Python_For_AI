"""AI models the profile card and calculates the cost per conversation"""

model = "llama3.2"
cont_win = 120000
tokens_price = 1.00
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model} {type(model)}")
print(f"Context window: {cont_win} tokens {type(cont_win)}")
print(f"Price per 1K tokens: {tokens_price} PKR {type(tokens_price)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

TPC = int(input("Tokens per chat: "))


calculaton = round(TPC / 1000 * tokens_price, 2)
print(f"Estimated cost: {calculaton:.2f} PKR")

CPD = int(input("Per day chat: "))
monthly_cost = round(calculaton * CPD * 30, 2)
print(f"Estimated monthly cost: {monthly_cost:.2f} PKR")
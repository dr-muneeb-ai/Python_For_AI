"""AI models the profile card and calculates the cost per conversation."""

model = "llama3.2"
cont_win = 120000
tokens_price = 1.00
runs_locally = True

print("--- AI Model Profile Card ---")
print(f"Model: {model} {type(model)}")
print(f"Context window: {cont_win} tokens {type(cont_win)}")
print(f"Price per 1K tokens: {tokens_price} PKR {type(tokens_price)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

tokens_per_chat = int(input("Tokens per chat: "))


estimated_cost = round(tokens_per_chat / 1000 * price_per_1k_tokens, 2)
print(f"Estimated cost: {estimated_cost:.2f} PKR")


chats_per_day = int(input("Chats per day: "))
monthly_cost = round(estimated_cost * chats_per_day * 30, 2)
print(f"Estimated monthly cost: {monthly_cost:.2f} PKR")
""" small model router using Conditions and Operators. """

task = input("(code / private / chat): ").strip().lower()

tokens = int(input("Estimated tokens: "))

cloud_price = 0.5

if task == "private":
    model = "llama3.2 (local, Ollama)"
    price = 0.0

elif task == "code":
    model = "Claude (cloud, coding)"
    price = cloud_price

elif task == "chat":
    model = "Small cloud model (chat)"
    price = cloud_price

else:
    model = "Invalid task"

if tokens > 4000:
    warning = "Warning: Long request."
else:
    warning = "Length is perfect"

cost = (tokens / 1000) * price
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()
if paid_user == "no" and tokens > 2000:
    upgrade_message = "Upgrade to send long requests."
else:
    upgrade_message = "No upgrade message."
print("\n" + "=" * 40)
print(f"Task: {task}")
print(f"Chosen model: {model}")
print(f"Estimated tokens: {tokens}")
print(f"Estimated cost: {cost:.2f} PKR")
print(warning)
print(upgrade_message)
print("=" * 40)
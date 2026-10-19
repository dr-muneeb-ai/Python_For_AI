
""" Make an AI model identification card and figure out how much it will cost. """

import calendar
from datetime import date
MODEL_NAME: str = "gemma3:1b"
cont_window: int = 9123
temperature: float = 0.5
local_run: bool = True

print("== AI Model Profile Card ==")
print(f"Model Name: {MODEL_NAME} | Type: {type(MODEL_NAME)}")
print(f"Context Window: {cont_window} | Type: {type(cont_window)}")
print(
    f"Temperature: {temperature} | Type: {type(temperature)}"
)
print(f"Runs Locally: {local_run} | Type: {type(local_run)}")

tokens_used = int(input("\nTokens used per chat: "))

chat_cost = (tokens_used / 1000) * temperature

print(f"Estimated cost = {chat_cost:.2f} PKR")

perday_cost = int(input("Chats per day: "))
today = date.today()
months=calendar.monthrange(today.year, today.month)[1]
monthly_cost = chat_cost * perday_cost * months

print(f"Current date: {today}")
print(f"Estimated monthly cost: {monthly_cost:.2f} PKR")
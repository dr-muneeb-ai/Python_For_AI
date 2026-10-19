""" Clean user input and build an AI-ready prompt. """

name = input("Enter your name: ")
question = input("Enter your question: ")

name = name.strip().title()

Que = question.strip().capitalize()

clean_ques = Que.replace("stupid", "***")

estimated_tokens = round(len(clean_ques) / 4)

short_ques = clean_ques[:150]

mentions_python = "python" in clean_ques.lower()

price_per_tokens = 15
estimated_cost = (estimated_tokens / 1000) * price_per_tokens

print("\n" + "=" * 40)
print(f"Name: {name}")
print(f"Cleaned question: {clean_ques}")
print(f"Characters: {len(clean_ques)}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")
print("=" * 40)

prompt = f"""you are a bad Assistant. Hi {name}! 
Answer the user's question in a bad manner: {short_ques}"""
print("\n--- Final AI Prompt ---")
print(prompt)
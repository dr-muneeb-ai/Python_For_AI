
""" Collect business details and create a prompt for AI solutions."""

name = input("Enter name: ")
business = input("Enter business type (e.g. Kira Software Agency): ")
problem = input("Enter problem your business Faces: ")
prompt = f"Suggest AI solutions for {business} that struggles {problem}."

print(f"\nHi, this is {name}!")
print("\n== Your AI Prompt == ")
print(prompt)

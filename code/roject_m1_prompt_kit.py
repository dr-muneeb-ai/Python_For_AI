"""
AI Prompt Kit for Bright Minds Tuition Centre.

asks five straightforward questions of the owner of a tutoring center and prints
Four ready-to-use AI prompts for WhatsApp conversation, business expansion, parent assistance, and marketing.
"""

B_N = input("Tuition Centre Name: ").strip()
B_T = input("Centre Type (e.g. tuition centre): ").strip()
city = input("City: ").strip()
customers = input("Main Students (e.g. Matric, FSc, O/A Level): ").strip()

budget = int(input("Monthly Budget (PKR): "))

if B_N == "":
    B_N = "Bright Minds Tuition Centre"

if B_T == "":
    B_T = "Tuition centre"

if city == "":
    city = "your city"

if customers == "":
    customers = "school and college students"
line = "=" * 41
print(f"\n{line}")
print(f"   AI Prompt Kit for {B_N}")
print(line)
print("\n[1] Student Marketing")
print(
    f"Make a welcoming and appealing social media post for "
    f"{B_N}, a {B_T} in {city}.\n"
    f"Aim for pupils who study {customers}. Emphasize quality "
    "instruction, encouraging instructors, and test-taking. "
    "Add a single request for admittance. "
)
print("\n[2] Parent and Student Support")
print(
    f"You are a helpful student support assistant at {B_N}\n"
    "When a parent inquires about their child's academic achievement, write a kind and professional response. Find out which class."
    "or topic they require assistance with. Make sure your response is understandable and kind."
)
print("\n[3] Tuition Centre Growth")
print(
    f"Suggest 3 low-cost ways for {B_N}, a "
    f"{B_T} in {city}, to attract more students "
    f"studying {customers}.\n"
    f"The monthly budget is {budget} PKR. Give practical "
    "steps, estimated costs and expected benefits."
)
print("\n[4] WhatsApp Admission Auto-Reply")
print(
    f"You are the WhatsApp assistant of {B_N} "
    f"in {city}.\n"
    f"Write a friendly auto-reply for students and parents "
    f"interested in {customers}."
    "They may ask on fees, courses, timings, and admissions, and inform him we will react after business hours," 
    "you say as you greet them."
    "Don't exceed four lines."
)
print(f"\n{line}")
print("Copy any prompt and paste it into ChatGPT, Claude or Ollama.")
print(line)
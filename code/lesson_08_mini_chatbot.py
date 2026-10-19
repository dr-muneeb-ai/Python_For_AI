"""Local Tutor Center
The bot uses fundamental rules to reply to the majority of problems
"""

BOT = "Bright Minds Bot"
print(f"{BOT}: Hi! How can I help you today? Type 'bye' to exit.")

name = input(f"{BOT}: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"{BOT}: Nice to meet you, {name}!")

def show_menu():
    """Display the available chatbot options."""
    print("\n" + "=" * 40)
    print("[=======TUITION CENTRE HELP MENU=======]")
    print("=" * 40)
    print("You can ask me about:")
    print("1. Fees       - Type (fee, fees, price, cost)")
    print("2. Timings    - Type (time, timing, open, hours)")
    print("3. Courses    - Type (course, teaching subjects, class)")
    print("4. Location   - Type (where, location, address)")
    print("5. Admission  - Type (admission, enroll, register)")
    print("6. Complaint  - Type (refund)")
    print("7. Problem    - Type (problem, issue, complaint)")
    print("8. Greeting   - Type (hi, hello, salam)")
    print("9. Human Help - Type (human, agent)")
    print("10. Exit       - Type (bye, exit)")
    print("=" * 40)

 
count = 0; unanswered = 0; complaints = 0
while True:
    show_menu()
    message = input(f"{name}: ").strip().lower()
    count += 1

    if message == "bye" or message == "exit":
        print(f"{BOT}: Goodbye, {name}! Please come back next time brother.")
        break

    elif message == "":
        print(f"{BOT}: Type Question otherwise Go a Head.")

    elif "agent" in message or "human" in message:
        print(f"{BOT}: Connecting you to a human...")
        break

    elif "refund" in message:
        complaints += 1
        print(f"{BOT}: Don't even dream of it. wait 1 hour otherwise Go a Head")

    elif "complaint" in message or "problem" in message or "issue" in message:
        print(f"{BOT}: I don't care about your problem. Get out")

    elif "hour" in message or "hours" in message or "open" in message or "time" in message or "timing" in message:
        print(f"{BOT}: Classes run 3 pm to 8 pm, Monday to Sunday. Any Question ︻デ═一")

    elif "fee" in message or "fees" in message or "price" in message or "cost" in message or "how much" in message:
        print(f"{BOT}: Matric 100,000 PKR/month, FSc 150,000 PKR/month, O/A Level 250,000 PKR/month.")

    elif "subject" in message or "class" in message or "teaching subjects" in message or "course" in message:
        print(f"{BOT}: We teach Thieving, Criminology, Cyber Theft, Shoplifting, Social engineering")

    elif  "where" in message or "location" in message or "address" in message:
        print(f"{BOT}: We are in Diaz Mension, near Gangster state.")

    elif "admission" in message or "join" in message or "enroll" in message or "register" in message:
        print(f"{BOT}: Admissions are open. WhatsApp us on 0326-0999091 to book a free demo class.")

    elif message == "hi" or message == "hello" or message.startswith("Assalam o Alaikum"):
        print(f"{BOT}: Han, {name}! What do you want now?")
    else:
        unanswered += 1
        prompt = (
            "You are the Excellent assistant of Bright Minds Tuition Centre. "
            f"Answer in 2 lines: {message}"
        )
        print(f"{BOT}: I am not sure yet. In Module 2, an AI will answer using this prompt:")
        print(f"  {prompt}")

print("=" * 40)
print(f"Chat summary: {count} messages, {unanswered} unanswered, {complaints} complaints.")
print("=" * 40)

"""
Bright Minds Tuition Center - AI Content Studio

Features:
- Original mini chatbot FAQs and responses
- /menu: Generate descriptions for all listed courses
- /post fun|premium|urgent: Create a social media post
- /price <level>: Show the stored fee without using AI
- /reset: Clear AI chat memory
- AI chat for questions not handled by existing rules
- Session report with usage statistics
"""

import time
from langchain.chat_models import init_chat_model

# ------------------------------------------------ SETUP

BOT = "Bright Minds Bot"
BUSINESS_NAME = "Bright Minds Tuition Center"
WHATSAPP = "0326-0999091"

config = {
    "model_name": "llama3.2",
    "provider": "ollama",
    "max_messages": 6,
    "cloud_price_per_1k": 0.5,
}

facts = {
    "name": BUSINESS_NAME,
    "hours": "3 pm to 8 pm, Monday to Sunday",
    "location": "Diaz Mension, near Gangster state",
    "whatsapp": WHATSAPP,

    "courses": [
        "Thieving",
        "Criminology",
        "Cyber Theft",
        "Shoplifting",
        "Social engineering",
    ],

    "fees": {
        "matric": 100000,
        "fsc": 150000,
        "o/a level": 250000,
    },
}

tones = {
    "fun": "playful and energetic, with short sentences",
    "premium": "professional, elegant and focused on quality",
    "urgent": "exciting and action-oriented, without inventing deadlines",
}

# Create the models once
precise = init_chat_model(
    config["model_name"],
    model_provider=config["provider"],
    temperature=0.2,
)

creative = init_chat_model(
    config["model_name"],
    model_provider=config["provider"],
    temperature=0.8,
)

# ------------------------------------------------ AI FACTS

fee_lines = ""
for level, price in facts["fees"].items():
    fee_lines += f"- {level.upper()}: {price:,} PKR per month\n"

course_lines = ""
for course in facts["courses"]:
    course_lines += f"- {course}\n"

system_text = f"""
You are the assistant of {BUSINESS_NAME}.
Answer in 2 short lines.
Only use the facts below. Never invent prices, timings, addresses,
course details or offers. If you do not know an answer, say so
and suggest contacting the center.

Courses:
{course_lines}

Fees:
{fee_lines}

Opening hours: {facts['hours']}
Location: {facts['location']}
WhatsApp: {facts['whatsapp']}
"""

system_message = {
    "role": "system",
    "content": system_text,
}

messages = [system_message]

# ------------------------------------------------ COUNTERS

message_count = 0
answered_count = 0
unanswered_count = 0
complaint_count = 0

chat_answers = 0
menu_descriptions = 0
post_count = 0
price_answers = 0

total_tokens = 0
total_seconds = 0.0

# ------------------------------------------------ MENU

def show_menu():
    print("\n" + "=" * 48)
    print("          BRIGHT MINDS TUITION CENTER")
    print("                  HELP MENU")
    print("=" * 48)

    print("FAQ OPTIONS")
    print("  Greetings      : hi, hello, salam")
    print("  Courses        : course, subject, class")
    print("  Fees           : fee, fees, price, cost")
    print("  Timings        : time, timing, hours, open")
    print("  Location       : where, location, address")
    print("  Admissions     : admission, enroll, register")
    print("  Complaints     : complaint, problem, issue, refund")
    print("  Human support  : human, agent")
    print()
    print("AI STUDIO COMMANDS")
    print("  /menu          : Generate all course descriptions")
    print("  /post fun      : Create a fun social media post")
    print("  /post premium  : Create a professional post")
    print("  /post urgent   : Create an action-oriented post")
    print("  /price matric  : Check Matric fees")
    print("  /price fsc     : Check FSc fees")
    print("  /price o/a level : Check O/A Level fees")
    print("  /reset         : Clear AI chat memory")
    print("  bye / exit     : End the session")
    print("=" * 48)


print("=" * 48)
print(f"  {BUSINESS_NAME} - AI Content Studio")
print("=" * 48)

C_N = input(f"{BOT}: What is your name? ").strip().title()

if C_N == "":
    C_N = "Friend"

print(f"{BOT}: Nice to meet you, {C_N}!")

# ------------------------------------------------ MAIN LOOP

while True:
    show_menu()

    customer_message = input(f"{C_N}: ").strip()
    lower_text = customer_message.lower()
    message_count += 1

    # ------------------------------------------------ /menu

    if lower_text == "/menu":
        menu_items = []

        for course in facts["courses"]:
            start = time.perf_counter()

            response = creative.invoke([
                {
                    "role": "system",
                    "content": (
                        "Write one short, professional course description. "
                        "Do not invent course features or make promises."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Write one sentence of at most 20 words for the "
                        f"{course} course at {BUSINESS_NAME}. "
                        "Do not mention a price or unsupported facts."
                    ),
                },
            ])

            total_seconds += time.perf_counter() - start

            usage = response.usage_metadata or {}
            total_tokens += usage.get("total_tokens", 0)
            menu_descriptions += 1

            menu_items.append((course, response.content))

        print("\n" + "-" * 48)
        print("COURSE DESCRIPTIONS")

        for number, item in enumerate(menu_items, start=1):
            print(f"\n{number}. {item[0]}")
            print(f"   {item[1]}")

        print("-" * 48)
        answered_count += 1

    # ------------------------------------------------ /post

    elif lower_text == "/post" or lower_text.startswith("/post "):
        tone_name = lower_text[5:].strip()

        if tone_name not in tones:
            print(f"{BOT}: Tone not found. Using fun.")
            tone_name = "fun"

        start = time.perf_counter()
        post_text = ""

        print(f"\n{BOT}: Generating {tone_name} social media post...\n")

        for chunk in creative.stream([
            {
                "role": "system",
                "content": (
                    "Write a concise social media post using only "
                    "the supplied business facts. Do not invent offers."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Write a post of at most 4 lines for {BUSINESS_NAME}. "
                    f"Tone: {tones[tone_name]}. "
                    f"Courses: {course_lines} "
                    f"Fees: {fee_lines} "
                    f"Hours: {facts['hours']}. "
                    f"WhatsApp: {WHATSAPP}."
                ),
            },
        ]):
            content = chunk.content

            if isinstance(content, str):
                print(content, end="", flush=True)
                post_text += content

            if chunk.usage_metadata:
                total_tokens += chunk.usage_metadata.get(
                    "total_tokens", 0
                )

        print()
        total_seconds += time.perf_counter() - start
        post_count += 1
        answered_count += 1

        # Roman Urdu version
        start = time.perf_counter()

        urdu_response = precise.invoke([
            {
                "role": "system",
                "content": (
                    "Translate the following social media post into "
                    "natural Roman Urdu. Keep names and numbers unchanged."
                ),
            },
            {
                "role": "user",
                "content": post_text,
            },
        ])

        total_seconds += time.perf_counter() - start

        usage = urdu_response.usage_metadata or {}
        total_tokens += usage.get("total_tokens", 0)

        print("\nRoman Urdu:")
        print(urdu_response.content)
        print()

    # ------------------------------------------------ /price

    elif lower_text == "/price" or lower_text.startswith("/price "):
        item_name = lower_text[6:].strip()
        price_answers += 1

        if item_name == "":
            print(f"{BOT}: Please type a level, e.g. /price matric")

        else:
            price = facts["fees"].get(item_name, -1)

            if price == -1:
                print(
                    f"{BOT}: Sorry, {item_name.title()} is not "
                    "in the fee list."
                )
                print("     Available: Matric, FSc, O/A Level.")
            else:
                print(
                    f"{BOT}: {item_name.upper()} fees are "
                    f"{price:,} PKR per month."
                )

            answered_count += 1

    # ------------------------------------------------ /reset

    elif lower_text == "/reset":
        messages = [system_message]
        print(f"{BOT}: Chat memory cleared.")
        answered_count += 1

    # ------------------------------------------------ ORIGINAL MINI CHATBOT

    elif lower_text == "" :
        print(f"{BOT}: Type Question otherwise Go a Head.")

    elif lower_text == "bye" or lower_text == "exit":
        print(
            f"{BOT}: Goodbye, {C_N}! "
            "Please come back next time brother."
        )
        break

    elif "agent" in lower_text or "human" in lower_text:
        answered_count += 1
        print(f"{BOT}: Connecting you to a human...")
        break

    elif any(word in lower_text for word in
             ["refund", "complaint", "problem", "issue"]):
        complaint_count += 1
        answered_count += 1
        print(
            f"{BOT}: Don't even dream of it. "
            "wait 1 hour otherwise Go a Head"
        )

    elif "complaint" in lower_text or "problem" in lower_text or "issue" in lower_text:
        print(f"{BOT}: I don't care about your problem. Get out")

    elif any(word in lower_text for word in
             ["hour", "hours", "open", "time", "timing"]):
        answered_count += 1
        print(
            f"{BOT}: Classes run 3 pm to 8 pm, Monday to Sunday. "
            "Any Question ︻デ═一"
        )

    elif any(word in lower_text for word in
             ["fee", "fees", "price", "cost", "how much"]):
        answered_count += 1
        print(
            f"{BOT}: Matric 100,000 PKR/month, "
            "FSc 150,000 PKR/month, "
            "O/A Level 250,000 PKR/month."
        )

    elif any(word in lower_text for word in
             ["subject", "class", "teaching subjects", "course"]):
        answered_count += 1
        print(
            f"{BOT}: We teach Thieving, Criminology, Cyber Theft, "
            "Shoplifting, Social engineering"
        )

    elif any(word in lower_text for word in
             ["where", "location", "address"]):
        answered_count += 1
        print(
            f"{BOT}: We are in Diaz Mension, near Gangster state."
        )

    elif any(word in lower_text for word in
             ["admission", "join", "enroll", "register"]):
        answered_count += 1
        print(
            f"{BOT}: Admissions are open. WhatsApp us on "
            "0326-0999091 to book a free demo class."
        )

    elif (
        lower_text in ["hi", "hello", "salam"]
        or lower_text.startswith("assalam o alaikum")
    ):
        answered_count += 1
        print(f"{BOT}: Han, {C_N}! What do you want now?")

    # ------------------------------------------------ AI CHAT FALLBACK

    else:
        messages.append({
            "role": "user",
            "content": customer_message,
        })

        messages = (
            [system_message]
            + messages[1:][-config["max_messages"]:]
        )

        start = time.perf_counter()
        response = precise.invoke(messages)
        total_seconds += time.perf_counter() - start

        messages.append({
            "role": "assistant",
            "content": response.content,
        })

        usage = response.usage_metadata or {}
        total_tokens += usage.get("total_tokens", 0)
        tokens_sent = usage.get("input_tokens", 0)

        print(f"{BOT}: {response.content}")
        print(
            f"     (Memory: {len(messages) - 1} messages, "
            f"{tokens_sent:,} input tokens)"
        )

        unanswered_count += 1
        chat_answers += 1

# ------------------------------------------------ SESSION REPORT

print("\n" + "=" * 48)
print("SESSION REPORT")
print(f"Total messages: {message_count}")
print(f"Answered by rules/commands: {answered_count}")
print(f"AI chat answers: {chat_answers}")
print(f"AI course descriptions: {menu_descriptions}")
print(f"Social media posts: {post_count}")
print(f"Price lookups: {price_answers}")
print(f"Unanswered / AI-routed questions: {unanswered_count}")
print(f"Complaints received: {complaint_count}")
print(f"AI tokens recorded: {total_tokens:,}")
print(f"AI time: {total_seconds:.2f} seconds")
print("=" * 48)
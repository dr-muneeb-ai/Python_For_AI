
"""
Bright Minds Tuition Center Front Desk
FAQs, fee estimates, admission support and AI-ready prompts.
"""

BOT_NAME = "Bright Minds Bot"
BUSINESS_NAME = "Bright Minds Tuition Center"

WHATSAPP = "0326-0999091"
OPENING_TIME = "3 pm to 8 pm, Monday to Sunday"
ADDRESS = "Diaz Mansion, near Gangster State"

CLOUD_PRICE_PER_1K = 0.1
LOCAL_MODEL_NAME = "llama3.2 (local, private)"
CLOUD_MODEL_NAME = "small cloud model (cheap)"

print("=" * 50)
print(f"  {BOT_NAME} - {BUSINESS_NAME}")
print("=" * 50)
print("Ask about fees, courses, timings, admissions or location.")
print("Type /quote for a fee estimate or bye to exit.")

def show_menu():
    print("\n" + "=" * 45)
    print("       BRIGHT MINDS TUITION CENTER")
    print("              HELP MENU")
    print("=" * 45)
    print("What would you like to know?")
    print()
    print("1. Greetings      - Type: hi, hello, salam")
    print("2. Courses        - Type: courses, subjects")
    print("3. Fees           - Type: fees, price, cost")
    print("4. Fee Estimate   - Type: /quote")
    print("5. Timings        - Type: time, timing, hours")
    print("6. Location       - Type: location, address")
    print("7. Admissions     - Type: admission, join, enroll")
    print("8. Teachers       - Type: teacher, tutor")
    print("9. Certificates   - Type: certificate, payment")
    print("10. Complaint     - Type: complaint, problem, refund")
    print("11. Human Support - Type: human, agent")
    print("12. Exit          - Type: bye, exit")
    print("=" * 45)
    print("Example: Type /quote to calculate course fees.")
    print("=" * 45)


C_N = input(f"{BOT_NAME}: What is your name? ").strip().title()

if C_N == "":
    C_N = "Friend"

M_C = 0
answered_count = 0
unanswered_count = 0
Q_C = 0
T_Q_V = 0.0
total_ai_cost = 0.0
complaint_count = 0

while True:
    show_menu()
    customer_message = input(f"{C_N}: ").strip().lower()
    M_C += 1

    if customer_message == "":
        print(f"{BOT_NAME}: Please enter a question.")

    elif customer_message == "bye" or customer_message == "exit":
        print(f"{BOT_NAME}: Goodbye, {C_N}!")
        break
    elif "agent" in customer_message or "human" in customer_message:
        answered_count += 1
        print(f"{BOT_NAME}: Please contact our team on WhatsApp: {WHATSAPP}.")
        break

    elif any(word in customer_message for word in
             ["complaint", "problem", "issue", "refund"]):
        complaint_count += 1
        answered_count += 1
        print(f"{BOT_NAME}: Sorry for the inconvenience.")
        print(f"     Our team will not help you. Get out")
    elif (customer_message in ["hi", "hello", "salam"]
          or customer_message.startswith("assalam o alaikum")):
        answered_count += 1
        print(f"{BOT_NAME}: Hello {C_N}! Welcome to {BUSINESS_NAME}.")
    elif any(word in customer_message for word in
             ["course", "courses", "subject", "subjects", "teach", "class"]):
        answered_count += 1
        print(f"{BOT_NAME}: We teach Criminology, and Theiving Basics")
        print("     Ask us about course fees or admissions.")
    elif any(word in customer_message for word in
             ["fee", "fees", "price", "cost", "how much"]):
        answered_count += 1
        print(f"{BOT_NAME}: Type /quote to estimate your course fee.")
        print("     Available courses: Criminology, Theiving Basics")
    elif any(word in customer_message for word in
             ["time", "timing", "hours", "open"]):
        answered_count += 1
        print(f"{BOT_NAME}: Our example timings are {OPENING_TIME}.")
    elif any(word in customer_message for word in
             ["location", "address", "where"]):
        answered_count += 1
        print(f"{BOT_NAME}: Our example address is {ADDRESS}.")
        print("     Please confirm the exact address before visiting.")
    elif any(word in customer_message for word in
             ["admission", "admissions", "enroll", "enrol",
              "register", "join"]):
        answered_count += 1
        print(f"{BOT_NAME}: Admissions are open!")
        print(f"     WhatsApp: {WHATSAPP}")
        print("     Contact us to book a free demo class.")
    elif "teacher" in customer_message or "tutor" in customer_message:
        answered_count += 1
        print(f"{BOT_NAME}: Contact our team for teacher availability.")
        print(f"     WhatsApp: {WHATSAPP}")
    elif "certificate" in customer_message or "payment" in customer_message:
        answered_count += 1
        print(f"{BOT_NAME}: Contact our team for certificate and payment policies.")
        print(f"     WhatsApp: {WHATSAPP}")
    elif customer_message == "/quote":
        course_name = input(
            f"{BOT_NAME}: Course (Killing / Mudering / Criminology)? "
        ).strip().lower()

        quantity_text = input(
            f"{BOT_NAME}: How many students? "
        ).strip()

        if not quantity_text.isdigit() or int(quantity_text) <= 0:
            print(f"{BOT_NAME}: Enter a valid whole number greater than zero.")

        else:
            student_count = int(quantity_text)

            if course_name == "killing":
                unit_price = 5000
            elif course_name == "mudering":
                unit_price = 8000
            elif course_name == "criminology":
                unit_price = 3000
            else:
                unit_price = 0
            if unit_price == 0:
                print(f"{BOT_NAME}: Sorry, that course is not available.")
                print("     Choose Killing, Mudering or Criminology.")

            else:
                subtotal = unit_price * student_count

                if student_count >= 10:
                    discount = subtotal * 0.10
                else:
                    discount = 0

                total_cost = subtotal - discount

                Q_C += 1
                answered_count += 1
                T_Q_V += total_cost

                print(f"{BOT_NAME}: Course: {course_name.title()}")
                print(f"     Students: {student_count}")
                print(f"     Subtotal: {subtotal:,.0f} PKR")
                print(f"     Group discount: -{discount:,.0f} PKR")
                print(f"     Estimated total: {total_cost:,.0f} PKR")
                print("     Final fees should be confirmed with the center.")
    else:
        unanswered_count += 1

        cleaned_question = customer_message.capitalize()[:150]
        estimated_tokens = round(len(cleaned_question) / 4)

        if any(word in customer_message for word in
               ["phone", "cnic", "my address"]):
            chosen_model = LOCAL_MODEL_NAME
            estimated_cost = 0.0
        else:
            chosen_model = CLOUD_MODEL_NAME
            estimated_cost = estimated_tokens / 1000 * CLOUD_PRICE_PER_1K

        ai_prompt = (
            f"You are a friendly assistant for {BUSINESS_NAME}. "
            f"Answer {C_N} in two short lines. "
            "Do not invent fees, policies or business details. "
            f"If you do not know the answer, suggest contacting {WHATSAPP}. "
            f"Customer question: {cleaned_question}"
        )

        total_ai_cost += estimated_cost

        print(f"{BOT_NAME}: I don't have a fixed answer yet.")
        print(f"     AI route: {chosen_model}")
        print(f"     Estimated AI cost: {estimated_cost:.4f} PKR")
        print(f"     AI prompt: {ai_prompt}")
        print("     Note: This code creates a prompt; it does not call an AI model.")

print("=" * 50)
print("SESSION REPORT")
print(f"Messages: {M_C}")
print(f"Answered by rules: {answered_count}")
print(f"Unanswered / AI-ready: {unanswered_count}")
print(f"Fee quotes: {Q_C}")
print(f"Total quoted value: {T_Q_V:,.0f} PKR")
print(f"Estimated AI cost: {total_ai_cost:.4f} PKR")
print(f"Complaints received: {complaint_count}")
print("=" * 50)

# Python for AI — Learning Project

**Course:** Python for AI  
**Module:** 1 — Python Basics for GenAI and Agentic AI  
**Student:** Muneeb  
**Project:** Python Fundamentals and Business Helper Bot

## About This Project

This repository contains my Python learning tasks and beginner-level AI projects. It focuses on Python fundamentals used in Generative AI and Agentic AI, including variables, data types, strings, user input, conditions, loops, and prompt engineering.

The final project is **Bright Minds Bot**, a rule-based chatbot for a tuition centre. It answers common questions about fees, timings, courses, location, admissions, and complaints. It also counts unanswered questions and generates a sample prompt for future AI integration.

## Technologies Used

- Python 3.14+
- uv — Python project and package management
- Git and GitHub — version control
- LangChain and Ollama — tools for learning AI model integration

## Project Structure

```text
python-ai/
├── code/
│   ├── lesson_01_intro.py
│   ├── lesson_04_print_input.py
│   ├── lesson_05_variables.py
│   ├── lesson_05_variable.py
│   ├── lesson_06_strings_prompts.py
│   ├── lesson_07_conditions.py
│   ├── lesson_08_mini_chatbot.py
│   └── lesson_2_1_first_ai_call.py
├── docs/
├── notebook/
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Learning Tasks

### Task 1.1 — Python Introduction
- Variables and strings
- Displaying information with `print()`
- Basic f-strings

### Task 1.4 — Business Problem Prompt
- Collecting user input
- Using variables to describe a business problem
- Creating a prompt for possible AI solutions

### Task 1.5 — AI Model Profile Card
- Python data types: `str`, `int`, `float`, and `bool`
- Displaying values with f-strings
- Converting input using `int()`
- Estimating chat and monthly costs

### Task 1.6 — Prompt Cleaner
- Cleaning user input with `.strip()`
- Formatting names with `.title()`
- Working with `.lower()`, `.capitalize()`, and `.replace()`
- Measuring characters and estimating tokens
- Creating a multi-line AI prompt

### Task 1.7 — Smart Model Router
- Using `if`, `elif`, and `else`
- Selecting models according to task type
- Estimating costs
- Applying token limits and paid-user conditions

### Task 1.8 — Business Helper Bot
- Creating a menu-driven chatbot
- Using functions, loops, and conditional statements
- Handling greetings and common questions
- Counting unanswered questions and complaints
- Providing a human-handover message
- Preparing prompts for future AI integration

## Bright Minds Tuition Centre — Chatbot Design

The chatbot uses predefined rules to recognize common user questions.

| Intent | Example keywords | Response |
|---|---|---|
| Greeting | `hi`, `hello`, `salam` | Greets the user by name |
| Fees | `fee`, `fees`, `price`, `cost` | Displays example course fees |
| Timings | `time`, `timing`, `hours`, `open` | Provides class timings |
| Courses | `course`, `subject`, `class` | Provides information about subjects |
| Location | `where`, `location`, `address` | Provides location information |
| Admission | `admission`, `enroll`, `register` | Explains how to inquire about admission |
| Complaint | `refund`, `complaint`, `problem`, `issue` | Provides a complaint response |
| Human help | `human`, `agent` | Displays a human-handover message |
| Unknown question | Unrecognized keywords | Generates a sample AI prompt |
| Exit | `bye`, `exit` | Ends the conversation and prints a summary |

*Note: Fees, contact details, location, timings, and courses in the chatbot are demonstration data. Verify and replace them with the actual tuition centre's information before real-world use.*

## How to Run the Project

### 1. Install prerequisites

Install Python and [uv](https://docs.astral.sh/uv/).

### 2. Open the project directory

```bash
cd python-ai
```

### 3. Run individual tasks

**Task 1.5**

```bash
uv run code/lesson_05_variables.py
```

**Task 1.6**

```bash
uv run code/lesson_06_strings_prompts.py
```

**Task 1.7**

```bash
uv run code/lesson_07_conditions.py
```

**Task 1.8 — Bright Minds Bot**

```bash
uv run code/lesson_08_mini_chatbot.py
```

Run each program separately and follow its input prompts.

## Example Chatbot Interaction

```text
Bright Minds Bot: Hi! How can I help you today? Type 'bye' to exit.
Bright Minds Bot: What is your name? Muneeb
Bright Minds Bot: Nice to meet you, Muneeb!

Muneeb: hi
Bright Minds Bot: Han, Muneeb! What do you want now?

Muneeb: bye
Bright Minds Bot: Goodbye, Muneeb!

========================================
Chat summary: 2 messages, 0 unanswered, 0 complaints.
========================================
```

*This is an illustrative example; actual output depends on the code and user input.*

## What I Learned

- How to use Python variables and built-in data types.
- How to collect, clean, and process user input.
- How to use built-in functions such as `print()`, `input()`, `len()`, `type()`, and `round()`.
- How string methods such as `.strip()`, `.lower()`, and `.title()` work.
- How to control program flow with conditions and loops.
- How to create a simple rule-based chatbot.
- How to track unanswered questions and prepare prompts for future AI applications.
- How to organize code and manage changes using Git and GitHub.

## Future Improvements

- Connect the chatbot to a real language model using LangChain.
- Store frequently asked questions in a separate data file.
- Improve keyword matching and error handling.
- Add appointment or admission inquiry management.
- Replace demonstration data with verified business information.
- Add automated tests for common and unexpected inputs.

## Important Note

This is an educational project intended to demonstrate Python fundamentals and the basic structure of a business chatbot. The current Bright Minds Bot uses predefined rules; it does not generate real AI responses or connect to a live business system.

## Author

**Kira**  
Python for AI — Conceptual Project
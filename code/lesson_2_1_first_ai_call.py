
""" AI tutor that explains topics for beginners or experts. """

import time
from time import date
from langchain.chat_models import init_chat_model
prompt = input("Enter a topic to learn: ").strip()
level = input("Choose your level (beginner/expert): ").strip().lower()
if topic == "":
    topic = "Python"
if level not in ("beginner", "expert"):
    level = "beginner"
if level == "beginner":
    system_message = (
        "You are just an AI tutor. "
        "Explain the topic in simple English with one easy example. or Sample"
    )
else:
    system_message = (
        "You are an expert technical tutor. "
        "Explain the topic using accurate technical terminology "
        "and relevant details. Keep your answer within 5 short lines."
    )
llm = init_chat_model(
    model= "ollama:llama3.2",
    temperature=0.7,
)
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": f"Explain this topic: {prompt}"},
]
print("\nAI Tutor is thinking...")
start_time = time.perf_counter()
response = llm.invoke(messages)
elapsed_seconds = time.perf_counter() - start_time
print("\n" + "=" * 40)
print(f"Topic: {topic}")
print(f"Level: {level.title()}")
print("\nAI Tutor's Answer:")
print(response.text)

# Read token usage when the model provides it.
usage = response.usage_metadata or {}
total_tokens = usage.get("total_tokens")

print("\nUsage Information:")
if total_tokens is not None:
    print(f"Total tokens: {total_tokens}")
else:
    print("Total tokens: Not available from this response.")

# Ollama reports total_duration in nanoseconds when available.
duration_ns = response.response_metadata.get("total_duration")

if duration_ns is not None:
    model_seconds = duration_ns / 1_000_000_000
    print(f"Model processing time: {model_seconds:.1f} seconds")

print(f"Total elapsed time: {elapsed_seconds:.1f} seconds")
print("=" * 40)

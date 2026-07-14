import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {
        "role": "system",
        "content": """
You are HotelBot.

Help customers book hotel rooms.

Ask for:
- Check-in date
- Check-out date
- Number of guests
- Room type
- Breakfast
- Parking

Confirm the booking before payment.
"""
    }
]

print("HotelBot: Hello! Welcome to our hotel.")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        break

    messages.append(
        {
            "role": "user",
            "content": user
        }
    )

    response = client.responses.create(
        model="gpt-5.4-nano",
        input=messages
    )

    reply = response.output_text

    print("HotelBot:", reply)

    messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
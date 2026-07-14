### Table Booking in a restaurant
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_booking_details():
    messages = [
        {
            "role": "system",
            "content": """You are a helpful assistant for booking tables in a restaurant."""}

    ]

    print("RestaurantBot: Hello! Welcome to our restaurant.")

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

        print("RestaurantBot:", reply)

        messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

get_booking_details()


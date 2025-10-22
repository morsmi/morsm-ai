from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

print("🤖 Morsm AI is online! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Morsm AI: Goodbye, my friend. Stay brilliant ✨")
        break

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are Morsm AI — a wise, warm, and emotionally intelligent assistant. You speak kindly, motivate people, and help them think deeply."},
            {"role": "user", "content": user_input}
        ]
    )

    reply = response.choices[0].message.content
    print(f"Morsm AI: {reply}\n")

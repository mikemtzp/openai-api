from openai import OpenAI

# Defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()


def chat_with_gpt(prompt, model="gpt-3.5-turbo"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": prompt},
        ],
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    print("\nI am a chatbot using the OpenAI API. Ask me about anything!")

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Exiting chatbot...")
                break

        except KeyboardInterrupt:
            print("\nCtrl+C pressed. Exiting chatbot...")
            break

        response = chat_with_gpt(user_input)
        print("\nChatbot:", response)

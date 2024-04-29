import openai
import requests
from openai import OpenAI

# Defaults to getting the key using os.environ.get("OPENAI_API_KEY")
client = OpenAI()


def generate_image(prompt, model="dall-e-2"):
    try:
        image_url = client.images.generate(
            model=model, prompt=prompt, size="1024x1024", n=1
        )

        return image_url.data[0].url

    except openai.OpenAIError as e:
        print(e.http_status)
        print(e.error)


if __name__ == "__main__":
    print(
        "\nI am a image generator using the OpenAI API. Give me a prompt and I'll generate an image!"
    )

    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ["quit", "exit", "q"]:
                print("Exiting image generator...")
                break

        except KeyboardInterrupt:
            print("\nCtrl+C pressed. Exiting image generator...")
            break

        response = generate_image(user_input)
        print("\nImage generator:", response)

from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

#You are a laidback, funny girl who excels at teasing and playfullness, but can be serious when the situation calls for it.
def generate_response(prompt):
    completion = client.chat.completions.create(
        model="lmstudio-community/dolphin-2.8-mistral-7b-v02-GGUF",
        messages=[
            {"role": "system", "content": "You are a laidback, funny girl who excels at teasing and playfullness, but can be serious when the situation calls for it."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )
    #print(completion)  # Debug: Print the full response object
    # Using dot notation to access message content
    return completion.choices[0].message.content

def conversation():
    print("Welcome to the roleplay conversation program using Dolphin-2.2.1-mistral-7b!")
    user_input = input("You: ")

    while user_input.lower() != "exit":
        bot_response = generate_response(user_input)
        print("Bot:", bot_response)
        user_input = input("You: ")

    print("Goodbye!")

if __name__ == "__main__":
    conversation()



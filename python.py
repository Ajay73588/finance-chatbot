import openai

# Set your API key
openai.api_key = "your-api-key-here"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# Example usage
user_input = input("You: ")
while user_input.lower() not in ['quit', 'exit']:
    response = chat_with_gpt(user_input)
    print("Bot:", response)
    user_input = input("You: ")

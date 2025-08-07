import openai
import os

# OpenAI API anahtarını ortam değişkeninden al
openai.api_key = os.getenv("OPENAI_API_KEY")

def simple_ai_agent():
    print("🤖 Basit AI Agent'e hoş geldin! Çıkmak için 'exit' yaz.")
    
    while True:
        user_input = input("🧑‍💻 Sen: ")
        
        if user_input.lower() in ["exit", "quit", "çık"]:
            print("👋 Görüşmek üzere!")
            break

        response = openai.ChatCompletion.create(
            model="gpt-4",  # veya "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "Sen yardımcı bir yapay zeka agentsın."},
                {"role": "user", "content": user_input}
            ]
        )

        reply = response["choices"][0]["message"]["content"]
        print(f"🤖 Agent: {reply}\n")

if __name__ == "__main__":
    simple_ai_agent()
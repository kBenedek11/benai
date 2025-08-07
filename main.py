import os
from dotenv import load_dotenv
from google import genai



def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    respond = client.models.generate_content(model="gemini-2.0-flash-001", 
                                   contents = 
                                   "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    print(respond.text)
    print(f"Prompt tokens: {respond.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {respond.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()

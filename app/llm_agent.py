import openai
from config.config import Config
import time
openai.api_key = Config.OPENAI_API_KEY

def parse_search_results(results, prompt):
    content = " ".join(result["snippet"] for result in results.get("organic_results", []))
    while True:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo-instruct",  # Or "gpt-3.5-turbo" depending on your subscription
                messages=[
                    {"role": "system", "content": "You are an assistant that processes web search results."},
                    {"role": "user", "content": f"{prompt}\n\n{content}"}
                ]
            )
            return response["choices"][0]["message"]["content"]
        except openai.error.RateLimitError:
            print("Rate limit hit. Waiting 60 seconds before retrying...")
            time.sleep(60)
        except openai.error.OpenAIError as e:
            print(f"OpenAI error occurred: {e}")
            break

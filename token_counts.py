from openai import OpenAI
from mistralai import Mistral
from anthropic import Anthropic
import os
import json
import polars as pl
import time
from pathlib import Path

if __name__ == "__main__":
    MAX = 30
    key = os.environ.get("OPENAI_KEY2")
    query = "Who is the USA 40th president?"

    results = pl.DataFrame(None, schema={"runID": pl.Int64, "model": pl.String, "tokens": pl.Int64})

    # OpenAI run
    models = ["gpt-3.5-turbo", "o3", "gpt-5", "gpt-5-chat-latest"]

    for i in range(MAX):
        for model in models:
            openai = OpenAI(api_key=key)
            chat_response = openai.responses.create(
                    model= model,
                    input= query
            )

            print(chat_response.output_text)
            output_token_count = json.loads(chat_response.model_dump_json())["usage"]["output_tokens"]
            print(f"Output token count for mode {model}: {output_token_count}")

            df = pl.DataFrame({"runID": i, "model": model, "tokens": output_token_count})
            results = pl.concat([results, df])

    # Anthropic run
    key = os.environ.get("ANTHROPIC_KEY2")
    models = ["claude-3-haiku-20240307", "claude-3-7-sonnet-20250219", "claude-sonnet-4-20250514"]

    for i in range(MAX):
        for model in models:
            claude = Anthropic(api_key=key)
            chat_response = claude.messages.create(
                model=model,
                max_tokens=1024,
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    }
                ]
            )

            print(chat_response.content)
            output_token_count = json.loads(chat_response.model_dump_json())["usage"]["output_tokens"]
            print(f"Output token count for mode {model}: {output_token_count}")

            df = pl.DataFrame({"runID": i+30, "model": model, "tokens": output_token_count})
            results = pl.concat([results, df])

    # Mistral run
    key = os.environ.get("MISTRAL_API_KEY1")
    models = ["magistral-medium-2507", "mistral-medium-2505"]

    for i in range(MAX):
        for model in models:
            mistral = Mistral(api_key=key)
            chat_response = mistral.chat.complete(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": query,
                    }
                ]
            )

            print(chat_response.choices[0].message.content)
            output_token_count = json.loads(chat_response.model_dump_json())["usage"]["completion_tokens"]
            print(f"Output token count for mode {model}: {output_token_count}")

            df = pl.DataFrame({"runID": i+60, "model": model, "tokens": output_token_count})
            results = pl.concat([results, df])

    FILE = Path("./test_results.csv")
    results.write_csv(FILE, separator=";")
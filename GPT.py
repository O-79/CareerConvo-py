import os
from openai import OpenAI

class GPT:
    @staticmethod
    def GET_ANS(MSG):
        OpenAI.api_key = os.getenv('OPENAI_API_KEY')
        _model = "gpt-3.5-turbo"
        client = OpenAI()

        completion = client.chat.completions.create(
            model = _model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Your response should be in JSON format."},
                {"role": "user", "content": MSG}
            ],
            response_format={"type": "json_object"}
        )

        print(completion.choices[0].message.content)

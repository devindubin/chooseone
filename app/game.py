import os
# from groq import Groq
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
from openai import OpenAI

client=OpenAI()


from flask import Blueprint, request

bp = Blueprint("game",__name__,"/game")

@bp.route("/")
def play_game():
    data = request.args.get("data")


    # chat_completion = client.chat.completions.create(
    #     messages=[
    #         {
    #             "role":"user",
    #             "content": f"Provide a bulleted list of 4 random examples of the following meal type {data}. Do not repeat the prompt or provide any text other than the four examples."
    #         }
    #     ],
    #     model="gemma2-9b-it"
    # )

    completion = client.chat.completions.create(model='gpt-4o-mini',
                                         messages=[
                                             {"role":"system","content":"You are a list generator."},
                                             {"role":"user","content":f"List 4 random examples of the following meal category: {data}"}
                                         ])







    print(data)
    print("test")
    
    return completion.choices[0].message.content
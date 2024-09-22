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



    completion = client.chat.completions.create(model='gpt-4o-mini',
                                         messages=[
                                             {"role":"system","content":"You are a list generator."},
                                             {"role":"user","content":f"List 4 random examples of the following meal category: {data}. Provide output at as comma seperated list."}
                                         ])



    
    return completion.choices[0].message.content

#TODO: AI Generative images
def generate_images():
    """Requests AI image generation for listed dishes"""
    pass

#TODO: AI search for images
def search_images():
    """Requests AI to websearch for images of listed dishes"""
    pass


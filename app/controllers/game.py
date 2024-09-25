import os
# from groq import Groq
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
from openai import OpenAI

client=OpenAI()


def generate_game():
    #TODO: Call generate_food
    
    return 




def generate_food(data):
    #TODO: add parameter for choice of search or generation of image

    #TODO: Fine tune AI call to only return itemized list of foods

    completion = client.chat.completions.create(model='gpt-4o-mini',
                                         messages=[
                                             {"role":"system","content":"You are a list generator."},
                                             {"role":"user","content":f"List 4 random examples of the following meal category: {data}. Provide output at as comma seperated list."}
                                         ])


    #TODO: pass list to image generator or image search engine
    print(completion.choices[0].message.content)
    return 

#TODO: AI Generative images
def generate_images(food_list: list) -> dict:
    """Requests AI image generation for listed dishes"""

    food_output = {}

    for item in food_list:
        resp = client.images.generate(
            model="dall-e-3",
            prompt=item,
            n=1,
            size="1024x1024"
        )
        food_output[item] = resp


    return food_output
    

#TODO: AI search for images
def search_images():
    """Requests AI to websearch for images of listed dishes"""
    pass


import openai
import re
from openai import OpenAI
from drone import *
from djitellopy import enforce_types
from djitellopy.tello import *
import argparse
#from airsim_wrapper import *
import math
import numpy as np
import os
import json
import time
from openai import AsyncOpenAI
from openai import OpenAI
import pygame #Real-time speech
import pyaudio
import speech_recognition as sr

#UPDATED
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("YOUR_OPENAI_API_KEY"),
)



parser = argparse.ArgumentParser()
parser.add_argument("--prompt", type=str, default="instruction.txt")
parser.add_argument("--sysprompt", type=str, default="general_instruction.txt")
args = parser.parse_args()


print("Initializing ChatGPT...")



with open(args.sysprompt, "r") as f:
    sysprompt = f.read()

chat_history = [
    {
        "role": "system",
        "content": sysprompt
    },
    {
        "role": "user",
        "content": "move 10 units up"
    },
    {
        "role": "assistant",
        "content": """```python
tello.move_up([aw.get_drone_position()[0], aw.get_drone_position()[1], aw.get_drone_position()[2]+10])
```

This code uses the `fly_to()` function to move the drone to a new position that is 10 units up from the current position. It does this by getting the current position of the drone using `get_drone_position()` and then creating a new list with the same X and Y coordinates, but with the Z coordinate increased by 10. The drone will then fly to this new position using `fly_to()`."""
    }
]


def ask(prompt):
    chat_history.append(
        {
            "role": "user",
            "content": prompt,
        }
    )
   
    
    completion = openai.chat.completions.create(
    model="gpt-4",
    messages=chat_history,
    temperature=0
   
    )
   

    chat_history.append(
        {
            "role": "assistant",
            "content": completion.choices[0].message.content,
        }
    )
    return chat_history[-1]["content"]


print(f"Done.")

code_block_regex = re.compile(r"```(.*?)```", re.DOTALL)


def extract_python_code(content):
    code_blocks = code_block_regex.findall(content)
    if code_blocks:
        full_code = "\n".join(code_blocks)

        if full_code.startswith("python"):
            full_code = full_code[7:]

        return full_code
    else:
        return None


class colors:  # You may need to change color settings
    RED = "\033[31m"
    ENDC = "\033[m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"


print(f"Initializing Drone...")
#tello=Tello()  #PLEASE NEVER UNCOMMENT THIS
main()
#print(f"Done.")

with open(args.prompt, "r") as f:
    prompt = f.read()

ask(prompt)
print("Welcome to the Samis chatbot! I am ready to help you with your Samis Drone questions and commands for inspection purposes.")

'''
while True:
    question = input(colors.YELLOW + "SAMISgpt> " + colors.ENDC)

    if question == "!quit" or question == "!exit":
        break

    if question == "!clear":
        os.system("cls")
        continue

''' 
def record_audio():
    # Initialize the recognizer and microphone
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    # Record audio from the microphone
    with mic as source:
        print("Recording... Please SAMIS want to hear you speak.")
        audio = recognizer.listen(source)

        return audio

def speech_to_text(audio):
    try:
        recognizer = sr.Recognizer()
        # Recognize speech using Google Web Speech API
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Web Speech API could not understand the audio"
    except sr.RequestError:
        return "Could not request results from Google Web Speech API"

def process_with_openai(text):

    response_from_human = client.completions.create(
    #model="gpt-4",
    model="text-davinci-003",
    prompt=text,
        )
    return response_from_human.choices[0].text.strip()

# Main flow
audio = record_audio()
text = speech_to_text(audio)
print("Recognized text:", text)

# Process with OpenAI (uncomment the line below to enable)
processed_text = process_with_openai(text)
print(processed_text)
question = processed_text
response = ask(question)
 
response_from_samisbot = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=response,
    )

response_from_samisbot.stream_to_file("output.mp3")
print(f"\n{response}\n")
    

def play_audio(file_path):
    # Initialize pygame mixer
    pygame.mixer.init()

    # Load the audio file
    pygame.mixer.music.load(file_path)

    # Play the audio
    pygame.mixer.music.play()

    # Keep the script running until the audio finishes
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # You can adjust the tick rate as needed


play_audio('output.mp3')  # audio file

code = extract_python_code(response)
if code is not None:
    print("Please wait while I run the code...")
    exec(extract_python_code(response))
    print("Done!\n")




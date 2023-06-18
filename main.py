import os
import time
import sounddevice as sd
from gtts import gTTS
import openai
import speech_recognition as sr


api_key = "sk-*****************"

lang = 'en'

openai.api_key = api_key

person = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            audio = r.listen(source)
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global person
                person = said

                if "Friday" in said:

                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "user", "content": said}])
                    print("do you hear it ")
                    text = completion.choices[0].messages.content
                    print(text)
                    #speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    #speech.save("welcome1.wav")

                    # Play the audio using sounddevice




            except Exception:
                print("Exception")

        return said


    if "stop" in person:
        break

    get_audio()

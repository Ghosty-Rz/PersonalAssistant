import openai
import pyttsx3
import speech_recognition as sr
import time

# set the api key

openai.api_key = "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"

engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
       return recognizer.recognize_google(audio)
    except:
        print("skipping unknown error")

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt = prompt,
        max_tokens= 4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main ():
    while True:
        # wait for the user to say "moon"
        print("say 'Moon' to start the program")
        with sr.Microphone(device_index=1) as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower() == "moon":
                    # start recording audio
                    filename = "input.wav"
                    print("What is your question ...")
                    with sr.Microphone(device_index=1) as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    # transcribe audio to text
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print (f"you said: {text}")

                        # Generate the response using ChatGPT
                        response = generate_response(text)
                        print(f"=> {response}")

                        # read the response
                        speak_text(response)

            except Exception as e:
                print("An error has occurred: {}".format(e))



if __name__ == "__main__":
    main()
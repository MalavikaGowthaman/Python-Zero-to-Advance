import speech_recognition as sr
import pyttsx3
import logging
import os
import datetime
import webbrowser
import requests
import google.generativeai as genai  # Import the Gemini API client
import random
import wikipedia
import webbrowser
import requests
import google.generativeai as genai  # Import the Gemini API client
import random
import pygame  # Import pygame for music playback
from pytube import YouTube
import pygame
import time
import threading
import subprocess

# Logger for the application
LOG_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOG_DIR, exist_ok=True)
log_path = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Initialize text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # Female voice
stop_event = threading.Event()  # Event to stop speech

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def take_command():
    """Listen for user commands and recognize speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"You said: {query}\n")
    except Exception as e:
        logging.info(e)
        # print("Could you please repeat that?")
        return "Sorry, I didn't understand."
    return query

def wish_me():
    """Wish the user based on the current time."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        speak("Good Morning Malu!")
    elif hour < 18:
        speak("Good Afternoon Malu!")
    else:
        speak("Good Evening Malu!")
    
    speak("I am Zara. How can I assist you today?")

def gemini_response(query):
    """Get a response from the Gemini API. Answer should be in a short, crispy and easy way"""
    genai.configure(api_key="xx")  # Replace with your actual Gemini API key
    model = genai.GenerativeModel('gemini-pro')  # Adjust if needed
    response = model.generate_content(query)
    return response.text[:1000]

def remind_drink_water():
    """Remind the user to drink water every 30 minutes."""
    while True:
        time.sleep(1800)  # Wait for 30 minutes
        speak("Hey Malu Its a Time to drink water! Stay hydrated.")

def remind_walk():
    """Remind the user to walk every hour."""
    while True:
        time.sleep(3600)  # Wait for 1 hour
        speak("Hey Malu, Its a Time to take a 5-minute walk! Let's stay active.")

def wake_up_reminder():
    """Wake up reminder at 7 AM."""
    while True:
        current_time = datetime.datetime.now()
        if current_time.hour == 7 and current_time.minute == 0:
            speak("Good morning! It's 7 AM. Time to wake up!")
            time.sleep(60)  # Wait a minute to avoid multiple alerts
        time.sleep(30)  # Check every 30 seconds
        

# Start reminder threads
threading.Thread(target=remind_drink_water, daemon=True).start()
threading.Thread(target=remind_walk, daemon=True).start()
threading.Thread(target=wake_up_reminder, daemon=True).start()

def stop_speaking():
    """Stop the text-to-speech engine."""
    stop_event.set()  # Set the event to signal stopping
    engine.stop()  # Stop the speech immediately
        
wish_me()
while True:
    
    query = take_command().lower()
    print(query)
    
    if "stop" in query:
        stop_speaking()
        continue  # Move to the next command

    elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Time is {strTime}")

    elif "name" in query:
        speak("My name is Zara")
        
    elif "how are you" in query or "how about you" in query:
        speak("I'm good. Thanks for asking. How about you?")
        
    elif "i'm good" in query or "i'm fine" in query:
        speak("Thats good to hear, How can I help you?")
        
    elif "I am not Good" in query or "i am not fine" in query:
        speak("Oh ho Everything will be alright soon. How can I help you today?")
        
    elif 'who are you' in query or 'what can you do' in query:
        speak('I am Malu personal assistant. I am programmed to minor tasks like'
            'opening youtube,google chrome, gmail,greet,reminder,predict time, take a photo,search wikipedia,predict weather')


    elif "who made you" in query or "who created you" in query or "who discovered you" in query:
        speak("I was built by Malavika Gowthaman")
        print("I was built by Malavika Gowthaman")

    elif "bye" in query:
        speak("Okay, bye! See you soon. Have a nice day!")
        break  # Exit the loop

    elif "google" in query:
        search_term = query.replace("google", "")
        speak(f"Searching Google for {search_term}")
        search_url = f"https://www.google.com/search?q={search_term}"
        webbrowser.open(search_url)

    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia:")
        print(results)
        speak(results)

    elif "joke" in query:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the bicycle fall over? Because it was two-tired!",
            "What do you call fake spaghetti? An impasta!"
        ]
        joke = random.choice(jokes)
        speak(joke)

    elif "calculate" in query:
        query = query.replace("calculate", "").strip()
        try:
            answer = eval(query)  # Note: eval can be dangerous if used with untrusted input
            speak(f"The answer is {answer}.")
        except Exception as e:
            speak("I couldn't perform the calculation. Please try again.")
            
    elif "log off" in query or "sign out" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])        
    
    else:  # Any other question will be sent to the Gemini API
        speak(f"Let me check that for you: {query}")
        response = gemini_response(query)
        print(response)
        speak(response)

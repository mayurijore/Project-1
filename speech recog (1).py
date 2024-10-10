
import pyttsx3
# import engineio #engineio module is not needed.

engineio = pyttsx3.init()
voices = engineio.getProperty('voices')
engineio.setProperty('rate', 130)    # Aquí puedes seleccionar la velocidad de la voz
engineio.setProperty('voice',voices[3].id)

def speak(text):
    engineio.say(text)
    engineio.runAndWait()

speak("Welcom to matoshree college of engineering and research center nashik please ask any Query")

import sqlite3
import speech_recognition as sr
try:
    from .recognizers import google, whisper
except (ModuleNotFoundError, ImportError):
    pass
else:
    Recognizer.recognize_google = google.recognize_legacy
    Recognizer.recognize_whisper_api = whisper.recognize_whisper_api
def create_and_populate_database():
    # Create the database
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()

    # Create the questions table if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                 question TEXT, 
                 answer TEXT)''')

    # Commit changes
    conn.commit()

    # Insert example questions and answers into the table
    questions_and_answers = [
        (" What is name of principal?", "Doctor G k kharate"),
        (" departments in college?", "AI ,ENTC , MECHANICAL , COMPUTER,CIVIL"),
        ("how many faculties in college?", "20"),
        ("location of ai hod cabin?", "ground floor"),
        ("location of principal cabin cabin?", "ground floor"),
        ("location of students and accounts section?", "first floor"),
        ("what is time of college?", "8am to 5 pm"),
        ("technology resources available in campus", "lab and ai room"),
        ("how is internship placement process", "80 percent"),
        ("where is library", "yes second floor"),
        ("what events happening in college campus ", "cultural , sports"),
        ("where is first aid room", "third floor"),
        ("where is canteen", "third floor"),
        ("what type of placement opportunities", "it industry"),
        ("are there company job fair", "yes"),
        ("companies for campus selection", "tata, cognizant, infosys"),
        ("which type of program facilitates students visit to industries", "site visits"),

        
        # Add more questions and answers here
    ]

    # Insert questions and answers into the table
    for question, answer in questions_and_answers:
        c.execute("INSERT INTO questions (question, answer) VALUES (?, ?)", (question, answer))

    # Commit changes and close connection
    conn.commit()
    conn.close()

def listen_and_recognize():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("Please ask a question:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

def search_question_in_database(question):
    conn = sqlite3.connect('questions.db')
    c = conn.cursor()

    c.execute("SELECT answer FROM questions WHERE question LIKE ?", ('%' + question + '%',))
    result = c.fetchone()

    # Close connection
    conn.close()

    if result:
        return result[0]
    else:
        return None  # Return None if no answer found

if __name__ == "__main__":
    create_and_populate_database()

    while True:
        # Listen for the question
        question = listen_and_recognize()

        if question:
            print("You asked:", question)

            # Search for the question in the database
            answer = search_question_in_database(question)
            if answer:
                print("Answer:", answer)
                speak(answer)
            else:
                print("Sorry, I don't have an answer to that question.")
#                 text_to_speech("Sorry, I don't have an answer to that question.")
# 
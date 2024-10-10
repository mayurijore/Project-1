from gtts import gTTS
from pygame import mixer #to play the audio
text="Hello, I am your friendly assistant robot. I'm here to make your life easier and more convenient. Whether you need help with tasks, information, or just a chat, I'm at your service. How can I assist you today?"
tts = gTTS(text=text, lang="en")
tts.save("temp.mp3") # save the audio in a temp file
mixer.init(44100, -16,2,2048)  #freq 
mixer.music.load('temp.mp3')# load the audio file
mixer.music.play()



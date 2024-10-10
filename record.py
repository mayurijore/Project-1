import pyaudio
import wave

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Audio format (16-bit PCM)
CHANNELS = 1  # Mono audio
RATE = 44100  # Sample rate (samples per second)
RECORD_SECONDS = 5  # Duration of the recording
OUTPUT_FILENAME = "output.wav"  # Name of the output audio file

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Create an audio stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=1024)

print("Recording...")

frames = []

# Record audio
for _ in range(0, int(RATE / 1024 * RECORD_SECONDS)):
    data = stream.read(1024)
    frames.append(data)

print("Recording finished.")

# Close the audio stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded audio to a WAV file
with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print("Audio saved as", OUTPUT_FILENAME)

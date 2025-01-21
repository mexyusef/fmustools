"""
https://www.thepythoncode.com/article/using-speech-recognition-to-convert-speech-to-text-python
"""

# if not global_context['clock_reminder']:
#     return
# denger('c:/windows/media/tada.wav')
# speak(f'Thirty minutes has passed since {angka(jam())}. Please stand up and count to thirty.')
# denger()

from .audioutils import speak, angka, denger

import soundfile as sf
import sounddevice as sd
import speech_recognition as sr
import time
import keyboard
import tempfile
import os



def record_audio_timed(how_long=10, print_callback=print):
	elapsed_seconds = 0

	def print_elapsed_seconds():
		nonlocal elapsed_seconds
		elapsed_seconds += 1
		print_callback(str(elapsed_seconds) + '..')
		if elapsed_seconds >= how_long:
			sd.stop()

	print_callback(f"Recording started. Speak now for {how_long} secs...\n")
	sd.default.samplerate = 44100
	sd.default.channels = 1
	sd.default.dtype = "int16"

	start_time = time.time()
	recording = sd.rec(int(how_long * sd.default.samplerate))
	while time.time() - start_time < how_long:
		print_elapsed_seconds()
		time.sleep(1)
	sd.stop()

	audio_data = recording.flatten()
	sample_rate = sd.default.samplerate

	recognizer = sr.Recognizer()
	audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

	try:
		print_callback("Processing audio...\n")
		text = recognizer.recognize_google(audio)
		print_callback(f"Recognized text:\n{text}")
		return text
	except sr.UnknownValueError:
		print_callback("Unable to recognize speech.\n")
		return ""
	except sr.RequestError as e:
		print_callback(f"Speech recognition request error: {e}\n")
		return ""
	except Exception as e:
		print_callback(f"Speech recognition exception: {e}\n")
		return ""


def record_audio_timed_threaded(how_long=10, print_callback=print):
	from .threadutils import mulai
	kwargs = {
		'how_long': how_long,
		'print_callback': print_callback,
	}
	mulai(record_audio_timed, kwargs=kwargs)


def timed_recording():
	text = record_audio_timed(how_long=10)
	print("Final recognized text:", text)

def record_audio():
	sample_rate = 44100
	duration = 10  # Set the initial duration (in seconds) for recording

	# Record audio using sounddevice
	audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=2, dtype='int16')
	sd.wait()

	return audio_data, sample_rate

def recognize_speech_error_audiofile_is_data(audio_data, sample_rate):
	recognizer = sr.Recognizer()
	audio_data = audio_data.flatten()

	# Convert audio data to text using speech_recognition
	with sr.AudioFile(audio_data) as source:
		audio = recognizer.record(source)

	try:
		text = recognizer.recognize_google(audio)
		print("Recognized text:", text)
	except sr.UnknownValueError:
		print("Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))


def recognize_speech_no_sd_write(audio_data, sample_rate):
	recognizer = sr.Recognizer()
	audio_data = audio_data.flatten()

	# Save the audio data to a temporary WAV file
	temp_filename = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
	sd.write(temp_filename, audio_data, sample_rate)

	try:
		# Convert audio file to text using speech_recognition
		with sr.AudioFile(temp_filename) as source:
			audio = recognizer.record(source)

		text = recognizer.recognize_google(audio)
		print("Recognized text:", text)
	except sr.UnknownValueError:
		print("Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
	finally:
		# Clean up: Delete the temporary file
		os.remove(temp_filename)

import wavio

def recognize_speech_gagal(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    audio_data = audio_data.flatten()

    # Save the audio data to a temporary WAV file
    temp_filename = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    wavio.write(temp_filename, audio_data, sample_rate, sampwidth=3)

    try:
        # Convert audio file to text using speech_recognition
        with sr.AudioFile(temp_filename) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        # Clean up: Delete the temporary file
        os.remove(temp_filename)

def recognize_speech(audio_data, sample_rate):
    recognizer = sr.Recognizer()
    audio_data = audio_data.flatten()

    # Save the audio data to a temporary WAV file
    temp_filename = tempfile.NamedTemporaryFile(delete=False, suffix=".wav").name
    wavio.write(temp_filename, audio_data, sample_rate, sampwidth=3)

    try:
        # Convert audio file to text using speech_recognition
        with sr.AudioFile(temp_filename) as source:
            audio = recognizer.record(source)

        # Specify the language (e.g., 'en-US' for US English)
        text = recognizer.recognize_google(audio, language='en-US')
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    finally:
        # Clean up: Delete the temporary file
        os.remove(temp_filename)

def main_interrupt():
	print("Press 'Ctrl + C' to stop recording and recognize speech.")
	
	try:
		while True:
			audio_data, sample_rate = record_audio()
			recognize_speech(audio_data, sample_rate)
	except KeyboardInterrupt:
		print("Recording stopped.")

def main_keyboard():
	print("Press 'Esc' to stop recording and recognize speech.")
	
	try:
		while True:
			audio_data, sample_rate = record_audio()
			
			# Check if the 'Esc' key is pressed to stop recording
			if keyboard.is_pressed('Esc'):
				break

			recognize_speech(audio_data, sample_rate)
	except KeyboardInterrupt:
		print("Recording stopped.")


def record_audio_condition(print_callback=print):
    def print_elapsed_seconds(elapsed_seconds):
        print_callback(str(elapsed_seconds) + '..')

    print_callback("Recording started. Press 'Q' to stop recording and perform speech recognition...\n")

    sd.default.samplerate = 44100
    sd.default.channels = 1
    sd.default.dtype = "int16"

    recording = sd.rec(int(10 * sd.default.samplerate))  # Assume a default duration of 10 seconds
    start_time = time.time()
    elapsed_seconds = 0

    while True:
        print_elapsed_seconds(elapsed_seconds)
        time.sleep(1)

        # Check for key events
        events = keyboard.record(until='Q')
        if any(event.event_type == keyboard.KEY_DOWN for event in events):
            print_callback("Recording stopped.\n")
            sd.stop()
            break

        elapsed_seconds += 1

    audio_data = recording.flatten()
    sample_rate = sd.default.samplerate

    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

    try:
        print_callback("Processing audio...\n")
        text = recognizer.recognize_google(audio)
        print_callback(f"Recognized text:\n{text}")
        return text
    except sr.UnknownValueError:
        print_callback("Unable to recognize speech.\n")
        return ""
    except sr.RequestError as e:
        print_callback(f"Speech recognition request error: {e}\n")
        return ""
    except Exception as e:
        print_callback(f"Speech recognition exception: {e}\n")
        return ""

def test_record_audio_condition():  # gak berhasil panjang...cuma kebaca dikit
	recorded_text = record_audio_condition()
	print(recorded_text)

# import soundfile as sf
# import sounddevice as sd
# import speech_recognition as sr
# import time
# import keyboard
# import tempfile
# import os

def record_audio_with_condition_callback(condition_callback, print_callback=print):
    def print_elapsed_seconds(elapsed_seconds):
        print_callback(str(elapsed_seconds) + '..')

    print_callback("Recording started. Press 'Q' or satisfy the condition to stop recording and perform speech recognition...\n")

    sd.default.samplerate = 44100
    sd.default.channels = 1
    sd.default.dtype = "int16"

    recording = sd.rec(int(10 * sd.default.samplerate))  # Assume a default duration of 10 seconds
    elapsed_seconds = 0

    while not condition_callback():
        print_elapsed_seconds(elapsed_seconds)
        time.sleep(1)

        # Check for key events (optional)
        events = keyboard.record(until='Q')
        if any(event.event_type == keyboard.KEY_DOWN for event in events):
            print_callback("Recording stopped by key press.\n")
            sd.stop()
            break

        elapsed_seconds += 1

    print_callback("Recording stopped.\n")
    sd.stop()

    audio_data = recording.flatten()
    sample_rate = sd.default.samplerate

    recognizer = sr.Recognizer()
    audio = sr.AudioData(audio_data.tobytes(), sample_rate, 2)

    try:
        print_callback("Processing audio...\n")
        text = recognizer.recognize_google(audio)
        print_callback(f"Recognized text:\n{text}")
        return text
    except sr.UnknownValueError:
        print_callback("Unable to recognize speech.\n")
        return ""
    except sr.RequestError as e:
        print_callback(f"Speech recognition request error: {e}\n")
        return ""
    except Exception as e:
        print_callback(f"Speech recognition exception: {e}\n")
        return ""

def test_record_audio_with_condition_callback():
	start_time = time.time()
	def my_condition_callback():
		# Replace this with your own condition logic
		# Return True to stop recording, False to continue
		return time.time() - start_time >= 20  # Stop recording after 20 seconds

	recorded_text = record_audio_with_condition_callback(condition_callback=my_condition_callback)
	print(recorded_text)

if __name__ == "__main__":
	main_keyboard()


# pip install gTTS
# https://stackoverflow.com/questions/59623969/pygame-error-failed-loading-libmpg123-dll-attempt-to-access-invalid-address
from gtts import gTTS
from playsound import playsound  # pip install playsound
import vlc
import time
from num2words import num2words
from .fileutils import file_remove, hapus_file


def sample(text='Learn Python from Medium', outputpath='c:/tmp/python.mp3'):
    from pygame import mixer
    tts = gTTS(text)
    tts.save(outputpath)
    mixer.init()
    # pygame.error: Failed loading libmpg123-0.dll: The specified module could not be found.
    mixer.music.load(outputpath)
    # mixer.music.play(loops=-1)
    mixer.music.play()


def denger(filepath='c:/windows/media/alarm01.wav'):
    """
    Name: playsound
    Version: 1.3.0
    pip install playsound==1.2.2
    """
    # playsound(filepath)
    vlc.MediaPlayer(filepath).play()


def speak(text='Learn Python from Medium', outputpath='c:/tmp/tts.mp3', delay=0.5):
    # file_remove(outputpath)
    hapus_file(outputpath)
    tts = gTTS(text)
    tts.save(outputpath)
    time.sleep(delay)
    denger(outputpath)


def angka(bilangan):
    # pip install num2words
    return num2words(bilangan)

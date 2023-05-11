import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator


wit_api_key = 'RAWZEC4AYA5JDCG4ZTY63ARKLZLHFDZK'

#for mandarin no tld, for others put "tld=tld_for_tts" besides 'lang=...' in 'tts=gTTS(....'
#tld is accent
src_lang = 'en'
destination_lang = 'ja'

#tld_for_tts = 'pt'

translator = Translator()
rec = sr.Recognizer()

def speak(word):
    tts = gTTS(text=word, lang=destination_lang,)# tld=tld_for_tts)
    tts.save('output_gTTS.mp3')
    playdub = AudioSegment.from_mp3("output_gTTS.mp3")
    play(playdub)

while True:

    print("Recording...")
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source, duration=1)
        source.pause_treshold = 1
        audio = rec.listen(source, phrase_time_limit=None, timeout=None)
        
    try:
        print('...')
        transcript = rec.recognize_wit(audio, key=wit_api_key)
        
        if transcript == 'Exit':
            print("Exiting")
            break
        
        else:
            translation = translator.translate(transcript, src=src_lang, dest=destination_lang)
            print('EN : ', transcript)
            print('TRANSLATED : ', translation.text)
            speak(translation.text)
            

    except:
        print("An error occured...")
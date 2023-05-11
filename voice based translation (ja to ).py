import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator


wit_api_key = 'V7ZQZCY5OB7RHVYOLGJHNWO57UX2B2EV'

#for mandarin no tld, for others put "tld=tld_for_tts" besides 'lang=...' in 'tts=gTTS(....'
src_lang = 'ja'
destination_lang = 'en'
tld_for_tts = 'us'

translator = Translator()
rec = sr.Recognizer()

def speak(word):
    tts = gTTS(text=word, lang=destination_lang, tld=tld_for_tts)
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
        
        if transcript == '赤': # 赤 = aka
            print("exiting")
            break
        
        else:
            translation = translator.translate(transcript, src=src_lang, dest=destination_lang)
            print('JA : ', transcript)
            print('TRANSLATED : ', translation.text)
            speak(translation.text)
            

    except:
        print("An error occured...")
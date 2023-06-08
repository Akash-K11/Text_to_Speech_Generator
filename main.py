import pyttsx4 as pyt
engine = pyt.init()

print("""Hi there, welcome to Text to Speech Generator.
      Enter 'q' to exit.
      Enter 'g' to open guide.""")
engine.say("Hi there, welcome to Text to Speech Generator. Enter the text to generate speech for it.")
engine.runAndWait()

while True:
    text1 = input("Enter the text: ")
    match text1:
        case 'q':
            print("Ending the program.")
            engine.say("Ending the program.")
            engine.runAndWait()
            break
        case 'g':
            print("""Enter:
            'v+' to increase volume 
            'v-' to decrease volume
            'r+' to increase rate
            'r-' to decrease rate
            'c' to change voice """)
            continue
        case 'v+':
            volume = engine.getProperty('volume')
            # try:
            engine.setProperty('volume', volume + 0.25)
            engine.say('Volume has been increased successfully.')
            engine.runAndWait()
            # except:
            #     vol_max = "Volume is already at maximum level."
            #     print(vol_max)
            #     engine.say(vol_max)
            #     engine.runAndWait()
        case 'v-':
            # try:
            volume = engine.getProperty('volume')
            engine.setProperty('volume', volume - 0.25)
            engine.say('Volume has been decreased successfully.')
            engine.runAndWait()
            # except:
            #     vol_min = "Volume is already at minimum level."
            #     print(vol_min)
            #     engine.say(vol_min)
            #     engine.runAndWait()
        case 'r+':
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate + 50)
            engine.say('Speech rate has been increased successfully.')
            engine.runAndWait()
        case 'r-':
            rate = engine.getProperty('rate')
            engine.setProperty('rate', rate - 50)
            engine.say('Speech rate has been decreased successfully.')
            engine.runAndWait()
        case 'c':
            voices = engine.getProperty('voices')
            for i, voice in enumerate(voices):
                engine.setProperty('voice', voice.id)
                engine.say(f'For this voice, enter {i}')
            engine.runAndWait()
            voice_choice = int(input("Press the number corresponding to desired choice: "))
            engine.setProperty('voice', voices[voice_choice].id)
            engine.say("Hello there, this will be voice of speech from now on.")
            engine.runAndWait()
        case _:
            engine.say(text1)
            engine.runAndWait()

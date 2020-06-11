import pyttsx3
import speech_recognition as sr
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Bot():

    #this function is to setup audio 
    def __speech_setup(self):
        __engine=pyttsx3.init('sapi5')
        __voices=__engine.getProperty('voices')
        __engine.setProperty('voice',__voices[0].id)
        return __engine

    #this function is to train CREATE and TRAIN our bot
    def __chat_setup(self):
        __cb = ChatBot('Jarvis')
        __convo = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
            'What is your name ?',
            'My name is Jarvis I was created by IronMan',
            'In which language do you talk',
            'Mostly i talk in English',
            'Where are you from',
            'I was originated in New York but now i live in Jalandhar'
        ]
        __trainer = ListTrainer(__cb)
        __trainer.train(__convo)
        return __cb

    #constructor which setup the audio and trains the bot as soon as object in created
    def __init__(self):
        print('Initiating Jarvis ... \nSeting Up Speech...')
        self.__speek = self.__speech_setup()
        print('Speech Setup. \nTraining Jarvis...')
        self.__chat = self.__chat_setup()
        print('Jarvis is ready to use \nSay Hello to Jarvis')
    
    #this meathod converts text to audio
    def __Say(self,text):
        self.__speek.say(text)
        print(text)
        self.__speek.runAndWait()

    #this is the main function which take command and gives output
    def take_command(self):
        __recogniser = sr.Recognizer()
        __counter=0   #used this variable so that we can speek again if it fails to understand at first try
        while __counter<=3:
            __counter+=1
            #listning to audio with default microphone
            with sr.Microphone() as source:
                self.__Say('Listening...')
                __audio = __recogniser.listen(source)
            #recognising and converting audio into text
            try:
                print('Recognising....')
                __query=__recogniser.recognize_google(__audio,language='en-us')
                print(__query)
                self.__Say(self.__chat.get_response(__query))
                break
            except:
                text = 'unable to recognise' if __counter<=3 else 'Try again Later'
                self.__Say(text)
                __query=None
            
        

if __name__ == "__main__":
    Jarvis=Bot()
    response ='0'
    while response == '0':
        Jarvis.take_command()
        response=input('press 0 to give command or anything else to exit')

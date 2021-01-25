# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 05:29:14 2021
@author: feranmi
"""
import pandas as pd
import numpy as np
data=pd.read_csv('C:\Apps\scrapef.csv',encoding='utf-8')
#shift value of answers up 
data['questions']=data['questions']
data['answers']=data['answers'].shift(periods=-1)
data.dropna(axis=0,how='any',inplace=True)
me=list(data['questions'])
you=list(data['answers'])
#merge two lists horizontally
mex = [x if i%1 else 'questionz:'+ x for i, x in enumerate(me)]
youx= [x if i%1 else 'answerz:'+ x for i, x in enumerate(you)]
yx=[item for items in zip(mex,youx) for item in items]
#print(yx)

from chatterbot.chatterbot import ChatBot
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak


bot = ChatBot(
    'InverterBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'InverterBot',  
    logic_adapters=[
        {
            'import_path': 'zz.MyLogicAdapter',
            'default_response': 'I am sorry, but I do not understand your question.',
            'maximum_similarity_threshold': 0.95
        },
        'chatterbot.logic.TimeLogicAdapter'],
            preprocessors=[
        'chatterbot.preprocessors.clean_whitespace'
    ]
)
# Create a new instance of a ChatBot

        

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)
trainer.train((yx))
name=input("Enter Your Name: ")
print("Welcome to the inverter solutions Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye':
        print('Bot: Bye')
        break
    else:
        while True:
            response=bot.get_response(request)
            tag_type= str(response).split(':')[0]
            if tag_type!='questionz':
                break
        print('Bot:',response)
        speak(str(response))
        

#print(result.confidence)
        


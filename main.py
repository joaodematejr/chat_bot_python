import re, json
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('TW Chat Bot')

conversation = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 
			'Você gosta de programar?', 'Sim, eu programo em Python']

trainer = ListTrainer(bot)

trainer.train(conversation)

def main():
    while True:
        pergunta = input("Usuário: ")
        resposta = bot.get_response(pergunta)
        if pergunta == 'parar':
            break
        if float(resposta.confidence) > 0.5:
            print('TW Bot: ', resposta)
        else:
            print('TW Bot: Ainda não sei responder esta pergunta')

if __name__ == '__main__':
    main()
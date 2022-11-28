 while True:
        pergunta = input("Usuário: ")
        resposta = bot.get_response(pergunta)
        if pergunta == 'parar':
            break
        if float(resposta.confidence) > 0.5:
            print('TW Bot: ', resposta)
        else:
            print('TW Bot: Ainda não sei responder esta pergunta')
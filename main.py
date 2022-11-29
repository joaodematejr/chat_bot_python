import os
import time
import re

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

bot = ChatBot("TW Chat Bot")
driver = webdriver.Chrome()
trainer = ListTrainer(bot)

nameGroup = "Bot"

conversation = [
    "Oi",
    "Olá",
    "Tudo bem?",
    "Tudo ótimo",
    "Você gosta de programar?",
    "Sim, eu programo em Python",
]


def listening():
    while True:
        #_2gzeB
        #_3xTHG
        #_33LGR
        contact = driver.find_element(By.CLASS_NAME, '_33LGR')
        time.sleep(1)
        #contact2 = driver.find_element_by_css_selector(By.CSS_SELECTOR, 'selectable-text copyable-text')
        #texto = driver.find_element(By.CSS_SELECTOR, "selectable-text copyable-text").text
        # ultimo = len(post) - 1
        # texto = driver.find_element_by_css_selector(By.CSS_SELECTOR,'span.selectable-text').text
       
        #print(contact.text)
        time.sleep(5)
        print(contact.text)

        print("Bot: ", contact.text)

        if contact.text == "oi":
            print("45")
            

        


def salutation():
    input = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div')
    input.click()
    input.send_keys(["Bot: Oi, sou o robozin!", "Bot: Use :: no início para falar comigo"])
    time.sleep(1)
    input.send_keys(Keys.ENTER)
    time.sleep(1)
    listening()


def main():
    trainer.train(conversation)
    driver.get("https://web.whatsapp.com/")
    time.sleep(5)
    while True:
        if driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[3]/div[1]/div/div[1]/div'):
            print("Aguardando conexão...")
            time.sleep(5)
        else:
            print("Conectado")
            time.sleep(20)
            break
    inputFilter = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    inputFilter.click()
    inputFilter.send_keys(nameGroup)
    time.sleep(2)
    print(nameGroup)
    contact = driver.find_element(By.XPATH, '//span[@title = "{}"]'.format(nameGroup))
    contact.click()
    salutation()


if __name__ == "__main__":
    main()




#while True:
    #pergunta = input("Usuário: ")
    #resposta = bot.get_response(pergunta)
    #if pergunta == 'parar':
        #break
    #if float(resposta.confidence) > 0.5:
        #print('TW Bot: ', resposta)
    #else:
        #print('TW Bot: Ainda não sei responder esta pergunta')
from time import sleep
from loguru import logger

def primeira_atividade():
    print('Primeira atividade')
    sleep(2)

def segunda_atividade():
    print('Segunda atividade')
    sleep(1)

def terceira_atividade():
    print('Terceira atividade')
    sleep(1)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print('pipeline finalizada')

pipeline()
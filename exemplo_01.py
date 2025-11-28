from time import sleep
from loguru import logger

def primeira_atividade():
    print('Primeira atividade')
    logger.info('Primeira atividade')
    sleep(2)

def segunda_atividade():
    print('Segunda atividade')
    logger.info('Segunda atividade')
    sleep(1)

def terceira_atividade():
    print('Terceira atividade')
    logger.info('Terceira atividade')
    sleep(1)

def pipeline():
    primeira_atividade()
    segunda_atividade()
    terceira_atividade()
    print('pipeline finalizada')
    logger.info('pipeline finalizada')

pipeline()
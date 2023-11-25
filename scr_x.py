import os
from dotenv import load_dotenv
load_dotenv()
from gigachat import GigaChat

TOKEN = os.getenv('SBER_GIGACHAT')

# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
with GigaChat(credentials=TOKEN, verify_ssl_certs=False) as giga:
    response = giga.chat("Какие факторы влияют на стоимость страховки на дом?")
    print(response.choices[0].message.content)
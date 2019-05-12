import os
import requests

API_KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'


way = input('Введите путь файла ')
way_new = input('Введите путь для нового файла ')
language = input('Язык с которого перевести (fr - французский, es - испанский, de - немецкий) ')
new_language = input('Язык на который нужно перевести (fr - французский, es - испанский, de - немецкий, en - английски) или нажмите Enter ')
if not new_language:
    new_language = 'ru'

def translate_it(text, lang, text_new, to_lang):

    with open(text,  encoding='utf-8') as f:
        text = f.read()

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang, to_lang),
    }

    data = {
        'text': text
    }

    response = requests.get(URL, params=params, data=data)
    print(response)
    json_ = response.json()
    file_path = os.path.join(text_new, os.path.basename('{}-{}.txt'.format(lang,to_lang)))
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json_['text'][0])


translate_it(text=way, lang=language, text_new=way_new, to_lang=new_language)

'''
Created on Dec 3, 2018

@author: Florian "lfko" Becker
'''
import urllib.request
import urllib.parse
import json


def translate(word, sourceLang='en', targetLang='tr'):
    """ """
    print(' translating word {} to target language {}'.format(
        word, sourceLang, targetLang))
    return __openUrl__(word, sourceLang, targetLang)


def __openUrl__(word, source, target):
    """ 
        @param word: the word to translate
        @param source: source language (e.g. 'en')
        @param target: target language (e.g. 'tr')
        @return: translation of the word as string
    """
    #url = 'http://cevir.ws/vl?q=' + word + '&m=25&p=both&l' + target
    # free Google Translate API (without developer registration)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + source + '&tl=' + \
        target + '&dt=t&q=' + urllib.parse.quote_plus(word)

    print(' open url to translation service: ', url)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    # TODO add timeout

    resp = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(resp) as response:
        raw_data = response.read()

    json_data = json.loads(raw_data.decode())

    return json_data[0][0][0]

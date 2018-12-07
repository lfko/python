'''
Created on Dec 3, 2018

@author: Florian "lfko" Becker
'''
import urllib.request
import json
from pprint import pprint


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
    """
    #url = 'http://cevir.ws/vl?q=' + word + '&m=25&p=both&l' + target
    # free Google Translate API (without developer registration)
    url = 'https://translate.googleapis.com/translate_a/single?client=gtx&sl=' + source + '&tl=' + \
        target + '&dt=t&q=' + word

    print(' open url to translation service: ', url)

    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    # TODO add timeout
    resp = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(resp) as response:
        raw_data = response.read()
    #raw_data = resp.read()
    print(raw_data)
    #encoding = resp.info().get_content_charset('utf-8')
    json_data = json.loads(raw_data.decode())
    pprint(json_data[0][0][0])
    # return __deserialize_json__(json_data)


def __deserialize_json__(json_data):
    """ """
    req_status = json_data['control']

    if req_status['status'] == 'ok' and req_status['results'] > 0:
        word_meta = json_data['word']

        trans_dict = word_meta[0]
        trans_dict['title']
        trans_dict['desc']
    else:
        print('no translation could be found!')

    # TODO return the actual translation
    return "WORD"


if __name__ == '__main__':
    #a = translate('I did not understand')
    # print(a)
    st = 'aamakmek'
    replace = ''
    mode = 'in'
    tense = 'yor'
    person = 'um'
    f = eval(
        'st.replace("mak", replace).replace("mek", replace) + mode + tense + person')
    print(type(f))
    print(f)
    #print(st.replace(infinitive, replace) + mode + tense + person)

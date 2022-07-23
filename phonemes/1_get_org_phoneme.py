from bs4 import BeautifulSoup
import requests
import time

with open('phonemes/words.txt', 'r') as f:
    words_list = f.read().splitlines()
f_phoneme_ENG = open('phonemes/phoneme_ENG.txt', 'w+')
f_phoneme_AME = open('phonemes/phoneme_AME.txt', 'w+')
for word in words_list:
    print(word)
    try:
        url =  'https://www.oxfordlearnersdictionaries.com/definition/english/'+word+'?q='+word
        headers = requests.utils.default_headers()
        headers.update(
            {
                'User-Agent': 'My User Agent 1.0',
            }
        )
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        phonemes = soup.find_all('span', class_='phon')
        if len(phonemes) == 0:
            url =  'https://www.oxfordlearnersdictionaries.com/definition/english/'+word+'1_1?q='+word
            if word in ["favourite", "to"]:
                url =  'https://www.oxfordlearnersdictionaries.com/definition/english/'+word+'_1?q='+word
            headers = requests.utils.default_headers()
            headers.update(
                {
                    'User-Agent': 'My User Agent 1.0',
                }
            )
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            phonemes = soup.find_all('span', class_='phon')
            if word=="theater":
                f_phoneme_ENG.write("θɪətə"+'\n')
                f_phoneme_AME.write("θiːətər"+'\n')
                continue
        if len(phonemes) > 2:
            print(word, 'has more than 2 phonemes')
            print(phonemes)
        f_phoneme_ENG.write(phonemes[0].text.replace("/", "")+'\n')
        f_phoneme_AME.write(phonemes[1].text.replace("/", "")+'\n')
        # time.sleep(0.2)
    except Exception as e:
        print(e)
        continue
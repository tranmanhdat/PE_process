with open('phonemes/phoneme_ENG.txt', 'r') as f:
    phoneme_ENG_list = f.read().splitlines()
with open("phonemes/words.txt", 'r') as f:
    words_list = f.read().splitlines()
phoneme_present_dict = {}
with open('phonemes/phonemes_mapping.txt', 'r') as f:
    for line in f:
        pieces = line.strip().split('\t')
        phoneme_present_dict[pieces[0]] = pieces[1]
# print(phoneme_present_dict)
f_phoneme_ENG = open('phonemes/phoneme_ENG_2.txt', 'w+')
for idx, word in enumerate(words_list):
    phonemes_list = []
    j = 0
    print(word)
    while j<len(phoneme_ENG_list[idx])-1:
        if j+1 <= len(phoneme_ENG_list[idx])-1:
            if phoneme_ENG_list[idx][j:j+2] in phoneme_present_dict:
                phonemes_list.append(phoneme_ENG_list[idx][j:j+2])
                j = j+2
                continue
        phonemes_list.append(phoneme_ENG_list[idx][j])
        j = j + 1
    if j == len(phoneme_ENG_list[idx])-1:
        phonemes_list.append(phoneme_ENG_list[idx][j])
    f_phoneme_ENG.write(word+"\n")
    f_phoneme_ENG.write(" ".join([character for character in word])+"\n")
    f_phoneme_ENG.write(' '.join(phonemes_list)+'\n')
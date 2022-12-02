sentence = 'Jim quickly realized that the beautiful gowns are expensive'
letterDic = {}

for letter in sentence:
    if letter not in letterDic:
        letterDic[letter] = sentence.count(letter)

print(letterDic)

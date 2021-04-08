from itertools import product as p
import hashlib
import random

punc = [('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '{', '}', '|', ':', ';', '[', ']', '?', '>', '<')]
numbers = [('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')]
salt = '2458307'
leet = {'s': '$', 'a': '4', 'l': '1', 'e': '3', 't': '7', 'i': '1', 'o': '0', 'b': '8', 'g': '9'}
dictionary = []
leetlist = []
leetBaseWord = []
possibles = []

# get the flags from the flags.txt file and store data in possibles[]

with open("C:\\Users\\bcord\\PycharmProjects\\PythonPractice\\flags.txt", 'r') as hashfile:
    for line in hashfile:
        possibles.append(line.rstrip('\n'))

with open("C:\\Users\\bcord\\PycharmProjects\\PythonPractice\\wordsGreaterThanTen.txt") as wordfile:
    for lines in wordfile:
        dictionary.append(lines.rstrip('\n'))

# perform leet speak substitutions from dictionary. store in leetlist[]

for words in dictionary:
    leetSub = (''.join(letters) for letters in p(*({c, leet.get(c, c)} for c in words)))
    leetlist.append(leetSub)

# retrieve values from generator and store in list leetBaseWord[]

for item in leetlist:
    for word in item:
        leetBaseWord.append(word)
random.shuffle(leetBaseWord)


def combinations(r):
    for i in p(leetBaseWord, *punc, *numbers, possibles):
        format = "4621_ctf{{{0}}}"
        words = (format.format((''.join(i[0:3]))) + salt)
        capwords = (format.format((''.join(i[0:3]).capitalize())) + salt)
        base = hashlib.sha256(words.encode('utf-8')).hexdigest()
        basecapword = hashlib.sha256(capwords.encode('utf-8')).hexdigest()
        hashes = (i[-1])

        if base == hashes:
            with open("candidateWords.txt", 'a') as file1:
                file1.writelines("match success: " + hashes + "," + base + "," + words + '\n')

        elif basecapword == hashes:
            with open("candidateWords.txt", 'a') as file1:
                file1.writelines("match success: " + hashes + ", " + basecapword + ", " + capwords + '\n')

        else:
            #print(hashes + "," + base + "," + words)
            #print(hashes + " " + basecapword + " " + capwords)
            continue

    for w in p(leetBaseWord, *numbers, *punc, possibles):
        format = "4621_ctf{{{0}}}"
        words = (format.format((''.join(w[0:3]))) + salt)
        capwords = (format.format((''.join(w[0:3]).capitalize())) + salt)
        base = hashlib.sha256(words.encode('utf-8')).hexdigest()
        basecapword = hashlib.sha256(capwords.encode('utf-8')).hexdigest()
        hashes = (w[-1])

        if base == hashes:
            with open("candidateWords.txt", 'a') as file1:
                file1.writelines("match success: " + hashes + ", " + base + "," + words + '\n')

        elif basecapword == hashes:
            with open("candidateWords.txt", 'a') as file1:
                file1.writelines("match success: " + hashes + ", " + basecapword + ", " + capwords + '\n')

        else:
            #print(hashes + "," + base + "," + words)
            #print(hashes + "," + basecapword + "," + capwords)
            continue

combinations(str(leetlist))

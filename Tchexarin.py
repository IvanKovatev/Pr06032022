# import spacy
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("He bought a beautiful and fast car.")
# # to match the output style of the Stanford library for comparison...
# for token in doc:
#     print(f"{token.dep_}({token.head.text}-{token.head.i+1}, {token.text}-{token.i+1})")

# from re import A
file = ['The head', 'is not waiting', 'for the tai']

nouns = 'The head'
verb = 'is not waiting'
adverb = 'for the tail'

d = 5
n = 0
v = 0
a = 0

with open('text.txt') as fille:
    if nouns == file[0]:
        n += 1

    if verb == file[1]:
        v += 1

    if adverb == file[2]:
        a += 1

    else:
        d += 0

print('Сущ: ', n)
print('Гл: ', v)
print('Нар: ', a)
print('Др: ', d )
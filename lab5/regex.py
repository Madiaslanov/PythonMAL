#1
import re

# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# founded = re.findall(r'а(?:б*)',g)

# print(founded)

# #2
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# founded = re.findall(r'а\б{2,3}',g)

# print(founded)

#3
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# founded = re.findall(r'\w[а-я]+-\w[а-я]+',g)

# print(founded)

#4
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# founded = re.findall(r'[А-Я]{1}(?:[а-я]+)',g)

# print(founded)

#5
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# founded = re.findall(r'а.+б$',g)

# print(founded)

# #6
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# sub = re.sub(r' ',':.',g)

# print(sub)

# #7
# def tuie(zhylan):
#     слова = zhylan.split('_')
    
#     tuie = слова[0] + ''.join(word.capitalize() for word in слова[1:])
    
#     return tuie

# with open('reg_file.txt', 'r', encoding='utf-8') as файл:
#     zhylan = файл.read()

# zhylan = tuie(zhylan)

# print(tuie)

#8
# with open('reg_file.txt', 'r', encoding='utf-8') as file:
#     g = file.read()

# def taptym_au_seni(match):
#     return match.group(0).upper()

# sub = re.sub(r'[а-я]', taptym_au_seni, g)

# print(sub)

# 9
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()

# sub = re.sub(r'[А-Я]',' \1',g)

# print(sub)

# #10
# with open('reg_file.txt','r',encoding='utf-8') as file:
#     g = file.read()
#     snake = re.sub(r'(?<!^)(?=[А-Я])', '_',g).lower()
#     print(snake)

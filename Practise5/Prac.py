# print (re.search("^"))
# print(re.findall("текст поиска", откуда, re.флаг))
# print(re.findall("[символы для поиска]", откуда искать))
# x = re.sub("что", "на что", txt, сколько раз замену сделать) замена символов
# x = re.search("что надо найти", txt) возвращает match, нач и конец индекса, что match
import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
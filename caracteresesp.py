import re
man = open('mbox-short.txt')
for linea in man:
    linea = linea.rstrip()
    if linea.find("From:"):
        print(linea)
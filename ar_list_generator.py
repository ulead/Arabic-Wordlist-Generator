#-------------------------------------------------------------------------------
# Name:        ar_list_generator
# Purpose:      genrate an arabic wordlist for (education purpos only)
#
# Author:      Mohammed Alessa
#
# Created:     30/04/2021
# Copyright:   FREE
# Licence:     Creative Commons license
#-------------------------------------------------------------------------------


import re

data = open("rawdata.txt","r",encoding="utf-8")

print(data.read(100)) # للتأكد من البيانات سيتم طباعة اول 100 حرف (قد تأخذ طباعة كامل النص وقت طويل)

textData = data.read()
for line in textData.split("\n"):
    for word in line.split(" "):
        re.findall(r'[\u0600-\u06FF]+',word)
        for word1 in word.split(":"):
            if not (word1.isnumeric()):
                wordlist = open("wordlist.txt", "w",encoding="UTF-8")
                wordlist.write(word1+"\n")


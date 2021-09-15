# -*- coding: utf-8 -*-
"""

Edmond Tongyou
CPSC 223P-01
Wed March 03, 2021
tongyouedmondfullerton.edu

"""

# Maybe you can use some functions from the string module
import string

# Simple check to see if a specific word is in the
# list, returns the list tuple as so
# (times repeated, word)
def numWordsSpoken(candidate, word):
  if "Romney" in candidate:
    for index in range (0, len(romneyList)):
      if word in romneyList[index]:
        numSpoken = romneyList[index]
        break
  if "Obama" in candidate:
    for index in range (0, len(obamaList)):
      if word in obamaList[index]:
        numSpoken = obamaList[index]
        break
  return numSpoken


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named stopWordsString
stopWordsFile = open("stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()


# Start your code here

# The addition of swapSpeaker is to check if the
# current speaker has changed which indicates that
# their name is part of the next word, therefore the
# loop will continue early
romneyDict = {}
romneyList = []
obamaDict = {}
obamaList = []
currentWord = ""
currentSpeaker = 0
index = 0
swapSpeaker = False
debateString = debateString.split()

# Loop which uses enumeration to index specific words,
# this is to allow for the ability to peak into the
# next word in case we need to check for the speaker.
# All words are set to lowercase to keep (key,value)
# consistancy. Checks for any punctuation in the word
# and cuts it off the word if found in it. A check for
# when words are interrupted (--) is found and skips
# the word if seen.
for index, currentWord in enumerate(debateString):
  if swapSpeaker == False:
    if "." in currentWord or "," in currentWord or "!" in currentWord or "?" in currentWord or ":" in currentWord:
      currentWord = currentWord[:len(currentWord) - 1]

    if "--" in currentWord:
      continue


    if currentWord.lower() in stopWordsString:
      continue

    if "MR" in currentWord:
      if "ROMNEY" in debateString[index + 1]:
        currentSpeaker = 1
        swapSpeaker = True
        continue
    
    if "PRESIDENT" in currentWord:
      if "BARACK" in debateString[index + 1] or "OBAMA:" in debateString[index + 1]:
        currentSpeaker = 2
        swapSpeaker = True
        continue

    if "MR" in currentWord:
      if "LEHRER" in debateString[index + 1]:
        currentSpeaker = 0
        swapSpeaker = True
        continue
    
    if currentSpeaker != 0:
      currentWord = currentWord.lower()

      if currentSpeaker == 1:
        if currentWord not in romneyDict:
          romneyDict[currentWord] = 0
        romneyDict[currentWord] += 1

      if currentSpeaker == 2:
        if currentWord not in obamaDict:
          obamaDict[currentWord] = 0
        obamaDict[currentWord] += 1

  swapSpeaker = False


# Converts the dictionary to a list of tuples so that
# they can be sorted via sort()
romneyList = [(value, key) for key, value in romneyDict.items()]
obamaList = [(value, key) for key, value in obamaDict.items()]

# Sorts the list which puts it in ascending order,
# this is then reversed for the desired output
romneyList.sort()
obamaList.sort()
romneyList.reverse()
obamaList.reverse()

# Loop which only keeps the top 40 words in the list
while len(romneyList) != 40:
  romneyList.pop()
while len(obamaList) != 40:
  obamaList.pop()

print (romneyList)
print (obamaList)
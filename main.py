#variables required for the game
_win = False
_incorrect = 0
_word = []
_blankWord = []

#gets the user input and returns it
def userInput():
  _input = input()
  return _input

#split a string and add it to a list
#checks to see if the word contains special charcters or numbers
def setWord():
  _tword = userInput().lower()
  if _tword.isalpha() == True:
    _word = list(_tword)
    return _word
  else:
    print("Please use letters only (no numbers or special characters).")
    return setWord()
  
#creates a blank list to use
def setBlankWord(_word):
  for i in range(len(_word)):
    _blankWord.append("_")
  return _blankWord

#checks for a match in the arraylist, returns the value if correct
#uses recursion to check for duplicates
#sets all used words to set for duplicate checks
def match(_word, _input, _blankWord):
  for x in _word:
    if _input == x:
      _blankWord[_word.index(x)] = _input
      _word[_word.index(x)] = "set"
      match(_word, _input, _blankWord)
  return _blankWord

#converts list to string
def stringify(_list):
  word = ""
  for x in _list:
    word += x
  return word
  
#used if the player is incorrect  
def looseHangman(_incorrect):
  hangedman = [["-","-","-", "-"],[" "," "," ", "|"],[" "," "," ", "|"], [" "," "," ", "|"], [" "," "," ", "|"],["-","-","-", "-"]]
  if _incorrect > 0:
    hangedman[1][1] = "|"
    if _incorrect > 1:
      hangedman[2][1] = "0"
      if _incorrect > 2:
        hangedman[3][0] = "/"
        if _incorrect > 3:
          hangedman[3][1] = "|"
          if _incorrect > 4:
            hangedman[3][2] = "\\"
            if _incorrect > 5:
              hangedman[4][0] = "/"
              if _incorrect > 6:
                hangedman[4][2] = "\\"

  for i in range(len(hangedman)):
    print(stringify(hangedman[i]))
  if _incorrect < 7:  
    print("{} guesses left!".format(7-_incorrect))
    return False
  else:
    print("You have lost!")
    return True

#check if the blank word has any blank letters left
def winHangman(_blankWord):
  for x in _blankWord:
    if x == "_":
      return False
  print("You have won!")    
  return True  

#set the word
print("Please write a word to use (no numbers or special characters):")
_word = setWord()
_blankWord = setBlankWord(_word)
#while loop used to play the game
while _win == False:
  print("Please select a letter:")
  print("Current letters guessed: " + stringify(_blankWord))
  _input = userInput()[0].lower()
  #see if any changes have been made
  if stringify(_blankWord) != stringify(match(_word, _input, _blankWord)):
    _win = winHangman(_blankWord)

  #the user has chosen wrong, if _incorrect = 7 loose
  else:
    _incorrect+=1
    _win = looseHangman(_incorrect)
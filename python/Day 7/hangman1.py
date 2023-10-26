import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list=["arvark","baboon","camel"]
choser_word = random.choice(word_list)
print(choser_word)
show_list = []
ind = 0
check=0
lives=6
ans=0
check_match=0
for i in range(0,len(choser_word)):
    show_list.append("_")
while "_" in show_list:
    l_guess = input("guess a letter : ")
    for i in range(len(choser_word)):
        let = choser_word[i]
        if let==l_guess:
            check_match=1
            show_list[i]=let
        
    print(show_list)
    if check_match==0:
        lives-=1
        print(HANGMANPICS[5-lives])
        
    else:
        check_match=0
    if lives==-1:
        ans=1
        break


if ans==1:
    print("You lose")
else:
    print("you win")
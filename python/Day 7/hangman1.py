import random
word_list=["arvark","baboon","camel"]
choser_word = random.choice(word_list)
print(choser_word)
show_list = []
ind = 0;
check=0
for i in range(0,len(choser_word)):
    show_list.append("_")
while "_" in show_list:
    l_guess = input("guess a letter : ")
    for i in range(len(choser_word)):
        let = choser_word[i]
        if let==l_guess:
            check+=1
            show_list[i]=let
    print(show_list)
    
print("you win")
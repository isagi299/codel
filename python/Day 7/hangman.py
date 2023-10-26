print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
      ''')
import random
words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

a = random.choice(words)
print(a)
c=[]
p=6
x=0
e=""
ans=0
d=""
for i in range(0,len(a)):
    c.append("_")
while not p==0:
    b=input("guess a letter : ")
    for i in a:
        if i==b:
            print("you input right charecter.")
            c[x]=i
            # print(x)
            
            d = d[:x] + i + d[x:]
            ans=1
        
        x+=1
    x=0
    print(e.join(c))
    if ans==0:
        print("you input wrong letter.you lose a life")
        p-=1
        print(f"you have {p} charge left")
    else:
        ans=0
    
    if d==a:
        ans=2
        print("\nyou won")
        print(f"the word is {a}.")
        break
    if not ans==2 and p==5:
        print('''
        +---+
        |   |
        O   |
            |
            |
            |
        =========
              ''')
    if not ans==2 and p==4:
        print('''
        +---+
        |   |
        O   |
        |   |
            |
            |
        =========
              ''')
    if not ans==2 and p==3:
        print('''
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =========
              ''')
    if not ans==2 and p==2:
        print('''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =========
              ''')
    if not ans==2 and p==1:
        print('''
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        =========
              ''')

if not ans==2:
    print("\nyou lose")   
    print('''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =========
          ''')
    print(f"the correct word {a}.")
    

    
            
    
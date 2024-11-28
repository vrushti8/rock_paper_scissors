from random import randint
uguess=0
cguess=0
options=['rock','paper','scissors']
while True:
    uinput=input("Enter rock,paper,scissors or q to quit ").lower()
    if uinput=="q":
        break
    if uinput not in options:
        continue
    randomvalue=randint(0,2)
    cinput=options[randomvalue]
    print(f"computer picked {cinput}")

    if uinput=='rock' and cinput=='scissors':
        print("you win!")
        uguess+=1
    elif uinput=='paper' and cinput=='rock':
        print("you win!")
        uguess+=1
    elif uinput=='scissors' and cinput=='paper':
        print("you win!")
        uguess+=1
    elif uinput=='rock' and cinput =='rock':
        print("its a tie")
    elif uinput=='scissors' and cinput =='scissors':
        print("its a tie")
    elif uinput=='paper' and cinput =='paper':
        print("its a tie")
    else:
        print("you lost")
        cguess+=1
print(f"you won {uguess} times")
print(f"computer won {cguess} times")
if uguess>cguess:
    print("you have won the match")
print("end of match")



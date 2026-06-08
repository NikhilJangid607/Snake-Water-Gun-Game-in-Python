"""
1 for snake
0 for water
-1 for gun
"""

print("Good luck")
for i in range(1,6):
    import random
    computer=random.choice([1,0,-1])
    youlist={"s":1,"w":0,"g":-1}
    rev_list={1:"Sanke",0:"Water",-1:"Gun"}
    youstr=input("Enter your choice(S,W,G) : ")
    you=youlist[youstr]    
    print(f"You enter {rev_list[you]} \ncomputer enter {rev_list[computer]} ")
    if(computer==you):
        print("Its a draw.\n")
    else:
        if(computer==0 and you==1):
            print("You Win!\n")
        elif(computer==0 and you==-1):
            print("You Lose!\n")
        elif(computer==1 and you==0):
            print("You Lose!\n")
        elif(computer==1 and you==-1):
            print("You Win!\n")
        elif(computer==-1 and you==0):
            print("You Win!\n")
        elif(computer==-1 and you==1):
            print("You lose!\n")
        else:
            print("Enter a valid choice\n")

print("Thank you !")
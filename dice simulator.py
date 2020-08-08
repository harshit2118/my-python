min=1
max=6
K=True
from random import randint
while K:
    print("Rolling a dice")
    print("\nYou got {}".format(randint(min,max)))
    I=input("Continue(Y/N)")
    if I=="Y":
        K=True
    else:
        K=False
        print("Thank You For Playing")
        
              
        
    
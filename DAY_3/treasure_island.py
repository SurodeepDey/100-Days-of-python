import os
import sys
os.system('cls')

print(r"""
************************************************************************************************************************************
    _.--.
               _.-'_:-'||
              _.-'_.-::::'|| 
         _.-:'_.-::::::'  ||
          .'`-.-:::::::'     ||
         /.'`;|:::::::'      ||_
        ||   ||::::::'     _.;._'-._
        ||   ||:::::'  _.-!oo @.!-._'-.
        \'.  ||:::::.-!()oo @!()@.-'_.|
         '.'-;|:.-'.&$@.& ()$%-'o.'\U||
        `>'-.!@%()@'@_%-'_.-o _.|'||
         ||-._'-.@.-'_.-' _.-o  |'|| 
         ||=[ '-._.-\U/.-'    o |'|| 
         || '-.]=|| |'|      o  |'|| 
         ||      || |'|        _| '; 
         ||      || |'|    _.-'_.-' 
         |'-._   || |'|_.-'_.-' 
         jgs '-._'-.|| |' `_.-' 
              '-.||_/.-'
************************************************************************************************************************************
""")

print(f"Welcome to treasure island.\nYour mission is to find the treasure.")

l_or_r = input("You are at an intersection, Where do you want to go? (Left or Right): ").lower()

if l_or_r == 'left':
    swim_or_wait = input('You came across a river. Do you want to swim or wait for boat? (Swim or Wait):  ').lower()
    if swim_or_wait == 'wait':
        door_choice = input ('You arrived at the island unharmed. there are three doors. Which one you choose? (Red, Yellow or Blue): ').lower()
        if door_choice == 'yellow':
            print(f'You found the treasure! Congratulations!!')
        elif door_choice == 'red':
            print(f'You are burned by fire. Game Over!')
            sys.exit(1)
        elif door_choice == 'blue':
            print(f'You are eaten by beasts. Game Over!')
            sys.exit(1)
        else:
            print(f'You chose a door that does not exist. Game Over!')
            sys.exit(1)

    if swim_or_wait == 'swim':
        print(f'You are attacked by trout. Game Over!')
        sys.exit(1)
else:
    print(f'You fell into and hole. Game Over!')
    sys.exit(1)






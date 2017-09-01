#the dungeon adventure
import random
import time

items = []
global health
health = 10
goblin = [2,8]

print('You find yourself in a dark dungeon, with no idea where you are.')

#battle function
def fight(monster):
    
    global health
    print('Battle Start!')

    while (health > 0 and monster[1] > 0):
        if 'sword' in items:
            monster[1] -= 5
            print('You attack and deal 5 dmg to the monster!')
            time.sleep(2)
            if monster[1] <= 0:
                break
        else:
            monster[1] -= 1
            print('You attack and deal 1 dmg to the monster!')
            time.sleep(2)
            
        health -= monster[0]
        print('The monster attacks and deals ' + str(monster[0]) + ' to you!')
        time.sleep(2)
        
    if health > 0:
        print('You win the battle!') 
    else:
        print('You lose')
        
         
#very first room
def room_1():
    print('There are two doors, which one will you enter?')
    print('Left or Right?')
    choice = input()
    if choice == 'left':
        print('You open the left door, and enter the next room.')
        room_2()
    elif choice == 'right':
        print('You open the right door, and enter the next room.')
        room_3()

#room with the goblin
def room_2():
    print('You see a goblin right in front of you, about to attack you...')
    print('What will you do?')
    print('Sneak? Fight? Leave?')

    choice = input()
    if choice == 'fight':
        fight(goblin)
        print('You proceed to the next room...')
        room_4()
           
    elif choice == 'sneak':
        if random.randint(0,9) > 7:
            print('You manage to sneak past the goblin, and proceed to the next room...')
            room_4()
            
        else:
            print('You failed to sneak past the goblin.')
            print('He deals 2 damage to you!!')
            room_2()
            global health
            health = 0
            
    elif choice == 'leave':
        print('You leave the room...')
        room_1()
                
    else:
        print('Not an option, try again')
        room_2()
        

#room with the sword
def room_3():
    print('you walk into the room and find a sword on the ground')
    print('pick up the sword?')
    print('yes or no?')
    choice = input()
    if choice == 'yes':
          print('you pick up the sword')
          items.append('sword')
          room_1()
    elif choice == 'no':
          print('you leave the room')
          room_1()
    else:
          room_1()

#room after the goblin
def room_4():
    print('You enter the room, and see three doors ahead of you')
    print('which door will you try?')
    print('Left? Middle? Right?')
    choice = input()
    if choice == 'left':
        if 'key' in items:
            print('you use your key to unluck the door, and proceed to the next room')
            # go to room 5
            
    

        
#main game loop
while health > 0:
    room_1()

print('you died, game over')

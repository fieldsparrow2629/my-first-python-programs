#the dungeon adventure
import random

items = []
global health
health = 10

print('You find yourself in a dark dungeon, with no idea where you are.')

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
              if 'sword' not in items:
                print('You dont have a weapon, you take 5 damage!!')
                global health
                health -= 5
              else:
                print('You kill the goblin and proceed to the next room...')
                room_4()
              
    elif choice == 'sneak':
        if random.randint(0,9) > 7:
            print('You manage to sneak past the goblin, and proceed to the next room...')
            room_4()
            
                
        else:
            print('You failed to sneak past the goblin.')
            print('He deals 2 damage to you!!')
            health -= 2
            room_2()
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

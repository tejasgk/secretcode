alphabet='abcdefghijklmnopqrstuvwxyz'
key=3
newMessage=' '

message=input('please enter a a message:')

for character in message:
    position=alphabet.find(character)
    newPosition = (position + key) % 26
    newCharacter = alphabet[newPosition]
    newMessage+=newCharacter

print('your new message is',newMessage)





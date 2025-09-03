# Write code below 💖
Hufflepuff = 0
Slytherin = 0
Ravenclaw = 0
Gryffindor = 0

Dawn_Dusk = int(input('Q1) Do you like Dawn or Dusk? \n1) Dawn \n2) Dusk \n- '))

if Dawn_Dusk == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif Dawn_Dusk == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print('Wrong input')

Dead = int(input('Q2) When I’m dead, I want people to remember me as: \n1) The Good \n2) The Great \n3) The Wise \n4) The Bold \n- '))

if Dead == 1:
  Hufflepuff += 2
elif Dead == 2:
  Slytherin += 2
elif Dead == 3:
  Ravenclaw += 2
elif Dead == 4:
  Gryffindor += 2
else:
  print('Wrong input')

Music = int(input('Q3) Which kind of instrument most pleases your ear? \n1) The violin \n2) The trumpet \n3) The piano \n4) The drum \n- '))

if Music == 1:
  Slytherin += 4
elif Music == 2:
  Hufflepuff += 4
elif Music == 3:
  Ravenclaw += 4
elif Music == 4:
  Gryffindor += 4
else:
  print('Wrong input')

print('Your score for each house:', '\nSlytherin:', Slytherin, '\nHufflepuff:', Hufflepuff, '\nRavenclaw:', Ravenclaw, '\nGryffindor:', Gryffindor)
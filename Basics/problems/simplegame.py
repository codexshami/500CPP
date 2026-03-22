import random
player1= "vaibhav"
sum1=0
for i in range(5):
  temp=random.randint(1,5)
  print (temp)
  sum1= sum1+temp
print(player1)
print("reaches to")
print(sum1)
player2="ansh"
sum2= 0
for i in range(5):
  temp=random.randint(1,6)
  print(temp)
  sum2= sum2+temp
print(player2)
print("reaches to")
print(sum2)

if(sum1>sum2):
  print("vaibhav win")
elif(sum1<sum2):
  print("ansh wins")
else:
  print("tie")
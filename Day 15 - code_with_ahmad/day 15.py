import time

tim = time.strftime('%H : %M : %S')
print(tim)

if tim  <= '12:00:00' and tim >= '5:00:00':
  print("Good Morning")

elif tim  <= '18:00:00' and tim > '12:00:00':
  print("Good After Noon")

elif tim  <= '21:00:00' and tim > '18:00:00':
  print('Good Evening')

elif tim  <= '24:00:00' and tim > '21:00:00':
  print("Good Night")

else:
  print("Good Middle Of Night")
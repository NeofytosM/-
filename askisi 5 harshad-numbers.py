k=0
j=0
numbers=[]
number2=0
x=0

sum=0
ginomeno=0
#�� ������� ��� �� 1-10 ����� ���� ������� harshard
for k in range (10):
   if (k<10):
      print k+1

print k
#��� ����  �������� 10 ����� �� 99: ������ �� ����� �������  ��� �� ����� ������� ����� harshard
#�������� ��� ������ ���� �� ������� �� ����� ���
# ����������� �� ����� ��� ��� �� ����� �� �� �������� ��� ������ �� ������
#�� ��������� ���� ����� harshard ������� ��� ���������, �� ��� ���� ��� ����� harshard �������
for k in range (10,99):
   if (k>10 and k<=99):
      a= k/10
      b= k%10
      sum = a+b
   
      if (k%sum==0):
         print k
   
for k in range (100,1000):
   if (k>99):
      
      a= k/100
      x= k%100
      b=x/10
      c=x%10
      sum=a+b+c
  
      if (k%sum==0):
         print k


# epipleon prp na emfanizi tou arithmous pou to ginomeno ton psifiwn tous prp na dierite me ton idio ton arithmo
print " oi arithmoipou dierounte me to ginomeno twn psifiiwn tous"
for j in range (9):
   if (j<10):
      print j+1

print j
for j in range (10,99):
   if (j<=99):
      a= j/10
      if (a==0):
         continue
      b= j%10
      if (b==0):
         continue
      ginomeno= a*b
      if (j%ginomeno==0):
         print j
for j in range (100,1000):
   if (j>99):
      
      a= j/100
      if (a==0) :
         continue
      x= j%100
   
         
      b=x/10
      if (b==0) :
         continue
      c=x%10
      if (c==0):
         continue
      ginomeno=a*b*c
  
      if (k%ginomeno==0):
         print j

       


      
   
   
   
   
 






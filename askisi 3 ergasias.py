numbers = raw_input("ender the data of list").split(",")
board=[]
i=0
count =0
x=123
for i in range(len(numbers)):
   if (numbers[i]=="0"):
         x=numbers[i]
         numbers.remove("0")
         numbers.append(x)
print numbers

       
         

   


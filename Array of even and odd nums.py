#Provide an array of odd and even numbers -> (acceptable input values can be int+str)

list_a = [1,2,"3",5,7,9,"15",6,4,10,"11","0"]
even_num = []
odd_num = []

for i in list_a:
    num = int(i)
    if (num%2==0):
        even_num.append(num)
    else:
        odd_num.append(num)
        
print(even_num)
print(odd_num)
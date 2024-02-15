inp = int(input("Enter the as upper limit for finonacci series: -> "))

num1 = 0
num2 = 1

while(num1 <= inp):
    print(num1, end=" ")

    curr_num = num1+num2
    num1 = num2
    num2 = curr_num
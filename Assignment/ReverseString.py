input_string = input("Enter the string you want to reverse: -> ")


# With inbuilt function
new_input = input_string.split()
# print(" ".join(reversed(new_input)))


#without inbuilt function
stack = []

for i in new_input:
    stack.append(i)

new_stack = []

for i in range(len(stack)):
    new_stack.append(stack.pop())

for i in new_stack:
    print(i, end=" ")
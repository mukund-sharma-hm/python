string = str(input("Enter the String : "))


count = {}

for char in string:
    if(char in count):
        count[char] = count[char] + 1
    else:
        count[char] = 1
# print(count.items())
# print(count.items()[0])

sorted_characters = sorted(count.items(), key=lambda x: x[0])
sorted_count = sorted(sorted_characters, key=lambda x:x[1], reverse=True)

print(sorted_count[:3])

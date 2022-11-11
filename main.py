
def biggest(num1, num2, num3):
    if (num1>=num2) and (num1>=num3):
        largest = num1
    elif (num2>=num1) and (num2>=num3):
        largest =num2
    else:
        largest = num3
    return largest


def testIsBiggest():
    test1 = biggest(15, 45, 30)
    test2 = biggest(100, 50, 10)
    test3 = biggest(1, 2, 3)
    print(test1,  test2,  test3)

testIsBiggest()


#task 5
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[3])


#task 6
i = 1
while i <=10:
    print(i *"*")
    i += 1

#task 7
i = 10
while i >=1:
    print(i *"*")
    i -= 1

#break

while True:
    line = input('Find the secret number, try guessing: ')
    if line == '3':
        break
    print(line)
print('You found it, it was 3!')


# range(start, stop, step)
# stop is required so, range(6) = range(0, 6)
n=5
for i in range(n):
    for j in range(i):
        print ('*', end=" ")
    print('')
for i in range(n):
    for j in range(n - i):
        print ('*', end=" ")
    print('')

#Run-length code decoding

def encode(message):
    encoded_string = ""
    i = 0
    while (i <= len(message)-1):
        '''first while loop is for going through each letter'''
        count = 1
        ch = message[i]
        j = i #assign current letter index to j in order to count the occurrence of letters
        print(ch)
        print('this is j', j)
        print('this is i ', i)
        while (j < len(message)-1):
            if (message[j] == message[j + 1]):
                count = count + 1
                j = j + 1
            else:
                break
            '''the count and the character is concatenated to the encoded string'''
        encoded_string = encoded_string + str(count) + ch
        i = j + 1
    return encoded_string



encoded_message = encode("ABBBBCCCCCCCCAB")
print(encoded_message)

#homework
n=4
while n > 0:
    if n == 4 or n== 1:
        for i in range(4):
            print('*', end="")
        print()
    else:
        for i in range(n):
            for j in range(2):
                print('*', end="  ")
            print()
    n = n-1



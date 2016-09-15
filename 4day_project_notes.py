# input1 = "programming is fun"
# input2 = 'm'
# output= [6, 7]

sentence = "programming is fun"
letter = "m"
output = []


current_location = 0


# enumerate


for current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)
    current_location += 1


# USE IT
# print(sentence.replace(letter, '').index(letter))

#


#


#

print(output)

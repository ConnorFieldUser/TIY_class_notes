# input1 = "programming is fun"
# input2 = 'm'
# output= [6, 7]

sentence = "I decided to learn how to program and it was a good decision"
letter = " "
output = []


# type(enumerate(list))


for current_location, current_letter in enumerate(sentence):
    if current_letter == letter:
        output.append(current_location)


# USE IT
# print(sentence.replace(letter, '').index(letter))

#


#


#

print(output)

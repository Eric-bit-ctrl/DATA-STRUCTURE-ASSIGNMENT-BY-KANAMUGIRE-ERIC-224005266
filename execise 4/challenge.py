
word = "RWANDATECH"
stack = []          # empty stack

# Step 1: Push each letter into the stack

for i in word: # the loop iterates through each letter in the word

    stack.append(i)  # adds each letter to the stack

# Step 2: Pop each letter to form reversed word

reversed_word = "" # empty string to hold the reversed word

while stack:     #the loop continues until the stack is empty

    reversed_word = reversed_word + stack.pop()  # removes the last item from the stack, adds it to reversed_word

print("Original word:", word)
print("Reversed word:", reversed_word)

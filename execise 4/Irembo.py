# Step 1: Initialize stack
stack = [] # empty stack

# Step 2: Push steps
stack.append("Step1")
stack.append("Step2")
stack.append("Step3")

# Step 3: Undo 2 actions
stack.pop()  # removes "Step3"
stack.pop()  # removes "Step2"

# Step 4: Show which step is left
print("Step left:", stack[-1])
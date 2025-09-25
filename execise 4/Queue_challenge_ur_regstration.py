queue = ['Student1', 'Student2', 'Student3']
print('Queue registration order:')
while queue:
    registered = queue.pop(0)  # first student registers first, FIFO shows fairness for those who come first
    print('Registered:', registered)

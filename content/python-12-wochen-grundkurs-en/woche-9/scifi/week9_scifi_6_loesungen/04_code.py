# Problem: cannot read in 'w' mode
with open('test.txt', 'w') as f:
    f.write('Hello')

with open('test.txt', 'r') as f:
    content = f.read()
    print(f'Content: {content}')
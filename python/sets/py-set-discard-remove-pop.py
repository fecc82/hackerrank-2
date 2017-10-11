n = int(input())
s = set(map(int, input().split()))

number_of_commands = int(input())
for i in range(number_of_commands):
    command = input().split(" ")
    if command[0] == 'pop':
        s.pop()
    elif command[0] == 'remove':
        if int(command[1]) in s:
            s.remove(int(command[1]))
    elif command[0] == 'discard':
        s.discard(int(command[1]))

print(sum(s))
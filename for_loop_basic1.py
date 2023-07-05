# Basic
for i in range(151):
    print(i)

# multiples of 5
for i in range(5, 1001, 5):
    print(i)

# counting the dojo way
for i in range(101):
    if i % 5 == 0:
        if i % 10 == 0:
            print("Coding Dojo")
        else:
            print("Coding")
    else:
        print(i)

total = 0
for i in range(500001):
    if i % 2 == 0:
        pass
    else:
        total = total + 1
print(total)

for i in range(2018, 0, -4):
    print(i)

lowNum = 2
highNum = 9
multi = 3
for i in range(lowNum, highNum+1):
    if i % multi == 0:
        print(i)
x = 25 
guess = 3.0 
epsilon = 0.0001

steps = 0 
while abs(guess*guess - x)>= epsilon:
    guess = (guess+x/guess) / 2.0
    steps += 1

print(f"الجذر التقريبي للرقم {x} هو: {guess}")
print(f"عدد الخطوات اللي احتاجتها الخوارزمية: {steps}")
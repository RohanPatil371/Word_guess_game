import random
words=["programmer","computer","mouse","laptop"]
word=random.choice(words)
if word=='programmer':
    print("Hint :a person who designs and writes and tests computer programs")
elif word=='computer':
    print("Hint :Very closed friend of mouse")
elif word=='mouse':
    print("Hint:very closed friend of computer")
userguess=''
chances=10
while chances>0:
    wrongeguess=0
    for i in word:
        if i in userguess:
            print(f"Correct guess")
        else:
            wrongeguess+=1
        if wrongeguess==0:
            print(f"correct word: {word}")
            break
        guess=input("Make a guess ")
        userguess=guess+userguess

        if guess not in word:
            chances-=1
            print(f"Wronge. chances left :{chances}")

            if chances==0:
                print("Game over")

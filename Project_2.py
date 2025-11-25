import random
best_attempts=None
print("Guessing Game")

while True:
    print("\nChoose difficulty:")
    print("1. Easy (1 to 10)")
    print("2. Medium (1 to 50)")
    print("3. Hard (1 to 100)")

    level=input("Enter choice (1/2/3): ")

    if level=="1":
        limit=10
    elif level=="2":
        limit=50
    elif level=="3":
        limit=100
    else:
        print("Invalid choice! Try again")
        continue

    secret=random.randint(1,limit)
    attempts=0

    print(f"\nthinking of a number between 1 and {limit}.")

    while True:
        try:
            guess=int(input("Your guess: "))
            attempts+=1

            if guess<secret:
                print("Higher!")
            elif guess>secret:
                print("Lower!")
            else:
                print(f"Correct! You got it in {attempts} attempts")
                break

        except ValueError:
            print("Enter a number only")
            continue

    if best_attempts is None or attempts < best_attempts:
        best_attempts=attempts
        print("New best score")

    print(f"Best attempts so far: {best_attempts}")

    again=input("\nPlay again? (y/n): ").lower()

    if again!="y":
        print("Thanks for playing")
        break
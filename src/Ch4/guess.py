min, max = 1, 26
while True:
    guess = (min + max) // 2
    ans = input(f"Is your number {guess} (y,h,l)?")
    if ans.lower() == 'y':
        print("Got it!")
        break
    elif ans.lower() == 'l':
        min = guess
    elif ans.lower() == 'h':
        max = guess
    else:
        print("Invalid response")   
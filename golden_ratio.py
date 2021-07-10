GOLDEN_RATIO = (1 + 5 ** 0.5) / 2

operation = input(
    "\n(1) - get the lower value\n(2) - get the higher value\n(3) - get the two values by total\n\nInsert the operation number: ")

if operation == "1":

    higher = (int)(input("Higher value: "))
    lower = (GOLDEN_RATIO * higher) - higher
    print(f"Your lower value is: {lower}")

elif operation == "2":

    lower = (int)(input("Lower value: "))
    higher = GOLDEN_RATIO * lower
    print(f"Your higher value is: {higher}")

else:

    total = (int)(input("Total value: "))
    higher = total / GOLDEN_RATIO
    lower = (GOLDEN_RATIO * higher) - higher
    print(f"\nYour values are \nHigher: {higher}\nLower:{lower}\n")

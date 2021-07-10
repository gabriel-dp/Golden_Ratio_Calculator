GOLDEN_RATIO = (1 + 5 ** 0.5) / 2

operation = input(
    "\n(1) - descobrir menor valor\n(2) - descobrir maior valor\n(3) - descobrir os valores pelo total\n\nInsira o número da operação: ")

if operation == "1":

    higher = (int)(input("Maior valor: "))
    lower = (GOLDEN_RATIO * higher) - higher
    print(f"sua menor medida deve ser: {lower}")

elif operation == "2":

    lower = (int)(input("Menor valor: "))
    higher = GOLDEN_RATIO * lower
    print(f"sua maior medida deve ser: {higher}")

else:

    total = (int)(input("Total da soma: "))
    higher = total / GOLDEN_RATIO
    lower = (GOLDEN_RATIO * higher) - higher
    print(f"\nsuas medidas devem ser... \nmaior: {higher}\nmenor:{lower}\n")

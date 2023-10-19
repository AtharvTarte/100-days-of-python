print("welcome to the tip calculator\n")
a = int(input("what is your total bill\n"))
b = int(input("what percentage tip you want to give 10 , 15 or 20 \n"))
c = int(input("how many people to split the bill\n"))
d = a*b/100
print(f"the bill for per person is{d/c}")
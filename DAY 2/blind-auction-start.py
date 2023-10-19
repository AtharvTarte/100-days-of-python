
print("WELCOME TO THE AUCTION\n")

a = {}

name = input("WHAT IS YOUR NAME\n")
bid = int(input("WHAT IS YOUR BID IN $\n"))

a[name] = bid

def highest_bidder(a):
    b = 0
    name1 = "abc"
    for name in a:
        if a[name] > b:
            b = a[name]
            name1 = name
    print(f"HIGHEST BIDDER IS {name1} AND BID IS {b}$")


end_auction = False
while end_auction == False:
    b = input("Are there any other bidders ? \ntype Yes or No\n")
    if b == "No":
        highest_bidder(a = a)
        end_auction = True
    else:
        name = input("WHAT IS YOUR NAME\n")
        bid = int(input("WHAT IS YOUR BID IN $\n"))
        a[name] = bid



        

    

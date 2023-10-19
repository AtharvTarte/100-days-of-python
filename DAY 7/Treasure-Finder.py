print(""" Welcome to Treasure Island.
Your mission is to find the treasure.
          .--,_
        ['    '\.
         \       `''|
         |         ,]
          `._      ].
            |     \
          _/       -'\
         ,'          ,'
       _/'          \                     ,..-''L_
  |--''              '-;__        |\     /      .,'
   \                      `--.__,'_ '----     ,-'
   `\                             \`-'\__    ,|
,--;/                             /     .| ,/
\__                               '|    /  / 
  ./  _-,                         _|   S@yaN
  \__/ /                        ,/        "
       |                      _/
       |                    ,/
       \                   /
        |              /.-'
         \           _/                   :
          |         /                      .
           |        |                     .
      .    |        |                     '.
      ;     \       /                     ;\
      '      |     |                
             \    _|                      : 
              \_,/                         "'
                                          : '
                                             '
""")

a = input("YOU WANT TO GO LEFT OR RIGHT\nChoose from L or R\n")
if a == "L":
    b = input("swim or wait\n")
    if b == "wait":
        c = input("Which door?\nRed , Blue or Yellow\n")
        if c == "Red":
            print("Burned by fire.\nGame Over")
        if c == "Blue":
            print("Eaten by beasts.\nGame Over.")
        else:
            print("YOU WIN")
    else:
        print("GAME OVER")
else:
    print("GAME OVER")


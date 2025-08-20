print("Battleship Game")
print("Welcome to this game")

#ทำงานซ้ำ
while True:
    ships_board = [['O'] * 10 for _ in range(10)]

    board_to_print = ships_board
        
    print("  " + " ".join("ABCDEFGHIJ"))
    for i, row in enumerate(board_to_print):
        print(f"{i+1:<2}" + " ".join(row))
        

    print("if you want to quit please input -Quit-")
    command = input("\n> ").lower()
    
    if command == 'quit':
        print("ลาก่อน! นะครับ")
        break
    else:
        print("คำสั่งไม่ถูกต้อง กรุณาลองใหม่อีกครั้ง")


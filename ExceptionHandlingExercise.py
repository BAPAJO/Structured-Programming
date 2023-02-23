def game():
    ans = 0
    a = 0
    b = 0
    while ans >= 0:
        try:    
            a = int(input("Enter your number: "))
            b += a
            ans += 1
        except ValueError:
            print("The number must be an integer")
        answer = input("Do you wish to enter another number? (y/n) ")
        if answer == "n":
            break
    avg = b / ans               
    print(avg)         
game() 

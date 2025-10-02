print("Welcom to my program")
user_input = int(input("Enter a nubmer: "))
def even_or_not(user_input):
    if user_input % 2 == 0:
        print("It's a even number.")
        print("It's divisible by 2")
    else:
        print("It's a odd number")
        print("It's not divisible by 2")

even_or_not(user_input)
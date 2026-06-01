# ✅↓ Write your code here ↓✅
def number_of_bottles():
    milk = 99
    while milk != 1:
        print(f"{milk} bottles of milk on the wall, {milk} bottles of milk. \nTake one down and pass it around, {milk-1} bottles of milk on the wall.")
        milk -= 1
    print("1 bottle of milk on the wall, 1 bottle of milk.\n" \
    "Take one down and pass it around, no more bottles of milk on the wall.\n" \
    "No more bottles of milk on the wall, no more bottles of milk.\n" \
    "Go to the store and buy some more, 99 bottles of milk on the wall.")

number_of_bottles()


import os

os.system("clear")

x = int(input("Enter an integer: "))

if x > 1000:
    print("Number greater than 1000, terminating program")
    exit()

print("\n")

def my_function(x):
    for i in range(1, x+1):
        print(f"This is line number {i}")

my_function(x)

# Some comments go here

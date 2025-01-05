# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!

def palindromes(slowo):
    return slowo == slowo[::-1]

def main():
    while True:
        slowo = input("Please type in a palindrome: ")
        if palindromes(slowo):
           print(f"{slowo} is a palindrome!")
           break
        else:
            print("that wasn't a palindrome")

main()

if __name__ == "__main__":
    palindromes()
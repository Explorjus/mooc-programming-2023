# Write your solution here

liczba = int(input("Please type in a positive integer:"))

for i in range(liczba * -1, liczba + 1):
    if i != 0:
        print(i)
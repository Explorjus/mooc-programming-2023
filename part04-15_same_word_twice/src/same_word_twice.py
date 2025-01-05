# Write your solution here
lista = []
liczba_wpisanych_slow = 0

while True:
    word = input("Word: ")
    lista.append(word)
    liczba_wpisanych_slow += 1
    
    if word in lista and lista.count(word) > 1:
        print("You typed in", liczba_wpisanych_slow - 1, "different words")
        break


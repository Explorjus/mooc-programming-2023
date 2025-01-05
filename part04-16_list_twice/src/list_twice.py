# Write your solution here
lista = []

while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break
    lista.append(item)
    w_kolejnosci = sorted(lista)
    print("The list now:", lista)
    print("The list in order:", w_kolejnosci)









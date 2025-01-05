# Write your solution here
lista = []
num = 1
print("The list is now", lista)
while True:
    wej = input("a(d)d, (r)emove or e(x)it: ")

    if wej == "d":
        lista.append(num)
        print("The list is now", lista)
        num += 1
    
    if wej == "r" and len(lista) > 0:
        lista.pop()
        print("The list is now", lista)
        num -= 1

    if wej == "x":
        print("Bye!")
        break
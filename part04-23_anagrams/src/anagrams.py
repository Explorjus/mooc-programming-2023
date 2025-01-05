# Write your solution here


def anagrams(slowo1, slowo2):
    sort1 = sorted(list(slowo1))
    sort2 = sorted(list(slowo2))


    return sort1 == sort2

if __name__ == "__main__":
    print(anagrams("house", "esuoh"))


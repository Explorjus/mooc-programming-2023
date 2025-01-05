# Write your solution here
def mean(my_list):
    
    suma = sum(my_list)
    ilosc = len(my_list)
    
   
    return  suma / ilosc



# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3]
    result = mean(my_list)
    print(result)
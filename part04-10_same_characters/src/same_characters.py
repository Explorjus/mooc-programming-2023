# Write your solution here
def same_chars(string, a, b):

    if string[a] == string[b]:
       
        return True
    
    
    if string[a] or string[b] > len(string):
       
        return False
    
   
       
    else:
      
        return False
    
        
    






# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))
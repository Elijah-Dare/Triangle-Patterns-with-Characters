def print_word_pattern(word):
    """
        This is a fuction that takes in a word parameter  and prints out the iterated words 
    """
    length  = len(word) # This calculate the length of the word and stores it in the length variable
    for i in range(1, length + 1): # This iterated through the value of the word inputted by the user
        for j in range(i): # This iterated through each value of the outer loop
            char = word[j] # This checks the index of the each character in the word entered by the user 
                           # and stores it inside the variable char
            print(char, end=" ") # This prints the *char* variable and adds a space after each character is printed
            
        print() # This prints a newline after each row is printed
        
user_word = input("Enter a word: ").upper() # This takes the input from the user and converts it to uppercase character
print_word_pattern(user_word) # The function is called and the user_word variable is passed into it


            
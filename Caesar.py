# The alphabet we are using for the Caesar Cipher, along with the length.
#   They are both variables. It is common to make the names of variables that
#   don't change, or /constant/ variables, all caps.
#
#   !!! Do not change any variable that is in all caps. !!!
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALPHABET_LENGTH = 26

# Label for "SHIFT"
LABEL_SHIFT = Label("SHIFT", 200, 50, size=40)

# Label for the current shift amount. The original Caesar Cipher used 3.
shift_amount = Label(3, 200, 95, size=30)

# Labels for "ORIGINAL LETTER" and "SHIFTED LETTER"
LABEL_CURRENT_LETTER = Label("ORIGINAL LETTER", 100, 150, size=18, fill="mediumSlateBlue")
LABEL_SHIFTED_LETTER = Label("SHIFTED LETTER", 300, 150, size=18, fill="paleVioletRed")

# Label for original letter and shifted letter
# !!! These are the variables you will be modifying. !!!
original_letter = Label("A", 100, 200, size=50, fill="mediumSlateBlue")
shifted_letter = Label("C", 300, 200, size=50, fill="paleVioletRed")


# !!! WRITE CODE BELOW !!!

def caesarCipher(char, shift):
    # Makes the character upper case, if not already. Will throw error if the
    #   character is not a letter.
    char = char.upper()
    
    ### Part 1 ###
    # Set the original_letter label to the character held in char
    
    
    
    ### Part 2 ###
    # Find the position of the letter held by char inside ALPHABET and save it to
    #   a variable named original_position.
    #   HINT: Use the find() function.
    
    
    
    ### Part 3 ###
    # Add 3 to original_position for the shift, and save it to a new variable
    #   called shifted_position.
    
    
    
    ### Part 4 ###
    #  Use shifted_position to retrieve a letter from ALPHABET using the index
    #   operators: [], and save it variable named shifted_char.
    #  Example with number: shifted_character = ALPHABET[4]
    #   --> What would change if you wanted to use the shifted position instead?
    
    
    ### Part 5 ###
    # Change the shifted_letter label's value to match the the letter held in 
    #   shifted_char.
    
    
    
    pass
    

caesarCipher("A", 3)

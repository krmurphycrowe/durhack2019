import random, re

uwuDict = {
    "r" : "w",
    "l" : "w",
    "!" : "! :3",
    "R" : "W",
    "L" : "W"
}

vowels = ("a", "e", "i", "o", "u")

def uwuMe(message):
    """Takes string 'message' and returns the message in uwu form."""
    table = message.maketrans(uwuDict) # Creates translation table from dictionary
    reurl = re.search("https:[^ ]*",message)
    url = ""
    if reurl != None:
        url = reurl.group(0)
        message = message.replace(url,"")
    firstpass = message.translate(table) # Applies translation table to first pass
    secondpass = ""
    j = len(firstpass)-1
    i = 0
    while i <= j: # Iterates from the start to the end of the firstpass
        if i == j: # If we're at the end, we can't apply any multi-char translations
            secondpass += firstpass[i] # So just copy over the character
            i += 1
        elif firstpass[i].lower() == "n" and firstpass[i+1] in vowels: # If we have an n followed by a vowel
            secondpass += firstpass[i] + "y" + firstpass[i+1] # Insert a y in the middle
            i += 2 # Skip over the vowel since we've already added it
        elif i < j - 1 and firstpass[i:i+3].lower() == "ove": # If we have "ove"
            secondpass += "uv" # Replace with "uv"
            i += 3 # Skip over the whole sequence
        else: # Otherwise
            secondpass += firstpass[i] # Copy over the character
            i += 1
    thirdpass = ""
    if random.randrange(2): # 50% chance
        thirdpass += "UwU... " + secondpass # uwu goes before
    else:
        thirdpass += secondpass + " UwU" # uwu goes after
    return thirdpass + " " + url # Return the result

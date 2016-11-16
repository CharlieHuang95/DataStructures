# Global variables

LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def my_length(s):
    '''(str) --> (int)
    Given a string input, return the length of the string.
    '''
    
    new = "" #New Empty String
    count=0
    while new != s: #This loop ends when the New String is identical to the inputted one.
        new += s[count:count+1] #Adds characters in increments of 1.
        count += 1
    return count
        

def my_count(s, char):
    '''(str, str) --> (int)
    Given a string input and a character, return the number of occurrences
    of the character in the string.
    '''
    
    count = 0
    a = 0
    for i in s: #Loop reiterates for every character in the string.
        if s[a] == char: #Determines if selected character is in string.
            count += 1
        a += 1
    return count

def my_find(s, char):
    '''(str, str) --> (int)
    Given a string and a character, determine whether the character is in
    the string and index the position of the character within the string.
    '''
    
    b = 0
    while s[b] != char: #While loop stops when the character is found.
        b += 1
        if b >= my_length(s): #If statement ensures that the function can determine that char is not part of s.
            return -1
    return b
      
def my_lstrip(s, char):
    '''(str, str) --> (str)
    Given a string and a character, return a string without any leading
    occurences of the character.
    '''
    
    count = 0
    while s[count] == char: #Count the number of leading occurences before a character is different.
        count += 1     #Check the first, if the same, moves on. Count is kept.
    return s[count:]

def my_rstrip(s, char):
    ''' (str, str) --> (str)
    Given a string and a character, return a string without any trailing
    occurences of the character.
    '''
    
    count = my_length(s)
    while s[count-1] == char: #Count the last string character and determines if it is correct.
        count -= 1    #Check the second last and moves backwards. Count is kept.
    return s[:count]

def my_strip(s, char):
    ''' (str, str) --> (str)
    Given a string and a character, return a string without any leading
    or trailing occurences of the character.
    '''
    return my_rstrip((my_lstrip(s,char)),char) #Combines my_lstrip and my_rstrip.
    
def my_lower(s):
    ''' (str) --> (str)
    Given a string, return the string with all lowercase letters.
    '''
    
    count = 0
    new = ""
    while count < my_length(s):
        if my_count(UPPER,s[count]) != 0: #If letter is not part of the lower group.
            c = my_find(UPPER,s[count]) #Finds the index of the letter in upper group.
            new += LOWER[c]
        else:
            new += s[count]
        count += 1
    return new
 
def my_upper(s):
    ''' (str) --> (str)
    Given a string, return the string with all uppercase letters.
    '''
    
    count = 0
    new = ""
    while count < my_length(s):
        if my_count(LOWER,s[count]) != 0: #If letter is not part of the lower group.
            c = my_find(LOWER,s[count]) #Finds the index of the letter in upper group.
            new += UPPER[c]
        else: #Adds upper case letter or special character to New String normally.
            new += s[count]
        count += 1
    return new

def my_replace(s, char1, char2):
    ''' (str, str, str) --> (str)
    Given s, char1, char2, return a new string with all occurrences
    of char1 replaced with char2 in s.
    '''
    
    new = ""
    count = 0
    while count <= my_length(s):
        if s[count-1:count] == char1: #If char1 is found, char2 is added to the new string.
            new += char2
        else:
            new += s[count-1:count] #If char1 is not found, another character is added like normal.
        count += 1
    return new

def my_startswith(s1, s2):
    ''' (str, str) --> (bool)
    Given s1 and s2, return True if and only if s1 starts with s2.
    '''
    a = my_length(s2)
    return s2 == s1[0:a] #Checks to see if the beginning of s1 is the same as s2.

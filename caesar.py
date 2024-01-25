#!/usr/bin/env python
"""
SYNOPSIS

    Caesar.py
    No command line arguments involved.

DESCRIPTION

    Enter a plaintext message and then the rotation key. The
    plaintext is then converted to cypher text and saved to a file.

EXAMPLES

    User enters 'Hello!' and a key of 13.
    Output should give 'Uryyb!' and write it to a file.

AUTHOR

    Joe Blog <jblogs@TMC.org>

LICENSE

    This script is in the public domain, free from copyrights or
    restrictions.

VERSION

    0.2
"""
## Scenario 2 Code ##


# Caesar cypher function
def rot(text, key):

    # Iterate through each character in the message.
    for char in text:
        # Set cypher_text to an empty string to add to later
        cypher_text = ''
        # Check if the character is a letter (A-Z/a-z).
        if char.isalpha():
            # Get the Unicode number from of the character.
            num = ord(char)
            # If the final number is greater than 'z'/122..
            if (num + key) > 122:
                # If we go too far, work out how many spaces passed
                # 'a'/97 it should be using the proper key.
                x = (num + key) - 122
                # Add the chr version of x more characters passed
                # 'a'/97, take 1 to account for the 'a' position.
                # This adds a string character on to the cypher_text
                # variable.
                cypher_text += chr(x + ord('a') - 1)
            # If the rotated value doesn't go passed 'z'/122
            elif ((num + key <= 122)):
                # Use the key to add to the decimal version of the
                # character, add the chr version of the value to the
                # cypher text.
                cypher_text += chr(num + key)
        # Else, if the chracter is not a letter, simply add it as is.
        # This way we don't change symbols or spaces.
        else:
            cypher_text += char
    # Return the final result of the processed characters for use.
    return cypher_text


# Ask the user for their message
plain_input = input('Input the text you want to encode: ')
# Aks the user for the rotation key
rot_key = int(input('Input the key you want to use from 0 to 25: '))
# Secret message is the result of the rot function
secret_message = rot(plain_input, rot_key)
# Print out message for feedback
print('Writing the following cypher text to file:', secret_message)
# Write the message to file
with open('TestFile.txt', 'a+') as file:
    file.write(secret_message)

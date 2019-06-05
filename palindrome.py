import re
 
user_input = input("What is your single word text for palindrome test? \n ")
user_input = re.sub((r'[^A-Za-z]'), "", user_input)
text = user_input.lower() 
#print (text)
rtext = user_input[::-1]
#print (rtext)

if (text == rtext):
        print(user_input, "is palindrome")
else:
        print(user_input, "is not palindrome")

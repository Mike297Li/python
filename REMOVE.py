import string

str_input = 'Display ? the word Word to ! the user in a readable format, sorted : alphabetically'

# Create a translation table with all punctuation marks set to None
translator = str.maketrans('', '', string.punctuation)

# Use translate() to remove punctuation marks
str_output = str_input.translate(translator)

print(str_output)

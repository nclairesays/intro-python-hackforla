# STRINGS
# https://docs.python.org/3/tutorial/introduction.html#strings

s = str(42)

s  # convert another data type into a string (casting) -- casting coverts the type

s = 'I like you'

# examine a string
s[0]  # returns 'I'

len(s)  # returns 10, including white space characters

# string slicing like lists
s[0:7]  # returns 'I like '

# print(repr(s[0:7]))         #repr() -- see what the computer will see, so this will include the white space.
# help(repr)                  # "Return the canonical string representation of the object.""

s[6:]  # returns 'you'

s[-1]  # returns 'u'   # negative index, going backwords



# EXERCISE: Extract State from Addresses (Part 1)
# 1) Extract the state abbreviation from the string
# 2) Save each state abbreviation to a variable (ie state_one)
# Hint: {City}, {State Abbrev} {ZipCode}

address_1 = "Austin, TX 78701"
address_2 = "Washington, DC 20001"
address_3 = "North Hollywood, CA 91601"



state_one = address_1[-8:-6]
state_two = address_2[-8:-6]
state_three = address_3[-8:-6]

print(state_one)


# STRINGS - Part II

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)  # same thing

# split a string into a list of substrings separated by a delimiter
s = 'I like you'
s.split(' ')        # returns ['I','like','you']
s.split()           # same thing

# another example: split a string into a list of substrings separated by a delimiter
address = 'Toluca Lake, CA 91602'
address.split(',')        # returns ['Toluca Lake',' CA 91602']
address.split()           # ['Toluca', 'Lake', 'CA', '91602' ]


## Learn more with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/
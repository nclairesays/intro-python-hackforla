## Learn More Python with Automate the Boring Stuff:
## https://automatetheboringstuff.com/chapter1/

# Your First Program
#
print('hello world')
#
# # Comments in python use a '#'

## WARM UP QUIZ

# PART I
a = 5           # integer, positive or negative
b = 5.0         # float, floating point, decimal
c = a / 2       
d = b / 2

# What is type(a)?

print(type(a))

# What is type(b)?
print(type(b))


# What is c?
print("c is:", c)


# What is d?
print(d)



# EXERCISES

e = [a, b]
f = list(range(0, 10))

# What is type(e)?

print(type(e))      #list

# What is len(e)?
print(len(e))       #length


# What is type(f)?
print(type(f))      #list


# What are the contents of f?
print(f)            # [0..9] # range(0,10) -- last number is not included 
                    # range is a generator



# What is 'list()' called? # hint: google it
print(type(list()))   #type is still list; it's a function


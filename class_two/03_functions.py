
# FUNCTIONS
# how to you know the block is associated with the function with throu
# indentation -- use 4 spaces NOT tab

# A function is like a mini-program within a program.
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')

# Can you run the function hello()?

hello()



# FUNCTION PARAMETERS
# A function that uses the parameter / input

def hello_friend(name):
    print('Howdy, ' + name)


# A function with two parameters and returns a string

def make_fullname(first_name, last_name):
    return first_name + ' ' + last_name


## FUNCTIONS with Conditionals

def hello_new_friend(name):

    if name == 'Nathan':
        print('Hey Nate')
    else:
        print('Hey', name)

hello_new_friend("Naan")


### Exercise:
# Write a function named "learning_programming()"
# Takes two parameters: your name and the language you are learning
# It prints out the following message:
# "My name is {name} and I am learning {language}."

## Bonus -- if you are learning 'python', then it prints out 'This is cool!'


def learning_programming(name, language):
    #print("My name is {name} and I am learning {language}")
    #print("My name is {} and I am learning {}").format(name, language)
    # print("My name is " + name + " I am learning" + language)
    if language == "python":
        # print("My name is " + name + " I am learning " + language)
        print("This is cool! You're learning Python")
    else:
        print("My name is" + name + " I am learning" + language)
    

learning_programming('claire', 'python')

print([1, 2, 3])

### Learn More About Functions
# https://automatetheboringstuff.com/chapter3/
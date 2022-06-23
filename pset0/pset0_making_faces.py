# https://cs50.harvard.edu/python/2022/psets/0/faces/ ************* Click for the Question! 

def main():
    msg =  input("Hi! What would you like to say? ")    #Get input from the user
    converted_msg = convert(msg)    #calling the function
    print(converted_msg)    #print the result

def convert(msg):
    converted_msg_1 = msg.replace(":)", "🙂")    # Replacing :) for the happy emoji
    converted_msg_2 = converted_msg_1.replace(":(", "🙁")   # Replacing :( for the sad emoji)
    return converted_msg_2 # returning the converted string

main()
# https://cs50.harvard.edu/python/2022/psets/1/deep/ ************* Click for the Question! 

answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ") # Get the user input
if answer.strip() == "42":
    print("Yes")  # Print Yes if the user inputs 42, forty two or forty-two
elif answer.lower().strip() == "forty-two":
    print("Yes")
elif answer.lower().strip() == "forty two":
    print("Yes")

else:
    print("No")  # Output No if no form of 42 is detected

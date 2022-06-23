# https://cs50.harvard.edu/python/2022/psets/1/bank/#home-federal-savings-bank ************* Click for the Question!

answer =  input("Greeting: ")# Get the user input
clean_answer = answer.lower().strip()
if "hello" in clean_answer:    # Checking if the answer is "Hello" (Case Insensitive) or not, if yes, then = 0$ print
    print("$0")
elif "h" in clean_answer[0]:
    print("$20")
else:
    print("$100")   # Otherwise, we will print $100
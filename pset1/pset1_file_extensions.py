# https://cs50.harvard.edu/python/2022/psets/1/extensions/ ************* Click for the Question! 

file_name = input("File name: ")    # Get user input
clean_file_name = file_name.lower().strip() # Clean the Input
if ".gif" in clean_file_name: # If gif or png or jpeg or jpg, print "image/extension"
    print("image/gif")
elif ".png" in clean_file_name:
    print("image/png")
elif ".jpg" in clean_file_name:
    print("image/jpeg")
elif ".jpeg" in clean_file_name:
    print("image/jpeg")
elif ".pdf" in clean_file_name: # If pdf or zip, print "application/extension"
    print("application/pdf")
elif ".zip" in clean_file_name:
    print("application/zip")
elif ".txt" in clean_file_name: # If txt, print "text/plain"
    print("text/plain")
else:
    print("application/octet-stream")   # If nothing, print "Application/octet-stream"
# File Extensions

file_name = input("What is the name of the file: ")

if file_name.endswith(".gif"):
    print("image//gif")
elif file_name.endswith(".jpg"):
    print("image//jpg")
elif file_name.endswith(".jpeg"):
    print("image//jpeg")
elif file_name.endswith(".png"):
    print("image//png")
elif file_name.endswith(".pdf"):
    print("appplication//pdf")
elif file_name.endswith(".txt"):
    print("text//plain")
elif file_name.endswith(".zip"):
    print("application//zip")
else:
    print("aplication//octet-stream")
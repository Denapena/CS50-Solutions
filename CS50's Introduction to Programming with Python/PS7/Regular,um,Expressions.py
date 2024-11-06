def count(text):
    text = text.lower()
    count = 0
    for i in range(len(text)):
        if text[i] == "u":
            if len(text) >= i+2:
                if text[i+1] == "m":
                    if len(text) >= i+3:
                        if not text[i+2].isalpha():
                            if 0 <= i-1:
                                if not text[i-1].isalpha(): 
                                    count += 1
                            else:
                                count += 1
                        else:
                            if 0 <= i-1:
                                if not text[i-1].isalpha(): 
                                    count += 1
                    else:
                        if 0 <= i-1:
                            if not text[i-1].isalpha(): 
                                count += 1
                        else:
                            count += 1
    return count


print(count("um"))
print(count("um?"))
print(count("Um, thanks for the album."))
print(count("Um, thanks, um..."))
print(count("u"))
print(count("Umum"))
print(count("mUm, u m  .um  um?  dum mum"))


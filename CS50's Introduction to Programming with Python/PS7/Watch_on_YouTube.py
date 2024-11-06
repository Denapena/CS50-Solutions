import re


def parse(html):
    if x:= re.search(r"^<iframe src=\"https?://www\.youtube\.com/embed/([a-zA-Z0-9]{11})\"></iframe>$",html):
        url = x.group(1)
        return f"URL: https://youtu.be/"+url
    else:
        return "Invalid."

while True:
    html = input("URL: ")  
    print(parse(html))
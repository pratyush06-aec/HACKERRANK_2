import textwrap

def text_wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width= str(input()), int(input())

print(text_wrap(string, max_width))
def cap_text(text):
    return text.capitalize()

def cap_each(text):
    return text.title()


if __name__ == '__main__':
    print(cap_text("python"))
    print(cap_each("python file"))
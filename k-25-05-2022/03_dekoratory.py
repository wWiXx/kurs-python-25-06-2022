from functools import wraps

text = "Ala ma kota"
text2 = "Ala nie ma żadnego kota"


def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"

    return wrapper


@bold
def paragraph(text):
    return f"<p>{text}</p>"


@bold
def paragraph2(text2):
    return f"<p>{text2}</p>"


print(paragraph(text))
print(paragraph2(text2))

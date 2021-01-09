#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Arguments:
    text: string
    Return:
    text indentation
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    s = [".", "?", ":"]

    for n in s:
        if n in text:
            text = text.replace(n, n + "\n\n\a")
    print("\n\n".join([x.strip() for x in text.split("\a")]), end="")

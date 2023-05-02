import re,os


def ab_with_check(text):
    for ch in ['\\', '`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#', '+', '-', '.', '!', '$', '\'', '】', '/']:
        if ch in text:
            text = text.replace(ch, " ")
    return text

zz = "संस्कारी[( बहू/पत्नी/भाभी/मां)दूसरों का बिस्तर गरम करने वाली】"
print(zz)
story_title = ab_with_check(zz)
print(story_title)


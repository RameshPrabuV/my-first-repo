
import re

def matching_pattern():
    text1 = "The quick brown fox"
    pattern1 = r"quick"

    match1 = re.match(pattern1, text1)
    if match1:
        print("Match found:", match1.group())
    else:
        print("No match")

def searching_pattern():
    text2 = "The quick brown fox"
    pattern2 = r"brown"

    search1 = re.search(pattern2, text2)
    if search1:
        print("The search word found", search1.group())
    else:
        print("Not found")

def replace_pattern():
    text3 = "The quick brown fox surrounded by 10 brown dogs"
    pattern3 = r"brown"
    replace_word = "red"

    new_text = re.sub(pattern3, replace_word, text3)

    print("The new text is", new_text)

def splitting():
    text4 = "banana;apple,orange.strawberry/pineapple mango"
    pattern4 = r"[;,./: ]"

    splitting_word = re.split(pattern4, text4)

    print("The splitted list of fruits:", splitting_word)


matching_pattern()
searching_pattern()
replace_pattern()
splitting()





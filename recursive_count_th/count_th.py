'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    if len(word) < 2:  # If the word length is less than 2, having "th" isn't possible
        return 0  # so return 0
    if word[:2] == "th":  # if the first 2 letters are th
        return 1 + count_th(word[2:])  # add 1 to the count and move to index 2
    else:  # if the first 2 letters aren't th
        # don't add to the count and continue to next letter
        return 0 + count_th(word[1:])


print(count_th("ththfhtbhhtht"))

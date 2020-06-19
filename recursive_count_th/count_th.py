'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    substring = "th"
    wl = len(word)
    sl = len(substring)
    if wl == 0 or wl < sl:
        return 0
    if word[0:sl] == substring:
        return count_th(word[sl - 1:]) + 1
    return count_th(word[sl-1:])

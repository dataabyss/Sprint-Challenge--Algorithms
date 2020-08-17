'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word = list(word)
    count = 0
    if len(word) < 2:
        return count
    elif ''.join(word)[0:2] == 'th':
        count += 1
        del word[0:2]
        print(count)
        count_th(word)
    else:
        del word[0:2]
        count_th(word)
    return count

print(count_th('the'))
    

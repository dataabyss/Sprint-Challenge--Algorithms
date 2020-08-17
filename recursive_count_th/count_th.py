'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    word = list(word)
    count = 0
    while len(word) > 1:
        if ''.join(word)[0:2] == 'th':
            count += 1
            del word[0:1] # delete first letter instead of first two
            # print(count)
            count_th(word)
        else:
            del word[0:1]
            count_th(word)
    return count

print(count_th('the'))
    

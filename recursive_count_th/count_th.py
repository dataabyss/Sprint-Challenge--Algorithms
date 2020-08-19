'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# def count_th(word):
#     word = list(word)
#     count = 0
#     while len(word) > 1:
#         if ''.join(word)[0:2] == 'th':
#             count += 1
#             del word[0:1] # delete first letter instead of first two
#             count_th(word)
#         else:
#             del word[0:1]
#             count_th(word)
#     return count

# print(count_th('thethethth'))

def count_th(word):
    
    word_list = list(word)
    count = 0
    while len(word_list) > 1:
        if ''.join(word_list)[0:2] == 'th':
            count += 1
            del word_list[0:1] # delete first letter instead of first two
            count_th(word_list)
        else:
            del word_list[0:1]
            count_th(word_list)

    word_list = list(word)
    count2 = 0
    while len(word_list) > 1:
        if ''.join(word_list)[0:2] == 'TH':
            count2 += 1
            del word_list[0:1] # delete first letter instead of first two
            count_th(word_list)
        else:
            del word_list[0:1]
            count_th(word_list)            
            
    return count
           # f'"th" appears {count} time(s) in "{word}"\n' \
           # f'"TH" appears {count2} time(s) in "{word}"'            

print(count_th('THthththTH'))
    

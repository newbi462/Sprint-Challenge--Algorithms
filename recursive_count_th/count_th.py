'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = [0]
    if len(word) == 0:
        return 0
    else:
        def recursion(new_word):
            if new_word.find('th') < len(new_word):
                #print(new_word[new_word.find('th')])
                #print(f"word before:{new_word}")
                #print(new_word.replace("th", ""))
                new_word2 = new_word.replace("th", "", 1) # need dif mem
                print(f"word after:{new_word2}")
                count[0] += 1
                if new_word2.find('th') > new_word.find('th'):
                    print(f"count[0]:{count[0]}")
                    recursion(new_word2)
            #count[0] = word.find('th')


    # TBC
    #count = len(word)
    #count = word.find('th')

    #count = count + count_th(word)
    recursion(word)
    return count[0]

print(count_th("abcthefthghith"))

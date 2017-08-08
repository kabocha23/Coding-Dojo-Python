def findChar(lst,chr):
    new_list = []
    for text in lst: 
        if chr in text:
            new_list.append(text)
    print new_list

word_list = ['hello','world','my','name','is','Anna']
char = 'o'

word_list2 = ['who','what','when','where','how','why']
char2 = 'w'

findChar(word_list2,char2)
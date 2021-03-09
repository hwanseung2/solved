N = int(input())
if N >= 1 and N<=20000:
    list_ = []
    for n in range(N):
        string = str(input())
        string_count = len(string)
        list_.append((string,string_count))
    #print(list_)
    list_ = list(set(list_))
    new_list=[]
    for word, word_cnt in list_:
        new_list.append((word_cnt, word))
    new_list.sort()
    for i in new_list:
        print(i[1])

 



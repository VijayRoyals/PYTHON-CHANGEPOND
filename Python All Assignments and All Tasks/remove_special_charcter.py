def filtering(single_course):
    special_Char = ['!','@','#','$','%','^','&','*','(',')','-','_','/','?','~',',','<','>','.',':',';','\'','\"','+','=','[',']','{','}']
    ans = ""
    for ch in single_course:
        if ch not in special_Char:
            ans += ch
    return ans
def main():
    course = ['','Python','java',',,','angul:ar','php']
    remove_list = list(map(filtering,course))
    #remove_list = list(filter(filtering,course))
    remove_list = list(filter(None, remove_list))
    print(remove_list)
if __name__ == '__main__':
    main()


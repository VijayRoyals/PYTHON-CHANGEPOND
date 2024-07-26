def numbers(single_id):
    ans = ""
    number = '0123456789'
    for ch in single_id:
        if ch in number:
            ans += ch
    return ans
def main():
    product_id = ['HEM-234','HEM-123','HEM-566']
    remove_list = list(map(numbers,product_id))
    print(remove_list)
if __name__ == '__main__':
    main()
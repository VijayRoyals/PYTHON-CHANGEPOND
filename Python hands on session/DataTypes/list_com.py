num= int(input("Enter number : "))

def square_numbers(num):
    ans=[]
    for i in range(1,num+1):
        ans.append(i*i)
    print(ans)
if __name__ == "__main__":
    square_numbers(num)
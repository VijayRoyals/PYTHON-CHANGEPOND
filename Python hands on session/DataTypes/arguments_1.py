# Area of Circle = PI*Radius*Radius

def AreaOfCircle(Radius,PI=3.14):
    Result = PI*Radius*Radius
    return Result

def main():
    # Positional Argument
    output_1 = AreaOfCircle(10,12)
    print(output_1)

    # first arguments is posional and Default
    output_1 = AreaOfCircle(10)
    print(output_1)

    # Keyword Argument
    output_2 = AreaOfCircle(Radius=10)
    print(output_2)

if __name__ == '__main__':
    main()
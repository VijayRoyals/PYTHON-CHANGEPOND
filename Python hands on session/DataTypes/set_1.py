#Creating a Set

# staff_id = {123,43,233,322} #
# mixed_type = {'raghul',23,54,True,23}
# print('Set : ',mixed_type)
# print('Length : ',len(mixed_type))


# s1 = {True,0,1,False}
# print(s1)

# s1={True,1}
# print(s1)

# s1={1,True}
# print(s1)

#Task -> Iterate using for loop
mixed_type = {'raghul',23,54,True,23}
for i in mixed_type:
    print(i)
for i in range(len(mixed_type)):
    print(mixed_type[i])
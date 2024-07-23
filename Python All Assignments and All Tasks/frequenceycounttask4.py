def count_frequency(string):
    freq = {}
    for char in string:
        if char.isalpha():
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


test_string = "Hello, world!"
print("Frequency of letters:")
print(count_frequency(test_string))

def hidden(matrix, n):
    # Your implementation here!
    #initiate a new list, result = ""
    #loop through the matrix, flatten the matrix to a list. flatten=[]
    #loop through flaten, when index%n == 0, add this letter to result
    # result = ""
    # flatten = []
    # for row in matrix:
    #     for letter in row:
    #         flatten.append(letter)
    # for index  in range(len(flatten)):
    #     if index % n == 0:
    #         result += flatten[index]
    # return result
    flatten = (letter for row in matrix for letter in row)
    return "".join( letter for i, letter in enumerate(flatten) if i % n == 0)
matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print(hidden(matrix_2, 5))
print("All tests passed! Discuss time and space complexity if time remains!")


def permute(n: int, set = [], outstr: str = '('):
    '''
    Ethan Cook's permutation machine
    Prints the total permutations of set {1, 2, ... , n}
    in the form of n-tuples (x1, x2, ..., xn)
    '''

    if set == []: #builds the set (this will only run on the first call)
        for k in range(n):
            set.append(k + 1)

    if n == 0: #base case, nothing left to permute through so print the result
        print(outstr[:-2] + ')')

    for i in range(n): #cycles through the set
        tmp = set[:]
        tmp.remove(set[i])
        permute(n - 1, tmp, outstr + str(set[i]) + ', ') #where the magic happens


#num = int(input('permute how many digits: '))
num = 5
permute(num)
def find_pair_n2(arr, s):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] + arr[j]) == s:
                return f'Pair found at index {i} and {j}'

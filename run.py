
def max_or_array(A, N):
    total_or = 0
    for num in A:
        total_or |= num

    max_len = 0
    for i in range(N):
        current_or = 0
        for j in range(i, N):
            current_or |= A[j]
            before = 0
            for k in range(0, i):
                before |= A[k]
            after = 0
            for k in range(j+1, N):
                after |= A[k]
            remaining_or = before | after
            if remaining_or == total_or:
                max_len = max(max_len, (j - i + 1))
    return max_len
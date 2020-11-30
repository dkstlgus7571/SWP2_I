def for_eli(mat):
    newmat = []
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    for c in range(col_idx):
        rows_with_nonzero = [r for r in row_idx if mat[r][c]!=0]
        if rows_with_nonzero:
            pivot = rows_with_nonzero[0]
            row_idx.remove(pivot)
            newmat.append(mat[pivot])
            for r in rows_with_nonzero:
                if r is not pivot:
                    multiplier = mat[r][c]/mat[pivot][c]
                    mat[r] = [a-multiplier*b for a,b in zip(mat[r], mat[pivot])]

    for r in row_idx:
        newmat.append(mat[r])
    return newmat


def for_eli(mat):
    row_idx = list(range(len(mat)))
    col_idx = len(mat[0])
    pivot_mat = []
    for c in range(col_idx):
        rows_with_nonzero = [r for r in row_idx if mat[r][c] != 0]
        if rows_with_nonzero:
            pivot = rows_with_nonzero[0]
            for idx in rows_with_nonzero:
                pivot_mat.append(mat[idx])
                row_idx.remove(idx)
    return pivot_mat

A = [[0,2,3,4,5],
     [0,0,0,3,2],
     [1,2,3,4,5],
     [0,0,0,6,7],
     [0,0,0,9,9]]

print(for_eli(A))


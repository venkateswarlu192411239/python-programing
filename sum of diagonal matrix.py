matrix=[[1,2,3],[4,5,6],[7,8,9]]
diagonal_elements=[matrix[i][i]for i in range(len(matrix))]
diagonal_sum=sum(diagonal_elements)
print(diagonal_elements)
print(diagonal_sum)
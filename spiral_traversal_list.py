class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        c = 0
        i = 0
        j = -1
        answer_list = []
        while (len(answer_list) < m*n):
            while(j < n-c-1):
                j += 1
                answer_list.append(matrix[i][j])
            if (i >= m-c-1):
                break     
            while(i< m-c-1):
                i += 1
                answer_list.append(matrix[i][j])
            if (j <= c):
                break
            while(j>c):
                j -= 1
                answer_list.append(matrix[i][j])
            while(i>c+1):
                i -= 1
                answer_list.append(matrix[i][j])
            c += 1
        return answer_list
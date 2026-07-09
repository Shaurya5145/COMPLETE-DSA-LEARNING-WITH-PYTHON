class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral_order_matrix = []

        n = len(matrix)
        m = len(matrix[0])
        total = n*m

        c = 0

        colstart = 0
        colend = len(matrix[0])-1

        rowstart = 0
        rowend = len(matrix)-1

        while c<total:
            #rowstart
            for i in range(colstart,colend+1):
                spiral_order_matrix.append(matrix[rowstart][i])
                c+=1
            
            rowstart+=1

            if c==total:
                break

            #colend

            for i in range(rowstart,rowend+1):
                spiral_order_matrix.append(matrix[i][colend])
                c+=1

            colend-=1

            if c==total:
                break

            #rowend

            for i in range(colend,colstart-1,-1):
                spiral_order_matrix.append(matrix[rowend][i])
                c+=1

            rowend-=1

            if c==total:
                break

            #colstart

            for i in range(rowend,rowstart-1,-1):
                spiral_order_matrix.append(matrix[i][colstart])
                c+=1
            
            colstart+=1

            if c==total:
                break

        return spiral_order_matrix




        

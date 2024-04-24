class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        # EC, Prefix sums
        # get the sum of the rectangle ending at (i,j)th index in prefix sums array

        if len(matrix) == 0 or len(matrix[0]) == 0:
            self.prefixsums = []
            return

        self.matrix = matrix
        nr = len(matrix)
        nc = len(matrix[0])

        # make a matrix prefixsums to calculate the sum of the all the elements till the ith index in its rectangle box
        prefixsums = [[0 for i in range(nc)] for j in range(nr)]

        prefixsums[0][0] = matrix[0][0]
        # calcualte the sum of all the elements in the 1st row till ith index
        for i in range(1, nc):
            prefixsums[0][i] = prefixsums[0][i-1] + matrix[0][i]

        # calcualte the sum of all the elements in the 1st column till jth index
        for j in range(1, nr):
            prefixsums[j][0] = prefixsums[j-1][0] + matrix[j][0]

        # see it as squares ending at index (i,j) and remove the areas accordingly
        for i in range(1,nr):
            for j in range(1,nc):
                prefixsums[i][j] = prefixsums[i-1][j] - prefixsums[i-1][j-1] + prefixsums[i][j-1] + matrix[i][j]

        self.prefixsums = prefixsums

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # Base or Edge cases
        if len(self.prefixsums) == 0 or len(self.prefixsums[0]) == 0:
            return 0
        if row1==0 and col1 == 0:
            return self.prefixsums[row2][col2]
        # when row1 or col1 is zero
        if row1 == 0: 
            return self.prefixsums[row2][col2] - self.prefixsums[row2][col1-1]
        if col1 == 0:
            return self.prefixsums[row2][col2] - self.prefixsums[row1-1][col2]
        
        # return the answer from prefixsums directly in O(1) 
        return self.prefixsums[row2][col2] - self.prefixsums[row2][col1-1] - self.prefixsums[row1-1][col2] + self.prefixsums[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
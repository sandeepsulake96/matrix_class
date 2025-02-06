import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
       
        
        if self.h == 1:
            return self.g[0][0];
            
        else:
            return (self.g[0][0]*self.g[1][1] - self.g[0][1]*self.g[1][0]);
       
           

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        diag= [self.g[i][i] for i in range(self.w)];
        return sum(diag);
        
        
        
        

    def inverse(self):
        
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")

        # TODO - your code here
       
        inv =[]
        if self.h == 1:
            inv.append([1/self.g[0][0]]);
            
            return Matrix(inv);
        
        elif self.h ==2:
            
            a=self.g[0][0];
            b=self.g[0][1];
            c=self.g[1][0];
            d=self.g[1][1];
            
            if a*d == b*c:
                
                raise ValueError('The matrix is not invertible.');  
            else:
                fac = 1/(a*d-b*c);
                inv_mat = [[d,-b],[-c,a]];
                
                for i in range(len(inv_mat)):
                    for j in range(len(inv_mat[0])):
                        inv_mat[i][j] = fac*inv_mat[i][j];
            return Matrix(inv_mat);
                               
        
            
         

    def T(self):
                               
                               
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        #transpose = zeroes(self.w,self.h);
        transpose = [[0 for j in range(self.h)] for i in range(self.w)] # initialize the mat_sum matrix with zeros
                               
        for i in range(len(transpose)):
            for j in range(len(transpose[0])):
                transpose[i][j] = self.g[j][i];
                       
        return Matrix(transpose);
                       

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        
        mat_sum = [[0 for j in range(self.w)] for i in range(self.h)] # initialize the mat_sum matrix with zeros
        
        for i in range(self.h):
            for j in range(self.w):
                mat_sum[i][j]= self.g[i][j]+ other.g[i][j];
                
        return Matrix(mat_sum);
                
      

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #
        neg_mat = [[-self.g[i][j] for j in range(self.w)] for i in range(self.h)];
        
        return Matrix(neg_mat);
        

    def __sub__(self, other):
        
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        #   
        # TODO - your code here
        
        mat_sub = [[0 for j in range(self.w)] for i in range(self.h)]; # initialize the mat_sum matrix with zeros
        
        for i in range(self.h):
            for j in range(self.w):
                mat_sub[i][j]= self.g[i][j]- other.g[i][j];
                
        return Matrix(mat_sub)

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        if self.w != other.h:
            raise(ValueError, "Matrices can only be multiplied if the columns of first matrix equals rows of second") 
        
        product = []
        
        BT = other.T(); #taking transpose of the second matrix
        row=[];
        element=0;

       
        for rowA in (self.g):
            row=[];
            for rowB in (BT):
                element=0;
                for (eA,eB) in zip(rowA,rowB):
                    element += (eA*eB)

                row.append(element)
            product.append(row);


       
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
            mat_mul = zeroes(self.h,self.w); # initialize the mat_sum matrix with zeros

            for i in range(self.h):
                for j in range(self.w):
                    mat_mul[i][j]= (self.g[i][j]*other);

            return (mat_mul)
            
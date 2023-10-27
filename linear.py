from gurobipy import *
from operation import Operation
import copy 

class Matrix( Operation ):
    def __init__(self, mat ):
        self._matrix = mat 
        self._dim = len( mat ) 
        self._var_matrix = copy.deepcopy( self._matrix ) 

    '''
    A small function that gets i-th column of a matrix 
    '''
    def get_col(self, mat, i): 
        col_lst = []
        for row in range( len(mat) ):
            col_lst.append( mat[row][i] )

        return col_lst
    
    '''
    INPUT
    model: a gurobi model
    in_vars: a list of GRB.BINARY varibles
    out_vars: a list of GRB.BINARY variables
    
    RETURN
    model: a model with more constraints
    '''
    def genConstrs( self, model, in_vars, out_vars ):
        #print ( self._matrix ) 
        weight = sum( map( sum, self._matrix ) ) 
        #declare the support variables
        spt = [ model.addVar( vtype=GRB.BINARY ) for x in range(weight) ]

        #put the variables in their positions
        sptindex = 0
        for col in range( self._dim ):
            for row in range(self._dim):
                if self._matrix[row][col]:
                    self._var_matrix[row][col] = spt[sptindex]
                    sptindex += 1

        #print ( 'self._matrix', self._matrix ) 
        #add constraints for each row of the matrix, xi -copy-> s0, s1, s2, ... 
        for col in range( self._dim ):
            pure_col = self.pure_list( self.get_col( self._var_matrix, col) )
            model = self.General_DCopy( model, in_vars[col], pure_col )
        #s0, s1, s2, ...  -xor-> yi
        for row in range( self._dim ):
            pure_row = self.pure_list( self._var_matrix[row] )
            model = self.General_DXor( model, pure_row, out_vars[row] ) 
            
        model.addConstr( quicksum(in_vars) - quicksum(out_vars) == 0 )
        return model

 





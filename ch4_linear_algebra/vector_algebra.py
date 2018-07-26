def vector_add(v,w):
    """ Does componentwise (1 to 1 mapping) addition on two vectors of similar length"""
    return[v_i + w_i for v_i, w_i in zip(v,w)]
def vector_subtract(v,w):
    """ Does component wise subtraction to two vectors of the same length"""
    return[v_i - w_i for v_i, w_i in zip(v,w) ]
    
def vector_sum(list_of_vectors):
    '''takes a list of vectors and  compoment wise, adds them together'''
    result = list_of_vectors[0]     # We start the addition with everything being added to the first list
    for vector in list_of_vectors[1:]:      # Make a list out of the remaining vectors
        result = vector_add(result,vector)  # use the function from above to do vector addition
    return result
if __name__ == "__main__":
    vector1 = [1,2,3,4,5]
    vector2 = [1,2,3,4,5]
    print(vector_add(vector1,vector2))
    print(vector_subtract(vector1,vector2))

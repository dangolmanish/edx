def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    what this question says, It says we need to find the value without
    using ** or multiplication.
    soo, first we use exp (exponential) value set to 0, 
    when exp == 0 it will return value 1 
    else, now according the question base will multiply its recursive 
    result return   ..base * recurPower(base, exp - 1)
    now exp-1 is set to make the expontial value to set 0 and return 1
    e.g. 3^4 == 3*3*3^2
    3^4 ==3*3*3*3*3^0  
    
    '''
    # Your code here
 
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)

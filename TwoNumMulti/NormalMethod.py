a = '3141592653589793238462643383279502884197169399375105820974944592'
b = '2718281828459045235360287471352662497757247093699959574966967627'

def multiplier(param1,param2):
    length = len(param1)
    if length == 1:
        return int(param1)*int(param2)
    else:
        temp1 = multiplier(param1[:length//2],param2[:length//2])
        temp2 = multiplier(param1[length//2:],param2[length//2:])
        temp3 = multiplier(param1[:length//2],param2[length//2:])
        temp4 = multiplier(param1[length//2:],param2[:length//2])
        return 10**length*temp1+10**(length//2)*(temp3+temp4)+temp2
        
print(multiplier(a,b))

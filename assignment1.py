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

def KaratsubaMultiplier(param1,param2):
    length = len(param1)
    if length == 1:
        return int(param1)*int(param2)
    else:
        temp1 = multiplier(param1[:length//2],param2[:length//2])
        temp2 = multiplier(param1[length//2:],param2[length//2:])

        new_param1 = str(int(param1[:length//2])+int(param1[length//2:]))
        new_param2 = str(int(param2[:length//2])+int(param2[length//2:]))
        new_length = max(len(new_param1),len(new_param2))
        if new_length > length//2:
            new_param1 = '0'*(length-len(new_param1))+new_param1
            new_param2 = '0'*(length-len(new_param2))+new_param2

        temp3 = multiplier(new_param1,new_param2)
        
        return 10**length*temp1+10**(length//2)*(temp3-temp1-temp2)+temp2


print(multiplier(a,b))
print(KaratsubaMultiplier(a,b))

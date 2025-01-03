def function_with_uncommon_error_solution(a, b):
    if a == 0:
        return float('inf') if b > 0 else float('-inf')
    else:
        return a / b
    #return float('inf') if a==0 and b >0 else float('-inf') if a == 0 and b < 0 else a/b
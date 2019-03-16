A = [0] #this is any random string of numbers

def solution(A):
    A.sort()
    B = len(A)
    mini = 0 
    counter = 0
    if max(A) < 0:
        return 1
    else:
        for ele in A:
            if ele <= mini:
                counter += 1
                if counter == B:
                    return (mini+1)
                    break
                else:
                    continue            
            elif (ele - 1) == mini:
                mini = ele
                counter += 1
                if counter == B:
                    return (mini+1)
                    break
                else:
                    continue
            else:
                return (mini+1)
            
print(solution(A))

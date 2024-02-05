# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

""" As given in the problem the algorithmic complexity of this problem cannot be O(M * N) because
    in the manner of the comparisons you need to do, to conclude the Strings are similar. Because we
    want to decide that "HYJ&*!" and "j!*Hy&" are similar a straight O(N) linear comparison would not 
    work so the best case is O( M * N^2) """ 


def solution(A, B):
    
    num_matches = []
    same_org_strings = [] 
    prev_org = None

    def find_matches( string_list ):
        processed_strings = [] # we will not rematch the strings we have already matched 
        
        for i in range(0, len( string_list) ):
            appearance_cnt = 0
            if ( string_list[i] in processed_strings ):
                continue
            
            for p in string_list :
                if string_list[i] ==  p:
                    appearance_cnt += 1
                
            if appearance_cnt > 0:
                num_matches.append( appearance_cnt)
                
            processed_strings.append(string_list[i])

            
    for i in range(0,len(A)):
        org = A[i]
        sanitized_str = ""
        if org != prev_org and prev_org is not None :
            find_matches( same_org_strings)
            same_org_strings.clear()
        
        same_org_strings.append(sanitized_str.join(sorted(B[i].lower()) )) # We  are doing this so that it becomes easier to match. 
        prev_org = org 
    
    if ( len( same_org_strings) > 0): # process the last set of Strings we may have 
        find_matches( same_org_strings)
    
    return num_matches


""" Test Driver """
if __name__ == '__main__':
    print(solution( [0,0,0,1,1,2,2,3,3], ['hello', 'Hello', 'Helloooo', 'pass123','123PaSS', 'ghh$%6','GH%$H6','ajhgdj','kjsdk']))
    print(solution( [0,0,1,1,1] , ['pass123','123PaSS','hello', 'Hello', 'Helloooo']))
    
   

'''
goal :

   *  *
  **  **
 ***  ***
****   ***

'''
        

def solution(size):
    for i in range(1,size):
        print(f"{' '*(size-i)}{'*'*i}  {'*'*i}")       

solution(5)
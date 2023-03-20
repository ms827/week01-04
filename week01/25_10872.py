import time
ti = time.time()  # 시작 시간 저장

def factorial(n): 
    result = 1 
    if n > 0 :
        result = n * factorial(n-1) 
    return result 

n = int(input())
print(factorial(n))

print("time :", time.time() - ti)
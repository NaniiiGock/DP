import time

def solve(str, dict) -> bool:
    i1=0
    for i2 in range(len(str)+1):
        if str[i1:i2] in dict:
            i1=i2
    if i1==i2:
        return True
    return False

def test():
    for n in range(10):
        n+=1
        n*=1000
        data="a"*n
        dictionary={"a"}
        print(timing(1000, solve, data, dictionary))

def timing(iteretion, method, arg1, arg2):
    sum=0
    for _ in range(iteretion):
        tim=time.time()
        method(arg1, arg2)
        sum+=time.time()-tim
    return sum/iteretion

if __name__=="__main__":
    test()

n = 4

def fbn(n):
    if n ==2:
        return 1
    if n == 1:
        return 1
    return fbn(n-1)+fbn(n-2)
        
print(fbn(n)%20132013)

fb = [1,1]
for i in range(2,n):
    fb.append(fb[i-1]+fb[i-2])
print(fb[n-1]%20132013)
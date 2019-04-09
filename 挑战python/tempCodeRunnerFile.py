for key,value in dic:
    destination = n - value
    current = key
    if destination == current:
        continue
    if abs(destination-current) < n - abs(destination-current):
        sum_my += 2*abs(destination-current)-1
    else:
        sum_my += 2*(n - abs(destination-current))-1
    dic[key] = dic[destination]
    dic[destination] = value
print(sum_my)
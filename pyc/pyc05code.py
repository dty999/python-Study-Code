import pickle
banner = pickle.load(open('pyc//banner.p','rb'))
print((banner))

for linelist in banner:
    print(''.join(ch * count for ch,count in linelist))
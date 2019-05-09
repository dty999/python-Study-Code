# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
import os

def get_lines_py(path):
    lines_sum = 0
    lines_zhushi = 0
    lines_konghang = 0

    for fpathe,_,fs in os.walk(path):
        for f in fs:
            if f.endswith('.py'):
                print(f)
                path_py = os.path.join(fpathe,f)
                with open(path_py,'rt',encoding = 'utf-8') as f:
                    for line in f.readlines():
                        lines_sum += 1
                        line_tmp = line.strip()
                        if line_tmp.startswith('#') or line_tmp.startswith('"""'):
                            lines_zhushi += 1
                            continue
                        if len(line_tmp) == 0:
                            lines_konghang += 1
                            continue
    return lines_sum,lines_konghang,lines_zhushi



lines = get_lines_py('C:\\Users\\22512\\OneDrive\\document\\python-Study-Code')


print('总行数：',lines[0])
print('注释行数：',lines[2])
print('空行数：',lines[1])
                    
                    
                    



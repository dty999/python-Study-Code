#用正则表达式， 找到这样的“小写字符”：其两侧恰好都被3个大写字母占据。
import re
all_str = ''.join(open('pyc//pyc03.txt'))
chars = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',all_str)
print(''.join(chars))
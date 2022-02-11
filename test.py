list = [1,2,3]

import re
value = re.compile(r'^[-+]?[0-9]+\.[0-9]+$')
print(re.compile(r'^[-+]?[0-9]+\.[0-9]+$').match("-1"))
try:
    f = float("-1")
    print("aaa")
except ValueError:
    print("输入的不是数字！")
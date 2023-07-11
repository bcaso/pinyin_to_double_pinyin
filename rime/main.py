import sys
sys.path.append('..')

import dp


# 全拼词库位置
# path = '/home/{username}/.local/share/fcitx5/rime/py.dict.yaml'

# 全拼词库
fi = open('py.dict.yaml', 'r', encoding='utf-8', errors='ignore')
# 双拼词库
fo = open('dp.dict.yaml', 'w', encoding='utf-8')

lis = fi.readlines()
fi.close()

for line in lis:
    t = line
    if '	' in line:
        t = t.split('	')           # 先用 ^I 拆分出全拼编码
        py_lis =  t[1].split(' ')    # 再用空格将全拼字符串拆分为一个个的单个全拼字符串
        new_py_lis = [dp.todouble(py) for py in py_lis]   # 将每个全拼编码都转的双拼编码
        new_pystr = ' '.join(new_py_lis)                  # 将多个双拼编码合为一个字符串
        t[1] = new_pystr
        t = '	'.join(t)             # 使用 ^I 分隔
    fo.write(t)                      # 写入新文件

fo.close()

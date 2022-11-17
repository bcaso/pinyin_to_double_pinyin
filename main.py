from dp import todouble

def gen_single_pinyin_file(input_file: str, output_file: str) -> None:
    """
    传入拼音词库，生成单字对应的拼单词库，就是移除拼音词库中的词，或成语
    每一行的内容大概如下所示，以 tab 键分隔

    $ddcmd(祖宗,祖宗【pypf】)	zuzong

    :param input_file: 导入的拼音词库的文件名称
    :param output_file: 导出的单字拼单词库要用的文件名称
    """
    fi = open(input_file, 'r', encoding='utf-8', errors='ignore')
    fo = open(output_file, 'w', encoding='utf-8')

    res = []
    lis = fi.readlines()
    for line in lis:
        # 排除不合法的行
        if not line.startswith('$'): continue

        start = line.index('(')+1
        end = line.index(',')-1
        length = end - start + 1

        if length == 1:
            res.append(line)


    for each in res:
        fo.write(each)

    fi.close()
    fo.close()


def gen_single_double_pinyin_file(input_file: str, output_file: str) -> None:
    """
    将单字全拼词库转为单字双拼词库

    :param input_file: 单字全拼词库文件名
    :param output_file: 生成的单字双拼词库文件名
    """
    fi = open(input_file, encoding='utf-8', errors='ignore')
    fo = open(output_file, 'w', encoding='utf-8')

    lis = fi.readlines()
    res = []

    i = 0
    for line in lis:
        line = line.strip()
        code, dp_code = '', ''

        try:
            code, dp_code = line.split('\t')
            dp_code = todouble(dp_code)    # 将全拼编码转为双拼编码
        except Exception as e:
            print(e)
            print(line)
            print(line.split())
        res.append(f'{code}\t{dp_code}\n')

    # 写入文件
    # 在头部加上两行
    fo.write('---config@码表分类=辅码码表\n---config@码表别名= 拼音\n')

    for each in res: fo.write(each)

    fi.close()
    fo.close()


# 将多多输入法导出的全拼词库 '导出 - 辅码 - 汉语拼音.txt' 转换为全拼单字词库
gen_single_pinyin_file(input_file='导出 - 辅码 - 汉语拼音.txt', output_file='汉语拼音单字词库.txt')

# 将单字全拼词库 '汉语拼音单字词库.txt' 中的全拼编码转为双拼编码
gen_single_double_pinyin_file(input_file='汉语拼音单字词库.txt', output_file='多多小鹤双拼单字词库.txt')

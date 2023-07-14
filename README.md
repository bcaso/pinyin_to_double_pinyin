# 全拼转双拼脚本及词库

## 前言

五笔输入法都有临时拼音或拼音反查功能，如果对应的全拼编码改为双拼（小鹤双拼），用双拼反查形，或临时双拼，会比全拼更高效。

## 多多输入法小鹤双拼单字反查拼音词库

<a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/导出 - 辅码 - 汉语拼音.txt'>导出 - 辅码 - 汉语拼音.txt</a>：多多输入法导出拼音词库，这个拼音词库是由输入法<a href='http://98wb.ysepan.com/'>98 五笔新手版</a> 导出的。

main.py 作用：

1. 这个脚本先将多多输入法导出的拼音词库(<a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/导出 - 辅码 - 汉语拼音.txt'>导出 - 辅码 - 汉语拼音.txt</a>)转为单字拼音词库 <a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/汉语拼音单字词库.txt'>汉语拼音单字词库.txt</a>，去除其中的词组，因为将词组的全拼编码转换为对应的双拼编码的算法太复杂，不好实现。
2. 再将这个拼音单字词库中的全拼编码根据小鹤双拼的规则(<a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/dp.py'>dp.py</a>)替换为小鹤双拼编码，生成文件<a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/多多小鹤双拼单字词库.txt'>多多小鹤双拼单字词库.txt</a>。

替换拼音词库：

1. 清空多多输入法的拼音词库。
2. 导入脚本生成的 <a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/多多小鹤双拼单字词库.txt'>多多小鹤双拼单字词库.txt</a> 实现多多输入法中使用小鹤双拼编码反查五笔(单字反查)或临时小鹤双拼输入。



## 冰凌输入法小鹤双拼单字反查拼音词库

设置 -> 系统词库管理 -> 置换拼音词库 -> 选择文件 <a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/冰凌输入法/冰凌五笔_小鹤双拼单字反查拼音词库.txt'>冰凌五笔_小鹤双拼单字反查拼音词库.txt</a>

<details>
    <summary>格式要求：</summary>
  
1. 词库格式：<a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/冰凌输入法/冰凌五笔_小鹤双拼单字反查拼音词库.txt'>冰凌五笔_小鹤双拼单字反查拼音词库.txt</a>
: Unicode text, UTF-8 (with BOM) text, with CRLF line terminators。
2. 码表中每行有“编码”、“字”，“优先级/词序” 三个字段，“优先级/词序” 可以省略，字段之间用 `^I` 分隔，通过复制粘贴来输入该字符，在 vim 中 `:set list` 可以显示该字符。例如：

```shell
im^I测^I300
```

格式不正确会在置换拼音词库时会提示 “词库头不正确，不能生成码表”。

</details>



<b>生成冰凌输入法的小鹤双拼单字反查拼音词库的思路：</b>
1. 找到小鹤音形冰凌五笔词库 <a href='https://github.com/bcaso/pinyin_to_double_pinyin/blob/main/冰凌输入法/小鹤音形冰凌词库.txt'>小鹤音形冰凌词库.txt</a>。来自群(881376754)文件：`/网友分享词库/小鹤音形冰凌词库.txt`。
2. 去除词库中的多字的编码所在行，只剩下单字和对应的小鹤音形编码。
3. 将小鹤音形编码中的后两位的形码删除，只剩下前两位的音码。

然后置换拼音词库。

冰凌输入法的码表不能显示拆分，码表格式对比：

```text
# 多多输入法码表格式：
$ddcmd(要上屏的字,候选框显示的内容)  编码
$ddcmd(戈,戈〔 󰂇 󰂶 󰁒 󰄼 〕)  agny

# 冰凌输入法码表格式
编码 要上屏的字 词频
agny  戈 8326
```

## rime 输入法
拼音词库可能的位置：
1. `/home/{username}/.local/share/fcitx5/rime/py.dict.yaml`
2. `/usr/share/rime-data/py.dict.yaml`
3. 安卓同文输入法，`/sdcard/android/rime/py.dict.yaml`

替换拼音词库：将转换后的 `dp.dict.yaml` 改名为 `py.dict.yaml` 替换原有的 `py.dict.yaml`。

# references

[冰凌输入法码表定义 https://www.icesofts.com/guide/guide6.html ](https://www.icesofts.com/guide/guide6.html#:~:text=%E5%8D%81%E5%85%AD%E8%BF%9B%E5%88%B6%E6%95%B0%E5%AD%97%E3%80%82-,%E2%9E%A2%E2%80%83%E7%A0%81%E8%A1%A8%E5%AE%9A%E4%B9%89,-%E2%97%8F%E2%80%83%E7%A0%81%E8%A1%A8%E4%BD%8D%E4%BA%8E)

[冰凌输入法实现五笔输入+双拼反查 https://zhuanlan.zhihu.com/p/56074482 ](https://zhuanlan.zhihu.com/p/560744826)

[98 五笔资源库 http://98wb.ysepan.com/ ](http://98wb.ysepan.com/)

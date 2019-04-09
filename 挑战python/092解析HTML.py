"""我们每天都在浏览网页，HTML是网页的基础，现在请你模拟解析简单的HTML代码。
我们这里定义的HTML只包括两个特殊标记和,具体的解析规则如下：
rule1：你从输入中读入的一个单词，如果这个单词和当前行已有的长度加起来不超过80，则将该单词输出到当前行，否则另起一行，将该单词输出到下一行的开头；
rule2：如果你从输入中读到的是,则换行
rule3：如果你从输入中读到的是,则另起一行输出80个'-'（如果当前正好在新行的开始，则直接输出80个'-'），并再次换行到新行的开始。
rule4：单词之间以一个空格分开。
给你一个HTML字符串html,请你输出解析之后的结果。
注意：输入的每个单词长度保证不超过80；标点符号算作前一个单词的内容，
如：字符串"abc12, kkd" 包含两个单词："abc123,"和"kkd".保证正常的单词不会包括"<"或">"。

例：
html=
'''
Hallo, dies ist eine 
ziemlich lange Zeile, die in Html
aber nicht umgebrochen wird.

Zwei   produzieren zwei Newlines. 
Es gibt auch noch das tag  was einen Trenner darstellt.
Zwei   produzieren zwei Horizontal Rulers.
Achtung       mehrere Leerzeichen irritieren

Html genauso wenig wie


mehrere Leerzeilen.
'''
解析之后，输出：
Hallo, dies ist eine ziemlich lange Zeile, die in Html aber nicht umgebrochen
wird.
Zwei

produzieren zwei Newlines. Es gibt auch noch das tag
--------------------------------------------------------------------------------
was einen Trenner darstellt. Zwei
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
produzieren zwei Horizontal Rulers. Achtung mehrere Leerzeichen irritieren Html
genauso wenig wie mehrere Leerzeilen."""
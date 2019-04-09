"""Baidu的服务器上使用的不是北京时间，而是Baidu时间。Baidu时间的时分秒与北京时间相同，
但是日期与北京时间不同，是用一个正整数表示从2000年1月1日开始经过了几天。
现在就请大家设计一个程序将北京时间转换为百度时间。在本题中，闰年的年份是400的倍数，
或者是4的倍数但不是100的倍数。比如2000和8888均为闰年，但6100不是。
现在给你一个字符串stime,表示待转化的北京时间（不含空格和TAB），正确的格式有两种：
一种为：YYYY-MM-DD，（YYYY表示四位数年份，MM为两位月份，DD为两位日期）；
另一种为：MM/DD/YYYY，（YYYY表示四位数年份，MM为两位月份，DD为两位日期）；
若给定的stime是正确的时间，则输出转换后的结果（一个整数）；
否则输出Error。
如：stime="2000-01-01",则输出0
    stime="AStar2007",则输出Error
    stime="1999-12-31",则输出-1"""
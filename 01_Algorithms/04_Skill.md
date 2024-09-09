##### <a href="https://leetcode.cn/problems/integer-break/">343. 整数拆分	🟠</a>
```python
class Solution:
    def cuttingRope(self, bamboo_len: int) -> int:
        if bamboo_len <= 3:
            return bamboo_len - 1

        quotient, remainder = bamboo_len // 3, bamboo_len % 3
        if remainder == 0:
            return 3 ** quotient
        elif remainder == 1:
            return 3 ** (quotient - 1) * 4
        else:
            return 3 ** quotient * 2
```
每个大于4的数一定可以拆分成两个数使乘积大于4。 由于数学前提的存在，所以一定要将数尽量拆成2和3的组合（如果拆出来的子数大于4 那么一定不是最大值，因为数学前提。） 再就是为什么要多拆3而不是拆2的问题。 所以不管绳子多长，最后的答案肯定是3x3x3x3……3x3x2或者3x3x3x3……3x3x2x2

##### <a href="https://leetcode.cn/problems/nim-game/">292. Nim 游戏	🟢</a> 

你和你的朋友面前有一堆石子，你们轮流拿，一次至少拿一颗，最多拿三颗，谁拿走最后一颗石子谁获胜。

假设你们都很聪明，由你第一个开始拿，请你写一个算法，输入一个正整数 n，返回你是否能赢（true 或 false）。

比如现在有 4 颗石子，算法应该返回 false。因为无论你拿 1 颗 2 颗还是 3 颗，对方都能一次性拿完，拿走最后一颗石子，所以你一定会输。

首先，这道题肯定可以使用动态规划，因为显然原问题存在子问题，且子问题存在重复。但是因为你们都很聪明，涉及到你和对手的博弈，动态规划会比较复杂。

我们解决这种问题的思路一般都是反着思考：

如果我能赢，那么最后轮到我取石子的时候必须要剩下 1~3 颗石子，这样我才能一把拿完。

如何营造这样的一个局面呢？显然，如果对手拿的时候只剩 4 颗石子，那么无论他怎么拿，总会剩下 1~3 颗石子，我就能赢。

如何逼迫对手面对 4 颗石子呢？要想办法，让我选择的时候还有 5~7 颗石子，这样的话我就有把握让对方不得不面对 4 颗石子。

如何营造 5~7 颗石子的局面呢？让对手面对 8 颗石子，无论他怎么拿，都会给我剩下 5~7 颗，我就能赢。
```python
def canWinNim(int n):   return n % 4 != 0
```

##### <a href="https://leetcode.cn/problems/bulb-switcher/">319. 灯泡开关	🟠</a> 
因数为单数的会亮
```python
def bulbSwitch(int n):   return floor(sqrt(n))
```

##### <a href="https://leetcode.cn/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/">LCR 162. 数字 1 的个数	🔴</a>
输入一个整数 n ，求 1～n 这 n 个整数的十进制表示中 1 出现的次数。例如， 1~13 中包含 1 的数字有 1 、 10 、 11 、 12 、 13 因此共出现 6 次
```python
def digitOneInNumber(num: int) -> int:
    digit, res = 1, 0
    high, cur, low = num // 10, num % 10, 0
    while high != 0 or cur != 0:
        if cur == 0: res += high * digit
        elif cur == 1: res += high * digit + low + 1
        else: res += (high + 1) * digit
        low += cur * digit
        cur = high % 10
        high //= 10
        digit *= 10
    return res
```

##### <a href="https://leetcode.cn/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/">LCR 163. 找到第 k 位数字	🔴</a>
数字以 0123456789101112131415... 的格式作为一个字符序列，在这个序列中第 2 位（从下标 0 开始计算）是 2 ，第 10 位是 1 ，第 13 位是 1 ，以此类题，请你输出第 n 位对应的数字。
```python
def findNthDigit(n: int) -> int:
    #记录n是几位数
    i = 1 
    while i * pow(10, i) < n:
        #前面添0增加的位
        n += pow(10, i)
        i += 1
    #根据除法锁定目标数字，根据取模锁定位置
    return int(str(n // i)[n % i])
```

##### <a href="https://leetcode.cn/problems/ugly-number/">263. 丑数 	🟢</a>
##### <a href="https://leetcode.cn/problems/ugly-number-ii/">264. 丑数 II 	🟠</a>



##### <a href="https://leetcode.cn/problems/single-number/">136. 只出现一次的数字 	🟢</a>

##### <a href="https://leetcode.cn/problems/single-number-ii/">137. 只出现一次的数字 II 	🟠</a>

##### <a href="https://leetcode.cn/problems/single-number-iii/">260. 只出现一次的数字 III 	🟠</a>

##### <a href="https://leetcode.cn/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/">LCR 187. 约瑟夫环 	🟠</a>
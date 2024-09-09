
## 如何控制小数点位数
### py
```python
a = 3.14159
b = round(a, 2) # 保留两位小数

b = "%.2f" % a # 保留两位小数

b = '{:.2f}'.format(a) # 保留两位小数

print(b) # 输出 3.14
```
### Java
使用DecimalFormat类：

```java
import java.text.DecimalFormat;

double num = 3.14159;
DecimalFormat df = new DecimalFormat("0.00"); // 保留两位小数
String result = df.format(num);
System.out.println(result); // 输出 3.14

```

使用String.format()方法：

```java
double num = 3.14159;
String result = String.format("%.2f", num); // 保留两位小数
System.out.println(result); // 输出 3.14
```

使用Double.toString()：

```java
double num = 3.14159;
String result = Double.toString(num);
System.out.println(result); // 输出 3.14159
```


```python
#DSU(查并集)实现
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            # Union by rank
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
```

## python 二分函数 bisect
```python
index = bisect.bisect(ls, x)   #第1个参数是列表，第2个参数是要查找的数，返回值为索引
index = bisect.bisect_left(ls, x)
index = bisect.bisect_right(ls, x) #与bisect.bisect()一致
# bisect.bisect和bisect.bisect_right返回大于x的第一个下标，bisect.bisect_left返回大于等于x的第一个下标。

index = bisect.bisect(rides, start, hi = i - 1, key = lambda x : x[1])

#hi = i - 1：这是查找的上界。具体而言，在[0, hi)这个左闭右开区间中寻找。

#key = lambda x : x[1]：这是用于比较的元素。默认情况下，bisect比较元素x的值，而这里表示比较元素x的下标等于1的元素的值（说明元素x是一个列表或元组等等），即x[1]。
```


## 常用方法与容器类

### 使用数组记录字符
```Java
//使用数组记录字符
int[] cnt = new int[26];
for (int i = 0; i < n; ++i) {
    ++cnt[s1.charAt(i) - 'a'];
}
```

### 用Map记录字符
```Java
//用Map记录字符
Map<Character, Integer> map = new HashMap<>();

for (int i = 0; i < len1; i++) {
    char c = s1.charAt(i);
    map1.put(c, map1.getOrDefault(c, 0) + 1);
}
```

### 单调栈实现
```Java
int[] nextGreaterElement(int[] nums) {
    int n = nums.length;
    // 存放答案的数组
    int[] res = new int[n];
    Stack<Integer> s = new Stack<>(); 
    // 倒着往栈里放
    for (int i = n - 1; i >= 0; i--) {
        // 判定个子高矮
        while (!s.isEmpty() && s.peek() <= nums[i]) {
            // 矮个起开，反正也被挡着了。。。
            s.pop();
        }
        // nums[i] 身后的更大元素
        res[i] = s.isEmpty() ? -1 : s.peek();
        s.push(nums[i]);
    }
    return res;
}
```

### Java优先队列堆实现
```Java
//优先队列堆实现
    class Status implements Comparable<Status> {
        int val;
        ListNode ptr;

        Status(int val, ListNode ptr) {
            this.val = val;
            this.ptr = ptr;
        }

        public int compareTo(Status status2) {
            return this.val - status2.val;
        }
    }

    PriorityQueue<Status> queue = new PriorityQueue<Status>();

  //Queue的插入取出
  queue.offer(new Status(node.val, node));
  Status f = queue.poll();
```

### python实现堆
```python
ListNode.__lt__ = lambda a, b: a.val < b.val  # 让堆可以比较节点大小
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur =   dummy = ListNode()  # 哨兵节点，作为合并后链表头节点的前一个节点
        h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
        heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点
        
'''主要方法'''
defineClass.__lt__ = lambda a, b: a.val < b.val  # 重载 < > 
heapify(h)  # 堆化
node = heappop(h)  # 取出节点
heappush(h, node)  # 拉入节点
```

### 字典树结构实现
```python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
    
    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None
```

### 取边界值
```python
float('inf')
float('-inf')
int('inf')
int('-inf')
```
```Java
Integer.MIN_VALUE 
Integer.MAX_VALUE
Long.MIN_VALUE
Long.MAX_VALUE
```

### python Java 排序
```python
# 排序 默认递增
envelopes.sort(key=lambda x: (x[0], -x[1]))
p=sorted(envelopes , key=lambda x: (x[0], -x[1]),reverse=False)
```
```Java
Arrays.sort(envelopes, new Comparator<int[]>() {
    public int compare(int[] e1, int[] e2) {
        if (e1[0] != e2[0]) {
            return e1[0] - e2[0];
        } else {
            return e2[1] - e1[1];
        }
    }
});
```
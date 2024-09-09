
⭐
# 数组

## 双指针

### 常规双指针  

#### 

##### <a href="https://leetcode.cn/problems/remove-duplicates-from-sorted-array/">26. 删除有序数组中的重复项	🟢</a>

##### <a href="https://leetcode.cn/problems/remove-element/">27. 移除元素	🟢</a>

##### <a href="https://leetcode.cn/problems/remove-duplicates-from-sorted-list/">83. 删除排序链表中的重复元素   	🟢</a>

##### <a href="https://leetcode.cn/problems/move-zeroes/">283. 移动零	🟢</a>
---

### 左右指针  

####

##### <a href="https://leetcode.cn/problems/two-sum-ii-input-array-is-sorted/">167. 两数之和 II - 输入有序数组	🟠</a>

##### <a href="https://leetcode.cn/problems/reverse-string/">344. 反转字符串	🟢</a>


## 滑动窗口 

### 常规动窗口

####

##### <a href="https://leetcode.cn/problems/longest-substring-without-repeating-characters/">3. 无重复字符的最长子串	🟠</a>

##### <a href="https://leetcode.cn/problems/find-all-anagrams-in-a-string/">438. 找到字符串中所有字母异位词	🟠</a>

##### <a href="https://leetcode.cn/problems/permutation-in-string/">567. 字符串的排列	🟠</a>

##### <a href="https://leetcode.cn/problems/minimum-window-substring/">76. 最小覆盖子串	🔴</a>


## 二分查找
快速的查找方式，基于数组结构实现
###

####

##### <a href="https://leetcode.cn/problems/binary-search/">704. 二分查找	🟢</a>

##### <a href="https://leetcode.cn/problems/median-of-two-sorted-arrays/">4. 寻找两个正序数组的中位数	🔴</a>

##### <a href="https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/">34. 在排序数组中查找元素的第一个和最后一个位置	🟠</a>

```Java
//[a,b]
//常规二分
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; // 注意
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid - 1; // 注意
    }
    return -1;
}

int left_bound(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] < target)
            left = mid + 1; 
        else
            right = mid - 1; 

    }
    // 判断 target 是否存在于 nums 中
    if (left < 0 || left >= nums.length) {
        return -1;
    }
    // 判断一下 nums[left] 是不是 target
    return nums[left] == target ? left : -1;
}

int right_bound(int[] nums, int target) {
    int left = 0; 
    int right = nums.length - 1; 
    while(left <= right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] > target)
            right = mid - 1; 
        else
            left = mid + 1; 
    }
    if (right < 0 || right >= nums.length) {
        return -1;
    }
    return nums[right] == target ? right : -1;
}
//[a,b)
//常规二分
int binarySearch(int[] nums, int target) {
    int left = 0; 
    int right = nums.length; // 注意
    while(left < right) {
        int mid = left + (right - left) / 2;
        if(nums[mid] == target)
            return mid; 
        else if (nums[mid] < target)
            left = mid + 1; // 注意
        else if (nums[mid] > target)
            right = mid; // 注意
    }
    return -1;
}

```
##### <a href="https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/">153. 寻找旋转排序数组中的最小值	🟠</a>

##### <a href="https://leetcode.cn/problems/search-in-rotated-sorted-array/">33. 寻找旋转排序数组中的最小值	🟠</a>

##### <a href="https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/">81. 寻找旋转排序数组中的最小值II	🟠</a>


## 前缀和与差分

## 栈

### 单调栈

####

##### <a href="https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/">1081. 不同字符的最小子序列	    🟠</a>

##### <a href="https://leetcode.cn/problems/remove-duplicate-letters/">316. 去除重复字母(该题与1081相同)	🟠</a>

```Java
public String smallestSubsequence(String s) {
        boolean[] vis = new boolean[26];
        int[] num = new int[26];
        for (int i = 0; i < s.length(); i++) {
            num[s.charAt(i) - 'a']++;
        }

        StringBuffer sb = new StringBuffer();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (!vis[ch - 'a']) {
                while (sb.length() > 0 && sb.charAt(sb.length() - 1) > ch) {
                    if (num[sb.charAt(sb.length() - 1) - 'a'] > 0) {
                        vis[sb.charAt(sb.length() - 1) - 'a'] = false;
                        sb.deleteCharAt(sb.length() - 1);
                    } else {
                        break;
                    }
                }
                vis[ch - 'a'] = true;
                sb.append(ch);
            }
            num[ch - 'a'] -= 1;
        }
        return sb.toString();
    }
```

## 其他

### 中心扩散法(回文)

####

##### <a href="https://leetcode.cn/problems/longest-palindromic-substring/">5. 最长回文子串	🟠 </a>

### 双反转

####

##### <a href="https://leetcode.cn/problems/reverse-words-in-a-string/">151. 反转字符串中的单词	🟠</a>

```Java
    public String reverseWords(String s) {
        // 除去开头和末尾的空白字符
        s = s.trim();
        // 正则匹配连续的空白字符作为分隔符分割
        List<String> wordList = Arrays.asList(s.split("\\s+"));
        Collections.reverse(wordList);
        return String.join(" ", wordList);
    }
```
```python
def reverseWords(self, s: str) -> str:
    return " ".join(reversed(s.split()))
```

### 其他

####

##### <a href="https://leetcode.cn/problems/rotate-image/">48. 旋转图像	🟠</a>

##### <a href="https://leetcode.cn/problems/spiral-matrix/">54. 螺旋矩阵	🟠</a>

##### <a href="https://leetcode.cn/problems/spiral-matrix-ii/">59. 螺旋矩阵 II	🟠</a>

##### <a href="https://leetcode.cn/problems/longest-consecutive-sequence/">128. 最长连续序列    🟠</a>


# 链表

## 双指针

### 快慢指针  

####

##### <a href="https://leetcode.cn/problems/linked-list-cycle/">141. 环形链表	🟢</a>

##### <a href="https://leetcode.cn/problems/linked-list-cycle-ii/">142. 环形链表 II	🟠</a>

##### <a href="https://leetcode.cn/problems/middle-of-the-linked-list/">876. 链表的中间结点  🟠</a>

### 固定位指针  
  
####

##### <a href="https://leetcode.cn/problems/intersection-of-two-linked-lists/">160. 相交链表	🟢</a>

  ```python
  def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      if not (headA or headB):return None 
      p1,p2=headA,headB
      while(p1 != p2):
          p1 = p1.next if p1 else headB
          p2 = p2.next if p2 else headA
      return p1
  ```

##### <a href="https://leetcode.cn/problems/remove-nth-node-from-end-of-list/">19. 删除链表的倒数第 N 个结点	🟠</a>

### 条件调节指针

####

##### <a href="https://leetcode.cn/problems/partition-list/">86. 分隔链表	🟠</a>


## 递归

###

####

##### <a href="https://leetcode.cn/problems/reverse-linked-list/">206. 反转链表	🟢(迭代)</a>

```Java
//递归解法
// 定义：输入一个单链表头结点，将该链表反转，返回新的头结点
ListNode reverse(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    ListNode last = reverse(head.next);
    head.next.next = head;
    head.next = null;
    return last;
}
```

##### <a href="https://leetcode.cn/problems/reverse-linked-list-ii/">92. 反转链表 II	🟠(迭代) </a>

##### <a href="https://leetcode.cn/problems/reverse-nodes-in-k-group/">25. K 个一组翻转链表	🔴（分治）</a>

##### <a href="https://leetcode.cn/problems/palindrome-linked-list/">234. 回文链表	🟢 (回溯，栈)</a>

## 其他

###

####

##### <a href="https://leetcode.cn/problems/merge-two-sorted-lists/">21. 合并两个有序链表	🟢 (递归)</a>

```Java
//递归解法
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) {
            return l2;
        }
        else if (l2 == null) {
            return l1;
        }
        else if (l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        }
        else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }

    }
}
```  

##### <a href="https://leetcode.cn/problems/merge-k-sorted-lists/">23. 合并K个升序链表	🔴（堆）</a>

# 二叉树

## 递归

###

####

##### <a href="https://leetcode.cn/problems/maximum-depth-of-binary-tree/">104. 二叉树的最大深度	🟢</a>

```Java
/ 定义：输入根节点，返回这棵二叉树的最大深度
int maxDepth(TreeNode root) {
	if (root == null) {
		return 0;
	}
	// 利用定义，计算左右子树的最大深度
	int leftMax = maxDepth(root.left);
	int rightMax = maxDepth(root.right);
	// 整棵树的最大深度等于左右子树的最大深度取最大值，
    // 然后再加上根节点自己
	int res = Math.max(leftMax, rightMax) + 1;

	return res;
}
```

##### <a href="https://leetcode.cn/problems/binary-tree-inorder-traversal/">94. 二叉树的中序遍历	🟢</a>

##### <a href="https://leetcode.cn/problems/binary-tree-preorder-traversal/">144. 二叉树的前序遍历	🟢  
</a>

##### <a href="https://leetcode.cn/problems/invert-binary-tree/">226. 翻转二叉树    🟢</a>

##### <a href="https://leetcode.cn/problems/symmetric-tree/">101. 对称二叉树    🟢</a>

##### <a href="https://leetcode.cn/problems/diameter-of-binary-tree/">543. 二叉树的直径  🟢</a>

##### <a href="https://leetcode.cn/problems/binary-tree-level-order-traversal/">102. 二叉树的层序遍历	🟢</a>

```python
def levelOrder(self, root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if not root:
        return []
    que=[root]
    result=[]
    while(que):
        node=[]
        for _ in range(len(que)):
            p=que.pop(0)
            node.append(p.val)
            if p.left:que.append(p.left)
            if p.right:que.append(p.right)
        result.append(node)
    return result
```

##### <a href="https://leetcode.cn/problems/copy-list-with-random-pointer/">138. 复制带随机指针的链表  🟠</a>

```Java
Map<Node, Node> cachedNode = new HashMap<Node, Node>();

public Node copyRandomList(Node head) {
    if (head == null) {
        return null;
    }
    if (!cachedNode.containsKey(head)) {
        Node headNew = new Node(head.val);
        cachedNode.put(head, headNew);
        headNew.next = copyRandomList(head.next);
        headNew.random = copyRandomList(head.random);
    }
    return cachedNode.get(head);
}
```


##### <a href="https://leetcode.cn/problems/count-complete-tree-nodes/">222. 完全二叉树的节点个数   🟠</a>

##### <a href="https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/solutions/">236. 二叉树的最近公共祖先   🟠</a>

```python
class Solution:
    def __init__(self):
            self.ans = None
    def findLCA(self, root: TreeNode, p: TreeNode, q: TreeNode) -> bool:
        if not root:
            return False
        isPFound = self.findLCA(root.left, p, q)
        isQFound = self.findLCA(root.right, p, q)

        if (isPFound and isQFound) or ((root.val == p.val or root.val == q.val) and (isPFound or isQFound)):
            self.ans = root
        return isPFound or isQFound or root.val == p.val or root.val == q.val
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.findLCA(root, p, q)
        return self.ans
```

##### <a href="https://leetcode.cn/problems/binary-tree-maximum-path-sum/">124. 二叉树中的最大路径和  🔴</a>

## 二叉树构造

###

####

##### <a href="https://leetcode.cn/problems/maximum-binary-tree/">654. 最大二叉树 🟠</a>

```python
#构造的常规递归方法，引入索引
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def construct(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            best = left
            for i in range(left + 1, right + 1):
                if nums[i] > nums[best]:
                    best = i
        
            node = TreeNode(nums[best])
            node.left = construct(left, best - 1)
            node.right = construct(best + 1, right)
            return node
        
        return construct(0, len(nums) - 1)
```
```python
#单调栈方案(没看懂)
 def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        stk = list()
        tree = [None] * n

        for i in range(n):
            tree[i] = TreeNode(nums[i])
            while stk and nums[i] > nums[stk[-1]]:
                tree[i].left = tree[stk[-1]]
                stk.pop()
            if stk:
                tree[stk[-1]].right = tree[i]
            stk.append(i)
        
        return tree[stk[0]]
```
##### <a href="https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/">105. 从前序与中序遍历序列构造二叉树  🟠</a>
```python
 def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            preorder_root = preorder_left
            inorder_root = index[preorder[preorder_root]]
            
            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
```
##### <a href="https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal/">106. 从中序与后序遍历序列构造二叉树	🟠</a>

##### <a href="https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal/">889. 根据前序和后序遍历构造二叉树	🟠</a>

##### <a href="https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/">114. 二叉树展开为链表	🟠</a>

```python
class Solution:
    def __init__(self):
        self.nxt=None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:return
        self.flatten(root.right)
        self.flatten(root.left)
        root.left,root.right,self.nxt=None,self.nxt,root
```

## BST

###

####

##### <a href="https://leetcode.cn/problems/search-in-a-binary-search-tree/">700. 二叉搜索树中的搜索    🟢</a>

##### <a href="https://leetcode.cn/problems/insert-into-a-binary-search-tree/">701. 二叉搜索树中的插入操作  🟠</a>

##### <a href="https://leetcode.cn/problems/delete-node-in-a-bst/">450. 删除二叉搜索树中的节点  🟠</a>
```python
def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if root is None:
        return None
    if root.val > key:
        root.left = self.deleteNode(root.left, key)
    elif root.val < key:
        root.right = self.deleteNode(root.right, key)
    elif root.left is None or root.right is None:
        root = root.left if root.left else root.right
    else:
        successor = root.right
        while successor.left:
            successor = successor.left
        successor.right = self.deleteNode(root.right, successor.val)
        successor.left = root.left
        return successor
    return root
```
##### <a href="https://leetcode.cn/problems/validate-binary-search-tree/">98. 验证二叉搜索树(递归，中序遍历)    🟠
</a>

```python
def isValidBST(self, root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    def vaBST(root, minr, maxr):
        if not root:return True
        if (minr and root.val<=minr.val)or(maxr and root.val>=maxr.val):return False
        return vaBST(root.left,minr,root)and vaBST(root.right,root,maxr)
    return vaBST(root,None,None)
```

##### <a href="https://leetcode.cn/problems/kth-smallest-element-in-a-bst/">230. 二叉搜索树中第K小的元素	🟠</a>
```python
#中序迭代
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
```
```python
#中序递归(使用迭代器优化)
def kthSmallest(root: TreeNode, k: int) -> int:
    def inorder(root):
        if root:
            # 先遍历左子树
            yield from inorder(root.left)
            # 遍历当前节点，注意是 yield 而不是 return
            yield root.val
            # 最后遍历右子树
            yield from inorder(root.right)

    # 使用迭代器遍历 BST 的中序遍历序列
    it = inorder(root)
    for _ in range(k):
        ans = next(it)
    return ans
```
##### <a href="https://leetcode.cn/problems/convert-bst-to-greater-tree/">538. 把二叉搜索树转换为累加树	🟠</a>

##### <a href="https://leetcode.cn/problems/unique-binary-search-trees/">96. 不同的二叉搜索树(DP、Math)   🟠</a>

```python
#DP
def numTrees(self, n):
    G = [0]*(n+1)
    G[0], G[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            G[i] += G[j-1] * G[i-j]
    return G[n]
```
 - 卡塔兰数
$$ Catalan(n) = \frac{1}{n+1}\binom{2n}{n} $$

```python
#卡塔兰数解
def numTrees(self, n):
    C = 1
    for i in range(0, n):
        C = C * 2*(2*i+1)/(i+2)
    return int(C)
```
##### <a href="https://leetcode.cn/problems/unique-binary-search-trees-ii/">95. 不同的二叉搜索树 II 🟠</a>
```python
def generateTrees(self, n: int) -> List[TreeNode]:
    def generateTrees(start, end):
        if start > end:
            return [None,]
        
        allTrees = []
        for i in range(start, end + 1):  # 枚举可行根节点
            # 获得所有可行的左子树集合
            leftTrees = generateTrees(start, i - 1)
            
            # 获得所有可行的右子树集合
            rightTrees = generateTrees(i + 1, end)
            
            # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
            for l in leftTrees:
                for r in rightTrees:
                    currTree = TreeNode(i)
                    currTree.left = l
                    currTree.right = r
                    allTrees.append(currTree)
        return allTrees
    return generateTrees(1, n) if n else []
```

## 堆

###

####

##### <a href="https://leetcode.cn/problems/find-median-from-data-stream/">295. 数据流的中位数	🔴</a>

## 其他

###

####

##### <a href="https://leetcode.cn/problems/serialize-and-deserialize-binary-tree/">297. 二叉树的序列化与反序列化	🔴</a>
```python
#一种较为简单地序列反序列方法
class Codec:
    def serialize(self, root):
        if not root:
            return "null"

        sb = []
        sb.append(str(root.val))
        sb.append(self.serialize(root.left))
        sb.append(self.serialize(root.right))
        return ",".join(sb)
        

    def deserialize(self, data):
        datas = data.split(",")
        return self.deserialized(datas)
    
    def deserialized(self, datas):
        if datas[0] == "null":
            datas.pop(0)
            return None
        
        root = TreeNode(int(datas.pop(0)))
        root.left = self.deserialized(datas)
        root.right = self.deserialized(datas)

        return root
```

##### <a> JZ8.二叉树的下一个节点   🟠</a>
给定一个二叉树其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的next指针。
```python
    def GetNext(p):
        if p.right:
            p=p.right
            while(p.left):
                p=p.left
            return p
        else:
            while(p.next): #next指向父节点
                if p==p.next.left:
                    return p.next
                p=p.next
            return p.next
```

##### <a href="https://leetcode.cn/problems/populating-next-right-pointers-in-each-node-ii/">116. 填充每个节点的下一个右侧节点指针/117. 填充每个节点的下一个右侧节点指针 II   🟠</a>
```python
def connect(self, root: 'Node') -> 'Node':
    cur = root
    while cur:
        nxt = dummy = ListNode()  # 下一层的链表
        while cur:  # 遍历当前层的链表
            if cur.left:
                nxt.next = cur.left  # 下一层的相邻节点连起来
                nxt = cur.left
            if cur.right:
                nxt.next = cur.right  # 下一层的相邻节点连起来
                nxt = cur.right
            cur = cur.next  # 当前层链表的下一个节点
        cur = dummy.next  # 下一层链表的头节点
    return root
```


# 图

##

###

####

##### <a href="https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/">LCR 129. 字母迷宫 🟠</a>
```python
# 不使用visited的处理方式
def wordPuzzle(self, grid: List[List[str]], target: str) -> bool:
    def dfs(i, j, k):
        if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] != target[k]: return False
        if k == len(target) - 1: return True
        grid[i][j] = ''
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
        grid[i][j] = target[k]
        return res

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if dfs(i, j, 0): return True
    return False
```

##### <a href="https://leetcode.cn/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/">LCR 130. 机器人的运动轨迹 🟠</a>
地上有一个 rows 行和 cols 列的方格。坐标从 [0,0] 到 [rows-1,cols-1] 。一个机器人从坐标 [0,0] 的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，但是不能进入行坐标和列坐标的数位之和大于 threshold 的格子。 例如，当 threshold 为 18 时，机器人能够进入方格   [35,37] ，因为 3+5+3+7 = 18。但是，它不能进入方格 [35,38] ，因为 3+5+3+8 = 19 。请问该机器人能够达到多少个格子？
```python
def wardrobeFinishing(self ,  rows: int, cols: int,threshold: int) -> int:        
    markmat=[[False]*cols for _ in range(rows)]
    def count(num1,num2):
        return (sum(map(int,list(str(num1))))+sum(map(int,list(str(num2)))))<=threshold
    
    def bfs(i,j):
        if i>=0 and j>=0 and i<rows and j<cols and markmat[i][j]!=True and count(i,j):
            markmat[i][j]=True
            return bfs(i+1,j)+bfs(i,j+1)+1
        else:
            return 0
    return bfs(0,0)
```

##### <a href="https://leetcode.cn/problems/all-paths-from-source-to-target/">797. 所有可能的路径 🟠</a>

```python
def allPathsSourceTarget(self, graph):
    """
    :type graph: List[List[int]]
    :rtype: List[List[int]]
    """
    ans = []
    stk = [0]
    def dfs(x=0):
        if x == len(graph) - 1:
            ans.append(stk[:])
            return
        for y in graph[x]:
            stk.append(y)
            dfs(y)
            stk.pop()
    dfs()
    return ans
```

##### <a href="https://leetcode.cn/problems/course-schedule">207. 环检测(课程表) 🟠</a>

##### <a href="https://leetcode.cn/problems/course-schedule-ii/">207. 拓扑排序(课程表2) 🟠</a>


# 排序
##### <a href="https://leetcode.cn/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/">LCR 164. 把数组排成最小的数 🟠</a>
输入一个非负整数数组numbers，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组[3，32，321]，则打印出这三个数字能排成的最小数字为321323。

##### <a href="https://leetcode.cn/problems/shu-zu-zhong-de-ni-xu-dui-lcof/">LCR 164. 数组中的逆序对 🔴</a>


# 状态机
##### <a href="https://leetcode.cn/problems/ba-zi-fu-chuan-zhuan-huan-cheng-zheng-shu-lcof/description/">LCR 192. 把字符串转换成整数 (atoi) 🟠</a>

##### <a href="https://leetcode.cn/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/">LCR 138. 有效数字  🟠</a>
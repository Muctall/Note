import bisect
import heapq

def LastRemaining_Solution( n: int, m: int) -> int:
    #没有小朋友的情况
    if n == 0 or m == 0: 
        return -1
    x = 0
    #从小到大，更新x
    for i in range(2, n + 1):
        print(x,end="  ")

        x = (m + x) % i
    return x

def searchMatrix( matrix, target):
    m2=[matrix[i][0] for i in range(len(matrix))]
    a=bisect.bisect_left(matrix,4,key = lambda a:a[0])
    b=bisect.bisect_right(matrix[a],target)
    c=bisect.bisect_left(matrix,target,key = lambda a:a[b])
    print(a,b,c)

    if target==matrix[a][b]:
        return True
    else:
        return False
    
class Solution:
    def mergeKLists(self, lists):
        h = [head for head in lists if head]  # 初始把所有链表的头节点入堆
        heapq.heapify(h)  # 堆化
        while h:  # 循环直到堆为空
            node = heapq.heappop(h)  # 剩余节点中的最小节点
            if node.next:  # 下一个节点不为空
                heapq.heappush(h, node.next)  # 下一个节点有可能是最小节点，入堆
            cur.next = node  # 合并到新链表中
            cur = cur.next  # 准备合并下一个节点
        return dummy.next  # 哨兵节点的下一个节点就是新链表的头节点
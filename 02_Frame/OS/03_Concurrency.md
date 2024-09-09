# Thread
## Lock
mutual exclusion
fairness
performance


POSIX 库将锁称为互斥量（mutex）
```c
1  pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;
2  
3  Pthread_mutex_lock(&lock); // 包装了 pthread_mutex_lock()
4  balance = balance + 1;
5  Pthread_mutex_unlock(&lock);
```

atomic:DEKKER 算法和 PETERSON 算法

### 原子操作


**Test-and-Set (`TAS`) 伪代码:**

```plaintext
// TAS伪代码
function TAS(location):
    original_value = location  // 读取原始值
    location = 1              // 尝试设置新值
    return original_value     // 返回原始值
```

**Compare-and-Swap (`CAS`) 伪代码:**

```plaintext
// CAS伪代码
function CAS(location, expected_value, new_value):
    if location == expected_value:
        location = new_value   // 只有当值符合预期时才进行替换
        return true             // 替换成功
    else:
        return false            // 替换失败
```

**Load-Linked (`LL`) 和 Store-Conditional (`SC`) 伪代码:**

```plaintext
// LL伪代码
function LL(location):
    return location  // 返回当前值

// SC伪代码
function SC(location, new_value):
    if LL(location) == location:  // 检查LL操作的结果是否仍然是原始值
        location = new_value      // 仅在LL操作的结果未变时进行替换
        return true                // 替换成功
    else:
        return false               // 替换失败
```

**fetch-and-add(`FAA`)伪代码:**

```plaintext
// 共享变量
shared_variable = 0

// Fetch-and-Add 操作
function fetch_and_add():
    // 读取原始值
    original_value = shared_variable
    // 递增操作
    new_value = original_value + 1
    // 将新值写回共享变量
    shared_variable = new_value
    // 返回原始值
    return original_value
```



1. **Test-and-Set (`TAS`)：**
   - **用途：** 设置一个标志位，常用于实现简单的互斥锁。
   - **缺点：** 可能引起自旋锁，效率较低。

2. **Compare-and-Swap (`CAS`)：**
   - **用途：** 比较并交换操作，用于实现无锁同步，适用于更复杂的同步机制。
   - **优势：** 更灵活，不容易引起自旋锁。

3. **Load-Linked (`LL`) 和 Store-Conditional (`SC`)：**
   - **用途：** 用于实现原子性的读和写，常用于实现无锁算法。
   - **优势：** 更为通用，适用于一系列原子操作。

4. **Fetch-and-Add (`FAA`)：**
   - **用途：** 用于实现原子递增操作，常用于计数器的实现。
   - **优势：** 适用于一些特定场景，例如无锁计数器。

**比较总结：**

- `TAS` 和 `CAS` 是通用的原子操作，适用于一系列的同步机制，而 `TAS` 可能引起自旋锁。
  
- `LL` 和 `SC` 提供了更为通用的原子读和写操作，适用于一些复杂的无锁算法，但具体实现可能依赖硬件支持。
  
- `fetch-and-add` 用于实现原子递增操作，适用于一些计数器的场景。

### 并发结构
#### 计数器
懒惰计数器（sloppy counter）
#### 链表
hand-over-hand locking ，也叫作锁耦合， lock coupling

每个链表节点都包含一个独立的锁。这样，每个节点都有自己的锁，互相之间不会争用锁
#### 队列
Michael and Scott's Queue(M&S 队列)

两个锁，一个负责队列头，另一个负责队列尾： 通常，一个锁用于保护队列头部（head），另一个锁用于保护队列尾部（tail）。这使得入队列和出队列操作可以并发执行，因为它们分别只需要获取对应的锁。

假节点（Dummy Node）： Michael 和 Scott 在队列的头部添加了一个假节点。这个假节点的目的是使得队列不为空，即使没有实际的数据节点存在。这简化了队列的逻辑，确保队列的头部和尾部永远不会指向同一个节点。


### condition variable/semaphore
wait() 和 signal()
sem_wait() 和 sem_post()

### 死锁
- 互斥：
    线程对于需要的资源进行互斥的访问，例如一个线程抢到锁。

- 持有并等待：
    线程持有了资源，例如已经获得的锁，同时又在等待其他资源，比如需要获得的锁。
    预防技术：全持有锁

- 非抢占：
    线程获得的资源，例如锁，不能被其他线程抢占。
    预防技术：全trulock

- 循环等待：
    线程之间存在一个环路，环路上每个线程都额外持有一个资源，而这个资源又是下一个线程要申请的。
    预防技术：total ordering

调度避免：银行家算法

死锁检测和恢复技


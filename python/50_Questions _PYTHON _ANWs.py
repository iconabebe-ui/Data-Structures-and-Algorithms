#!/usr/bin/env python
# coding: utf-8

# # 1: Two Sum

# In[1]:


def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# # 2: Maximum Subarray (Kadane's Algorithm)

# In[2]:


def maxSubArray(nums):
    curr_sum = max_sum = nums[0]
    for num in nums[1:]:
        curr_sum = max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum


# # 3: Sort Colors (Dutch National Flag)

# In[6]:


def sortColors(nums):
    low, mid, high = 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# # 4: 4Sum

# In[8]:


def fourSum(nums, target):
    nums.sort()
    n, result = len(nums), []
    
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left, right = j+1, n-1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return result


# # 5: Merge Intervals

# In[9]:


def merge(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    
    return merged


# # 6: Minimum Remove to Make Valid Parentheses

# In[10]:


def minRemoveToMakeValid(s):
    stack = []
    to_remove = set()
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    
    to_remove.update(stack)
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)


# # 7: Sort Characters By Frequency

# In[11]:


from collections import Counter

def frequencySort(s):
    freq = Counter(s)
    sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
    return ''.join(char * count for char, count in sorted_chars)


# # 8: Permutation in String

# In[12]:


from collections import Counter

def checkInclusion(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
        return False
    
    s1_count = Counter(s1)
    s2_count = Counter(s2[:n1])
    
    for i in range(n2 - n1):
        if s1_count == s2_count:
            return True
        s2_count[s2[i]] -= 1
        if s2_count[s2[i]] == 0:
            del s2_count[s2[i]]
        s2_count[s2[i + n1]] += 1
    
    return s1_count == s2_count


# # 9: Palindrome Partitioning

# In[13]:


def partition(s):
    def is_palindrome(sub):
        return sub == sub[::-1]
    
    def backtrack(start, path):
        if start == len(s):
            result.append(path[:])
            return
        
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):
                path.append(substring)
                backtrack(end, path)
                path.pop()
    
    result = []
    backtrack(0, [])
    return result


# # 10: Minimum Window Substring

# In[14]:


from collections import Counter

def minWindow(s, t):
    need = Counter(t)
    missing = len(t)
    left = start = end = 0
    
    for right, char in enumerate(s, 1):
        missing -= need[char] > 0
        need[char] -= 1
        
        if missing == 0:
            while left < right and need[s[left]] < 0:
                need[s[left]] += 1
                left += 1
            
            if not end or right - left <= end - start:
                start, end = left, right
            
            need[s[left]] += 1
            missing += 1
            left += 1
    
    return s[start:end]


# # 11: Remove Linked List Elements

# In[15]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(0, head)
    curr = dummy
    
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return dummy.next


# # 12: Reverse Linked List

# In[17]:


def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    
    return prev


# # 13.Subsets

# In[18]:


def subsets(nums):
    result = [[]]
    
    for num in nums:
        result += [curr + [num] for curr in result]
    
    return result


# # 14: Generate Parentheses

# In[1]:


def generateParenthesis(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    result = []
    backtrack('', 0, 0)
    return result


# # 15: LRU Cache

# In[ ]:


class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self._add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# # 16: First Missing Positive

# In[21]:


def firstMissingPositive(nums):
    n = len(nums)
    
    # Place each number in its right position
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
            nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
    
    # Find first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


# # 17: Spiral Matrix

# In[22]:


def spiralOrder(matrix):
    if not matrix:
        return []
    
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    
    while top <= bottom and left <= right:
        # Left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        
        # Top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        
        # Bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    
    return result


# # 18: Valid Sudoku

# In[2]:


def isValidSudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue
            
            box_idx = (r // 3) * 3 + (c // 3)
            
            if (num in rows[r] or 
                num in cols[c] or 
                num in boxes[box_idx]):
                return False
            
            rows[r].add(num)
            cols[c].add(num)
            boxes[box_idx].add(num)
    
    return True


# # 19.Word Search

# In[ ]:


def exist(board, word):
    rows, cols = len(board), len(board[0])
    
    def dfs(r, c, index):
        if index == len(word):
            return True
        
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[index]:
            return False
        
        # Mark as visited
        temp = board[r][c]
        board[r][c] = '#'
        
        # Explore neighbors
        found = (dfs(r+1, c, index+1) or
                 dfs(r-1, c, index+1) or
                 dfs(r, c+1, index+1) or
                 dfs(r, c-1, index+1))
        
        # Restore cell
        board[r][c] = temp
        return found
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False


# # 20: Flatten Binary Tree to Linked List

# In[ ]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return
    
    stack = [root]
    prev = None
    
    while stack:
        curr = stack.pop()
        if prev:
            prev.right = curr
            prev.left = None
        
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        
        prev = curr


# # 21.Palindrome Linked List

# In[ ]:


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    # Compare both halves
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


# # 22.Reverse Nodes in k-Group

# In[ ]:


def reverseKGroup(head, k):
    def reverse(start, end):
        prev, curr = None, start
        while curr != end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        
        group_next = kth.next
        group_start = group_prev.next
        
        # Reverse current group
        kth.next = None
        reverse(group_start, group_next)
        
        # Connect reversed group
        group_prev.next = kth
        group_start.next = group_next
        
        group_prev = group_start


# # 23.Merge Two Sorted Lists

# In[ ]:


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    curr = dummy
    
    while list1 and list2:
        if list1.val <= list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    
    curr.next = list1 if list1 else list2
    return dummy.next


# # 24: Add Two Numbers

# In[ ]:


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


# # 25: Swap Nodes in Pairs

# In[ ]:


def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        
        # Swap
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
    
    return dummy.next


# # 26: Add Two Numbers

# In[ ]:


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    curr = dummy
    carry = 0
    
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = ListNode(total % 10)
        
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    
    return dummy.next


# # 27: Swap Nodes in Pairs

# In[ ]:


def swapPairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        
        # Swap
        prev.next = second
        first.next = second.next
        second.next = first
        
        prev = first
    
    return dummy.next


# # 28.Largest Rectangle in Histogram

# In[ ]:


def largestRectangleArea(heights):
    stack = []
    max_area = 0
    heights.append(0)  # Sentinel
    
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    
    return max_area


# # 29: Min Stack

# In[ ]:


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# # 30: Implement Stack using Queues

# In[ ]:


from collections import deque

class MyStack:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        self.queue.append(x)
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())

    def pop(self):
        return self.queue.popleft()

    def top(self):
        return self.queue[0]

    def empty(self):
        return len(self.queue) == 0


# # 31: BST Iterator

# In[ ]:


class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._leftmost_inorder(node.right)
        return node.val

    def hasNext(self):
        return len(self.stack) > 0


# # 32: Trapping Rain Water

# In[ ]:


def trap(height):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max = right_max = water = 0
    
    while left < right:
        if height[left] < height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1
    
    return water


# # 33: Maximum Depth of Binary Tree

# In[ ]:


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# # 34: Lowest Common Ancestor of Binary Tree

# In[ ]:


def lowestCommonAncestor(root, p, q):
    if not root or root == p or root == q:
        return root
    
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)
    
    if left and right:
        return root
    return left or right


# # 35: Kth Smallest Element in BST

# In[ ]:


def kthSmallest(root, k):
    stack = []
    curr = root
    
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        
        curr = stack.pop()
        k -= 1
        if k == 0:
            return curr.val
        
        curr = curr.right


# # 36: Binary Tree Level Order Traversal

# In[ ]:


from collections import deque

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    
    return result


# # 37: Sum Root to Leaf Numbers

# In[ ]:


def sumNumbers(root):
    def dfs(node, curr_sum):
        if not node:
            return 0
        
        curr_sum = curr_sum * 10 + node.val
        
        if not node.left and not node.right:
            return curr_sum
        
        return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
    
    return dfs(root, 0)


# # 38: Subtree of Another Tree

# In[ ]:


def isSubtree(root, subRoot):
    def isSame(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
    
    if not root:
        return False
    if isSame(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# # 39: Implement Trie (Prefix Tree)

# In[ ]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# # 40: Group Anagrams

# In[ ]:


from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    
    return list(anagrams.values())


# # 41.Subtree of Another Tree

# In[ ]:


def isSubtree(root, subRoot):
    def isSame(p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        return p.val == q.val and isSame(p.left, q.left) and isSame(p.right, q.right)
    
    if not root:
        return False
    if isSame(root, subRoot):
        return True
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


# # 42.Prefix Tree

# In[ ]:


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end
    
    def startsWith(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


# # 43: Bipartite Graph

# In[ ]:


def isBipartite(graph):
    n = len(graph)
    colors = [0] * n  # 0: uncolored, 1: red, -1: blue
    
    for i in range(n):
        if colors[i] == 0:
            colors[i] = 1
            stack = [i]
            
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if colors[neighbor] == 0:
                        colors[neighbor] = -colors[node]
                        stack.append(neighbor)
                    elif colors[neighbor] == colors[node]:
                        return False
    
    return True


# # 44: Flood Fill

# In[ ]:


def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    
    oldColor = image[sr][sc]
    rows, cols = len(image), len(image[0])
    stack = [(sr, sc)]
    
    while stack:
        r, c = stack.pop()
        if image[r][c] == oldColor:
            image[r][c] = newColor
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    stack.append((nr, nc))
    
    return image


# # 45: Number of Islands

# In[ ]:


def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return
        
        grid[r][c] = '0'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    
    return islands


# # 46: Clone Graph

# In[ ]:


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []

def cloneGraph(node):
    if not node:
        return None
    
    clones = {}
    
    def dfs(original):
        if original in clones:
            return clones[original]
        
        clone = Node(original.val)
        clones[original] = clone
        
        for neighbor in original.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


# # 47: Longest Increasing Path in Matrix

# In[ ]:


def longestIncreasingPath(matrix):
    if not matrix:
        return 0
    
    rows, cols = len(matrix), len(matrix[0])
    memo = [[0] * cols for _ in range(rows)]
    
    def dfs(r, c):
        if memo[r][c]:
            return memo[r][c]
        
        max_path = 1
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                max_path = max(max_path, 1 + dfs(nr, nc))
        
        memo[r][c] = max_path
        return max_path
    
    return max(dfs(r, c) for r in range(rows) for c in range(cols))


# # 48: Maximum Product Subarray

# In[ ]:


def maxProduct(nums):
    if not nums:
        return 0
    
    max_prod = min_prod = result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        
        result = max(result, max_prod)
    
    return result


# # 49: Longest Common Subsequence

# In[ ]:


def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n+1) for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[m][n]


# # 50: Unique Paths

# In[ ]:


def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]


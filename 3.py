# 找出不含有重复字符的 最长子串 的长度
# 滑动窗口入门题，枚举每个位置开始的最长子串
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substr = set() # 记录集合
        ans = 0
        right = 0
        for i in range(len(s)):
            if i != 0:
                substr.remove(s[i-1]) # 移除左指针之前的字符，从左指针处开始枚举
            while right < len(s) and s[right] not in substr:
                substr.add(s[right])
                right += 1
            ans = max(ans, right - i)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
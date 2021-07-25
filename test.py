class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) == 3:
            if s == s[::-1]:
                return 1
            else:
                return 0
        else:
            num_of_palindromes = 0
            unique = list(set(s))
            for char in unique:
                count = s.count(char)
                if count > 1:
                    # find first and last index of char in s
                    a_index = s.index(char)
                    c_index = s.rindex(char)
                    # find num of unique chars between the two indeces 
                    between = s[a_index+1:c_index]
                    num_of_palindromes += len(list(set(between)))
            return num_of_palindromes
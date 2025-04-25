class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Go through each character in the first string
        for i in range(len(strs[0])):
            char = strs[0][i]  # take character at index i

            # Compare it with the same position in other strings
            for word in strs[1:]:
                # If index out of range or mismatch
                if i >= len(word) or word[i] != char:
                    return strs[0][:i]  # return prefix up to i

        # If we finish the loop, the whole first word is common
        return strs[0]
class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        int n = s.length();
        int maxLength = 0;
        vector<int> charIndex(128, -1); // Assuming ASCII characters

        int left = 0;
        for (int right = 0; right < n; right++) 
        {
            char currentChar = s[right];
            if (charIndex[currentChar] != -1) 
            {
                left = max(left, charIndex[currentChar] + 1);
            }
            charIndex[currentChar] = right;
            maxLength = max(maxLength, right - left + 1);
        }
        
        return maxLength;
    }
};
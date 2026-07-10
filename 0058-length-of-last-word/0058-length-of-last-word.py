class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        clean_str = " ".join(s.split())

        last_word_length = 0

        print(clean_str)

        for i in range(len(clean_str)-1,-1,-1):
            if clean_str[i]!=" ":
                last_word_length += 1

            else:
                break

        return last_word_length
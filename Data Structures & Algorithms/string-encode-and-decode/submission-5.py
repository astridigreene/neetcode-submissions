class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        # s[0:2] - num strs
        # encoded =  str(len(strs)//100) + str(((len(strs) - len(strs)//100)//10)) + str(len(strs)%10)
        encoded = ""
        for i, string in enumerate(strs):
            encoded += str(len(string)//100) + str(((len(string) - (len(string)//100)*100)//10)) + str(len(string)%10)
            for j, letter in enumerate(string):
                ascii_val = ord(letter)
                val = str(ascii_val//100) + str((ascii_val - (ascii_val//100)*100)//10) + str(ascii_val%10)
                encoded += val
        return encoded

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        res = []
        count = 0
        length = int(s[0:3])
        curr_str = ""

        for i in range(3, len(s), 3):
            if count == length:
                count = 0
                length = int(s[i:i+3])
                res.append(curr_str)
                curr_str = ""
            else:
                curr_str += chr(int(s[i:i+3]))
                count += 1
        res.append(curr_str)

        return res

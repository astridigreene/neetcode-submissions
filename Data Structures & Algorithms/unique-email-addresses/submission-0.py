class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = set()
        for i, email in enumerate(emails):
            local = ""
            ignore = False
            for j, letter in enumerate(email):
                if letter == '@':
                    domain = email[j:]
                    break
                elif ignore or letter == '.':
                    continue
                elif letter == '+':
                    ignore = True
                else:
                    local += letter
            res.add(domain+local)
        return len(res)
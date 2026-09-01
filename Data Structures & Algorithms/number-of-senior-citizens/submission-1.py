class Solution:
    def countSeniors(self, details: List[str]) -> int:
        # 0-9 (phone), 10 (gender), 11-12 (age), 13-14 (seat)
        count = 0
        for i, arr in enumerate(details):
            print(int(arr[11:12]))
            if int(arr[11:13]) > 60:
                count += 1
        return count
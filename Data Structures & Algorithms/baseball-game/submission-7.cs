public class Solution {
    public int CalPoints(string[] operations) {
        int res = 0;
        int[] stack = new int[operations.Length * 2];
        int count = 0;
        for (int i = 0; i < operations.Length; ++i) {
            int score;
            if (operations[i] == "+") {
                score = stack[count-1] + stack[count-2];
                res += score;
                stack[count] = score;
                ++count;
            }
            else if (operations[i] == "D") {
                score = stack[count-1] * 2;
                res += score;
                stack[count] = score;
                ++count;
            }
            else if (operations[i] == "C") {
                res -= stack[count-1];
                --count;
            }
            else {
                score = int.Parse(operations[i]);
                res += score;
                stack[count] = score;
                ++count;
            }
            // Console.WriteLine($"{res}, {stack[count-1]} ");
        }
        return res;
    }
}
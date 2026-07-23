public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int max_count = 0;
        int curr_count = 0;
        for (int i = 0; i < nums.Length; ++i) {
            if (nums[i] == 0) {
                max_count = Math.Max(max_count, curr_count);
                curr_count = 0;
            }
            else ++curr_count;
        }
        max_count = Math.Max(max_count, curr_count);
        return max_count;
    }
}
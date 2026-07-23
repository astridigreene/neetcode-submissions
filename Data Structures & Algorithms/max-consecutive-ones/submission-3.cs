public class Solution {
    public int FindMaxConsecutiveOnes(int[] nums) {
        int max_count = 0;
        int curr_count = 0;
        for (int i = 0; i < nums.Length; ++i) {
            curr_count = (nums[i] == 0) ? 0 : curr_count + 1;
            max_count = Math.Max(max_count, curr_count);
        }
        return max_count;
    }
}
public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> nums_count = new HashSet<int>();
        foreach (int i = 0; i < nums.Length; ++i) {
            if (!nums_count.Add(nums[i])) {
                return true;
            }
        }
        return false;
    }
}
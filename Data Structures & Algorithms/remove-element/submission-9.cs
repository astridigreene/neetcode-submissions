public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int low = 0;
        for (int i = 0; i < nums.Length; ++i) {
            if (nums[i] != val) {
                nums[low] = nums[i];
                ++low;
            }   
        }
        return low;
    }
}
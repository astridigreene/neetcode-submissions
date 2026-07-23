public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int i = 0;

        int low = 0;
        while (i < nums.Length) {
            if (nums[i] != val) {
                nums[low] = nums[i];
                ++low;
            }   
            ++i;
        }
        // for (int j = 0; j < (nums.Length - low); ++j) {
        //     Console.Write($"{nums[j]} ");
        // }
        return low;
    }
}
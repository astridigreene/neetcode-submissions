public class Solution {
    public bool hasDuplicate(int[] nums) {
        // HashSet<int> nums_count = new HashSet<int>();
        // foreach (int num in nums) {
        //     if (!nums_count.Add(num)) {
        //         return true;
        //     }
        // }
        // return false;
        return new HashSet<int>(nums).Count < nums.Length;
    }
}
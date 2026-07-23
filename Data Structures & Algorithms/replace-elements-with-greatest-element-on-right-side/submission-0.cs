public class Solution {
    public int[] ReplaceElements(int[] arr) {
        int max = -1;
        for (int i = arr.Length - 1; i >= 0; --i) {
            int prev = arr[i];
            arr[i] = max;
            max = Math.Max(max, prev);
        }
        return arr;
    }
}
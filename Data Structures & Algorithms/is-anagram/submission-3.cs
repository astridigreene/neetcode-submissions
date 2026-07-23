public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length) return false;
        var letters = new Dictionary<char, int>();
        
        for (int i = 0; i < s.Length; ++i) {
            if (!letters.ContainsKey(s[i])) letters[s[i]] = 0;
            if (!letters.ContainsKey(t[i])) letters[t[i]] = 0;
            letters[s[i]]++;
            letters[t[i]]--;
        }

        foreach (int value in letters.Values) {
            if (value != 0) return false;
        }

        return true;
    }
}
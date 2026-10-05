public class Solution {
    public void ReverseString(char[] s) {
        int st = 0;
        int en = s.Length - 1;

        while (st < en) {
            char temp = s[st];
            s[st] = s[en];
            s[en] = temp;
            st += 1;
            en -= 1;
        }
    }
}
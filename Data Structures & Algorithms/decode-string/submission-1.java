
class Solution {
    public String decodeString(String s) {
        Stack<Integer> counts = new Stack<>();
        Stack<StringBuilder> resultStack = new Stack<>();
        StringBuilder curr = new StringBuilder();
        int num = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);

            if (Character.isDigit(ch)) {
                num = num * 10 + (ch - '0');
            }
            else if (ch == '[') {
                counts.push(num);
                resultStack.push(curr);
                num = 0;
                curr = new StringBuilder();
            }
            else if (ch == ']') {
                int repeat = counts.pop();
                StringBuilder temp = resultStack.pop();
                for (int j = 0; j < repeat; j++) {
                    temp.append(curr);
                }
                curr = temp;
            }
            else {
                curr.append(ch);
            }
        }

        return curr.toString();
    }
}

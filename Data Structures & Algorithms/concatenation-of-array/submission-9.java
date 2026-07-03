class Solution {
    public int[] getConcatenation(int[] nums) {
        int len = nums.length;
        int[] retVal = new int[len*2];

        int left = len;

        for (int i = 0; i < len; i++, left++){
            retVal[i] = nums[i];
            retVal[left] = nums[i];
        }
        return retVal;
    }
}
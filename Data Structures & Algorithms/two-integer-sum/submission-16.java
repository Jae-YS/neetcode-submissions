class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> diff = new HashMap<>();

        for (int i = 0; i < nums.length; i++){
            int val = nums[i];
            int difference = target - val;
            if (diff.containsKey(difference)){
                return new int[] { diff.get(difference), i };
            }

            diff.put(val, i);
        }
        throw new IllegalArgumentException("No two sum solution");
    }
}

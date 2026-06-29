class Solution {
    public boolean hasDuplicate(int[] nums) {
        ArrayList<Integer> check = new ArrayList<Integer>();

        for(int i=0; i < nums.length; i++){
            if(check.contains(nums[i])){
                return true;
            }
            else{
                check.add(nums[i]);
            }
        }
        return false;
    }
}
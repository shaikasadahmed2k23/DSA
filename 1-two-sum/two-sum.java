class Solution {
    public int[] twoSum(int[] nums, int target) {
        // for(int i = 0; )
        int n = nums.length;
        for(int i = 0 ; i < n ; i++)
        {
            for(int j = i+1 ; j < n ; j++)
            {
                if(nums[i] + nums[j] == target)
                {
                    // int x = nums[i];
                    // int y = nums[j];
                    // break;
                        return new int[]{i,j};

                }
            }
        }
                    return new int[]{}; 

    }

    
}   
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int totalLength = nums1.Length + nums2.Length;

        if (totalLength == 0)
        {
            return 0;
        }

        if (totalLength == 1)
        {
            return nums1.Length == 1 ? nums1[0] : nums2[0];
        }

        int numbersToGet = (totalLength/2) + 1;
        int nums1Index = 0;
        int nums2Index = 0;
        int left = 0; 
        int right = 0;

        for (int i = 0; i < numbersToGet; i++)
        {
            left = right;
            if (nums2Index >= nums2.Length || (nums1Index < nums1.Length && nums1[nums1Index] <= nums2[nums2Index]))
            {
                right = nums1[nums1Index];
                nums1Index++;
            } 
            else
            {
                right = nums2[nums2Index];
                nums2Index++;
            }
        }

        if (totalLength % 2 == 0)
        {
            
            return (double)(left+right)/2;
        }

        // Last number retrieved is the exact midpoint
        return right;
    }
}

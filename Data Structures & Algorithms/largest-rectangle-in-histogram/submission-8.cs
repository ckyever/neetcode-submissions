public class Solution {
    public int LargestRectangleArea(int[] heights) {    
        int[] sortedHeights = heights.OrderByDescending(height => height).ToArray();
        int largestHeight = sortedHeights[0];

        int maxArea = 0;

        for (int currentHeight = 1; currentHeight <= largestHeight; currentHeight++)
        {
            int longestWidth = 0;
            int currentWidth = 0;
            for (int i = 0; i < heights.Length; i++)
            {
                if (heights[i] >= currentHeight)
                {
                    currentWidth++;
                }
                else
                {
                    longestWidth = Math.Max(longestWidth, currentWidth);
                    currentWidth = 0;
                }
            }
            longestWidth = Math.Max(longestWidth, currentWidth);
            maxArea = Math.Max(maxArea, (longestWidth * currentHeight));
        }

        return maxArea;
    }
}

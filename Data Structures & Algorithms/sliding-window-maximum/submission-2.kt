class Solution {
    fun maxSlidingWindow(nums: IntArray, k: Int): IntArray {
        val output = mutableListOf<Int>()

        for (i in 0..nums.size - k) {
            var maxi = nums[i]
            for (j in i until i + k) {
                maxi = maxOf(maxi, nums[j])
            }
            output.add(maxi)
        }

        return output.toIntArray()
    }
}
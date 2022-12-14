class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
	    arr = {}
	    for i in range(left, right+1):
	    	arr[i] = False
	    for i in arr:
	    	for left, right in ranges:
	    		if left <= i and i <= right:
	    			arr[i] = True
	    			break
	    	if arr[i] == False:
	    		return False
	    return True
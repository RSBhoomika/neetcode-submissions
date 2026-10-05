class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        
        # Step 1: Sort intervals by their end times
        intervals.sort(key=lambda x: x[1])
        
        # Step 2: Track the end time of the last non-overlapping interval
        prev_end = intervals[0][1]
        remove_count = 0
        
        # Step 3: Iterate through the remaining intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            # If the current interval starts before the previous one ends, it's an overlap
            if start < prev_end:
                remove_count += 1
            else:
                # No overlap, update the valid end boundary
                prev_end = end
                
        return remove_count

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        count = Counter(ages)
        ans = 0
        for age_x, count_x in count.items():
            for age_y, count_y in count.items():
                if age_y>0.5*age_x+7 and age_y<=age_x:
                    if age_x == age_y:
                        ans+=count_x*(count_x-1)
                    else:
                        ans+=count_x*count_y
        return ans
        
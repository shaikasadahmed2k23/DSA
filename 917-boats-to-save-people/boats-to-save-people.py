class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        # y = sorted(people)
        # print(y)
        people.sort()

        l = 0
        h = len(people) - 1
        c = 0

        while l <= h:
            if people[l] + people[h] <= limit:
                l += 1
                h -= 1
            else:
                h -= 1

            c += 1

        return c
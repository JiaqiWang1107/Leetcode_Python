class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
            x = -x
        while x > 0:
            value = x % 10
            result = result * 10 + value
            x = int(x/10)
        if result > 2147483647 or result < -2147483647: # don't forget this part
            result = 0

        return result * sign




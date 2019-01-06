class Solution(object):
    def convert(self, s, numRows):

        result = ""
        length = len (s)
        n = numRows
        cycle =  2 * n - 2
        if n == 1:
            return s
        i = 0
        x = 0
        while len(result) < length:
            if cycle * x +i > length - 1:
                i = i + 1
                x = 0
            zig = cycle * x + i
            zag = cyele * (x+1) -  i
            if i == 0 or i ==  n - 1:
               result += s[zig]
            else:
               if zag > length - 1:
                  result += s[zig]
               else:
                  result += s[zig] + s[zag]
            x += 1
        return result


def excute():
    sol =  Solution()
    print (sol.convert("PPFEFWEFEW", 4))




"""
  :type s: str
  :type numRows: int
  :rtype: str
  """
"""
思路：

找到循环规律，然后按照一行一行写


0          0                          2n-2              4n-4            6n  
1          1                   2n-3   2n-1             .
2          2               2n-4       2n             .
3          3             .            2n+1         .
4          4           .                         .
5                  n+1                         .
n-2       n-2   n                           .                 
n-1       n-1                         3n-3              5n-5

cycle =  2n - 2
value (zig, zag)
row i :  
zig = cycle * x + i
zag = cycle * (x+1) -i

row = 0 and n-1 there is no zag
if n = 1 return initial string
"""
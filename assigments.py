+Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> listx = [1,2,3,4,5,6,7,8,9]
>>> listx.append(3)
>>> listx.remove(4)
>>> listx.insert(2, -1)
>>> listx
[1, 2, -1, 3, 5, 6, 7, 8, 9, 3]
>>> 
>>> 
>>> listx.reverse()
>>> listx
[3, 9, 8, 7, 6, 5, 3, -1, 2, 1]
>>> listx.extend(11,12)

>>> listx.extend([11,12]);
>>> listx
[3, 9, 8, 7, 6, 5, 3, -1, 2, 1, 11, 12]
>>> listx.pop()
12
>>> listx.index(5)
5
>>> listx.sort()
>>> listx
[-1, 1, 2, 3, 3, 5, 6, 7, 8, 9, 11]
>>> listx.count([-1, 1, 2, 3, 3, 5, 6, 7, 8, 9, 11])
0
>>> 
>>> 
>>> listy = [x*10 for x in (listx)]
>>> listy
[-10, 10, 20, 30, 30, 50, 60, 70, 80, 90, 110]
>>> 
>>> 
>>> k = (listx[0:5])
>>> k
[-1, 1, 2, 3, 3]
>>> 
>>> 
>>> u = (listx[5:])
>>> u
[5, 6, 7, 8, 9, 11]
>>> 
>>> 
>>> n = [[1,2,3], [4,5,6], [7,8,9]]
>>> 
>>> m = [1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> m.append(n)
>>> m
[1, 2, 3, 4, 5, 6, 7, 8, 9, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
>>> 

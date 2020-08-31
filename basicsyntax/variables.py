"""
table
object reference count
"""

a = "nyc"
b = "nyc"
print(a)
"""
table
object  reference   count
nyc     a,b         2
"""

a= 123
print(a)
print(b)
"""
table
object  reference count
nyc     b         1
123     a         1
"""

b=456
"""
table
object  reference   count
nyc                 0
123     a           1
456     b           1
Since reference count of nyc is 0, nyc will be trashed
"""

c="nyc"
d=c
print(c==d)
print(d is c)
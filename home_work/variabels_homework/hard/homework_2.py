A,B = map(float,input("Enter 2 Number: ").split())

print((B + 1 ) * A**2 / 2 +( 2 * A + 1) * (1 - B) / 2)

"""
when i asked chatgpt

i got this formula
((B + 1 ) * A**2 / 2 +( 2 * A + 1) * (1 - B) / 2)

and the idea is we have 2 options 
one for happy mode one for  sad mode

the trick is (B + 1)
when we  enter 1 as B and it becom (1 + 1) >> 2
so this help to pick the square the number option
when sad mode happend  when B = -1 it become >> 0

the second trick is with (1 - B)
it' same with B + 1 but in The opposite way

case 1 : happy mode
(1 + 1 ) * 7**2 / 2 = 49

second part

( 2 * 7 + 1) * (1 - 1) = 15 * 0 = 0

49 + 0 = 49

so in this case we squared A**2 in happy mode
2A + 1 sad mode
"""

"""
student name : Muhammad Khalaf Muhamamd
email : muhammadkhalaf195@gmail.com
"""
"""
# Que.1 WAP to print half Diamond star pattern
*
**
***
****
*****
******
*****
****
***
**
*

for i in range(5):
    for j in range(0, i + 1):
        print('*', end='')
    print()
for i in range(1, 5):
    for j in range(i, 5):
        print('*', end='')
    print()
=============================================================

# Que.2 WAP to Print K using Alphabets
A B C D
A B C
A B
A
A
A B
A B C
A B C D

n = 3
v = n
while v >= 0:
    c = 65
    for j in range(v + 1):
        print(chr(c + j), end=' ')
    v = v - 1
    print()
for i in range(n + 1):
    c = 65
    for j in range(i + 1):
        print(chr(c + j), end=' ')
    print()
==============================================================

# Que.3 WAP to print the diamond shape
    *
   * *
  * * *
 * * * *
* * * * *
* * * * *
 * * * *
  * * *
   * *
    *

n = 0
rows = 5
for i in range(1, rows + 1):
    for j in range(1, (rows - i) + 1):
        print(end=' ')
    while n != (2 * i - 1):
        print('*', end='')
        n = n + 1
    n = 0
    print()

k = 1
n = 1
for i in range(1, rows):
    for j in range(1, k + 1):
        print(end=' ')
    k = k + 1
    while n <= (2 * (rows - i) - 1):
        print('*', end='')
        n = n + 1
    n = 1
    print()
=================================================================

# Que.4 WAP to Print an Inverted Star Pattern
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *

n = 10
for i in range(n, 0, -1):
    print((n - i) * ' ' + i * '*')
============================================================

# Que.5 WAP to print digit pattern
|****
|*
|***
|**
|*****

n = '41325'
for i in n:
    print('|', end='')
    print('*' * int(i))
===============================================================

# Que.6 WAP Print Heart Pattern
  *   *   *   *
*       *       *
*               *
*     S A S     *
  *           *
    *       *
      *   *
        *

n = 8
m = n + 1
for i in range(n // 2 - 1):
    for j in range(m):
        if i == n // 2 - 2 and (j == 0 or j == m - 1):
            print('*', end=' ')
        elif j <= m // 2 and ((i + j == n // 2 - 3 and j <= m // 4)
                              or (j - i == m // 2 - n // 2 + 3 and j > m // 4)):
            print('*', end=' ')
        elif j > m // 2 and ((i + j == n // 2 - 3 + m // 2 and j < 3 * m // 4)
                             or (j - i == m // 2 - n // 2 + 3 + m // 2 and j >= 3 * m // 4)):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(n // 2 - 1, n):
    for j in range(m):
        if (i - j == n // 2 - 1) or (i + j == n - 1 + m // 2):
            print('*', end=' ')
        elif i == n // 2 - 1:
            if j == m // 2 - 1 or j == m // 2 + 1:
                print('S', end=' ')
            elif j == m // 2:
                print('A', end=' ')
            else:
                print(' ', end=' ')
        else:
            print(' ', end=' ')
    print()
=============================================================

# Que.7 WAP to right rotate n-numbers by 1
1 2 3 4
2 3 4 1
3 4 1 2
4 1 2 3

n = 4
for i in range(1, n + 1, 1):
    for j in range(1, n + 1, 1):
        if i == j:
            print(j, end=' ')
            if i <= j:
                for k in range(j + 1, n + 1, 1):
                    print(k, end=' ')
            for p in range(1, j, 1):
                print(p, end=' ')
    print()
=========================================================

# Que.8 WAP to print window pattern
* * * * * * *
*     *     *
*     *     *
* * * * * * *
*     *     *
*     *     *
* * * * * * *

def window_pattern(n):
    if n % 2 != 0:
        c = (n // 2) + 1
        d = 0
    else:
        c = (n // 2) + 1
        d = (n // 2)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == 1 or j == 1 or i == n or j == n:
                print('*', end=' ')
            else:
                if i == c or j == c:
                    print('*', end=' ')
                elif i == d or j == d:
                    print('*', end=' ')
                else:
                    print(' ', end=' ')
        print()


n = 7
window_pattern(n)
===========================================================

# Que.9 WAP to print hollow half diamond hash pattern
#
# #
#   #
#     #
#       #
#     #
#   #
# #
#

N = 5
for i in range(1, N + 1):
    for j in range(1, i + 1):
        if i == j or j == 1:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()
for i in range(N - 1, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or i == j:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print()
=================================================================

# Que.10 WAP to display half diamond pattern of numbers with star border
*
*1*
*121*
*12321*
*121*
*1*
*


def display(n):
    print('*')
    for i in range(1, n + 1):
        print('*', end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print('*', end='')
        print()
    for i in range(n - 1, 0, -1):
        print('*', end='')
        for j in range(1, i + 1):
            print(j, end='')
        for j in range(i - 1, 0, -1):
            print(j, end='')
        print('*', end='')
        print()
    print('*')


display(3)
=============================================================

# Que.11 WAP Simple Diamond Pattern
  * * *
* * * * *
  * * *
    *

size = 5
spaces = size
for i in range(size // 2 + 2):
    for j in range(size):
        if j < i - 1:
            print(' ', end=' ')
        elif j > spaces:
            print(' ', end=' ')
        elif (i == 0 and j == 0) | (i == 0 and j == size - 1):
            print(' ', end=' ')
        else:
            print('*', end=' ')
    spaces -= 1
    print()
===================================================

# Que.12 WAP to print Pascal’s Triangle
      1
     1 1
    1 2 1
   1 3 3 1
  1 4 6 4 1

from math import factorial as f
n = 5
for i in range(n):
    for j in range(n - i + 1):
        print(end=' ')

    for j in range(i + 1):
        print(f(i) // (f(j) * f(i - j)), end=' ')
    print()
=======================================================

"""

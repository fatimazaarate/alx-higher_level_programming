#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, div, mul

a = 10
b = 5

sum = add(a, b)
print("{} + {} = {}" .format(a, b, sum))

subs = sub(a, b)
print("{} + {} = {}" .format(a, b, subs))

multi = mul(a, b)
print("{} + {} = {}" .format(a, b, multi))

division = div(a, b)
print("{} + {} = {}" .format(a, b, division))

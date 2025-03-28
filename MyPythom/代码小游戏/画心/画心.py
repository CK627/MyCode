from turtle import *
from math import *
color('red')
tracer(1)
begin_fill()
adx_x = -100
while (adx_x < 101):
    adx_a = sqrt(1-pow(adx_x/100,2))
    adx_b = pow(pow(adx_x/100,2),1/3)
    goto(adx_x,(adx_a+adx_b)*50)
    goto(adx_x,(-adx_a+adx_b)*50)
    adx_x += 1
end_fill()
done()
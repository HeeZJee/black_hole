import math as m
from decimal import Decimal as dec
pi = m.pi
dec = dec(pi)
G = 6.6262e-11
a = input("enter semi major axis: ") #143616000000000
t =input("Enter orbital period: ") #491961600
a_cube = pow(float(a),3)
t_sqr = pow(float(t),2)
mass1= 4*pow(float(pi),2)*a_cube
mass2 = G*t_sqr
mass = mass1/mass2
print("mass is ", str(mass))
mass_of_sun = 1.9891e30

solar_mass = mass/mass_of_sun
print('its equal to %s solar masses'%mass_solar)
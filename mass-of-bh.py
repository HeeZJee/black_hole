import scipy.constants as sc
from decimal import Decimal as dec

_pi = sc.pi             #pi
pi = dec(_pi)

_speed_of_light = sc.c      #Speed of Light
c = dec(_speed_of_light)

_G = sc.G                   #Gravitational Cosntant 
G = dec(_G)


d_unit = input('which unit you will like to you use \nAU or meters?\n')

if d_unit == 'au' or unit == 'AU':
    r_peri = dec( input("Enter radius at peristron: ")) #120
    r_appi = dec( input("Enter radius at apustron: ")) #1800
    r_peri_AU = dec(r_peri*149597900000)
    r_appi_AU = dec(r_appi*149597900000)
elif unit  == 'meters' or unit == 'meter' or unit == 'm' :
    r_appi = dec( input("Enter radius at apustron: "))
    r_peri = dec( input("Enter radius at periastron: "))
else:
    print("Invalid unit") 
#t_unit = input('Enter unit for time period')
#if t_unit == 'years' or t == 'year' or t == 'yrs' or t == 'yr':
    t_yr = dec( input("Enter orbital period: ")) #491961600
    t = dec(t_yr*dec(sc.year))

print("time is ",t)

m_axis =  dec(pow(r_peri,3)+ 3*(pow(r_peri,2))*r_appi+ 3*r_peri*(pow(r_appi,2))+ pow(r_appi,3))
t_sqr = pow(t,2)
mass1= pow(pi,2)*pow(m_axis,3)
mass2 = 2*G*t_sqr
mass = mass1/mass2

print("mass is of object is %s kg" %mass)

m_sun = 1.9889200011445836e30
mass_of_sun = dec(m_sun)
solar_mass = mass/mass_of_sun
print('Its equal to %s solar masses.'%solar_mass)
import scipy.constants as sc
from decimal import Decimal as dec


_pi = sc.pi             #pi
pi = dec(_pi)

_speed_of_light = sc.c      #Speed of Light
c = dec(_speed_of_light)

_G = sc.G                   #Gravitational Cosntant 
G = dec(_G)


d_unit = input('which unit you will like to you use \nAU or meters?\n')

if d_unit == 'au' or d_unit == 'AU':
    r_periAU = dec( input("Enter radius at peristron: ")) #120
    r_appiAU = dec( input("Enter radius at apustron: ")) #1800
    r_appi = dec(r_appiAU*149597900000)
    r_peri = dec(r_periAU*149597900000)
elif d_unit  == 'meters' or d_unit == 'meter' or d_unit == 'm' :
    r_appi = dec( input("Enter radius at apustron: "))
    r_peri = dec( input("Enter radius at periastron: "))
else:
    print("Invalid unit") 

#t_unit = input('Enter unit for time period')
#if t_unit == 'years' or t == 'year' or t == 'yrs' or t == 'yr':
t_yr = dec( input("Enter orbital period: ")) #491961600
t = dec(t_yr*dec(sc.year))




mass1= pow(pi,2)*pow(r_appi+r_peri,3)
mass2 = 2*G*pow(t,2)
mass = dec(mass1/mass2)

print("mass is of object is %s kg" %mass)

m_sun = 1.9889200011445836e30
mass_of_sun = dec(m_sun)
solar_mass = dec(mass/mass_of_sun)
print('Its equal to %s solar masses.'%solar_mass)
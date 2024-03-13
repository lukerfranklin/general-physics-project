"""
General physics project - nuclear fission model

Author: Luke Franklin
Last updated: 13/03/2024
"""
import numpy as np
import matplotlib.pyplot as plt

def reactions_produced(fuel_concentration, neutrons):
    # conc is a percentage
    return np.multiply(fuel_concentration, neutrons)

def neutrons_produced(fuel_left, neutrons):
    # fuel_left is a percentage first called with enrichment %
    temp = np.multiply(2.5, reactions_produced(fuel_left, neutrons))
    #print("temp ", temp)
    return temp

def no_of_unkown(total_particles, percentage_of_fuel):
    return total_particles * (1-percentage_of_fuel)

def mass_to_particles(mass, atomic_mass):
    return np.multiply(mass, AVOGADRO_CONSTANT)/atomic_mass

def show_stuff(neutrons, fuel_particles):
    print("neutrons: ", neutrons, "\nfuel particles left: ", fuel_particles)
    return 0

# PARAMETERS TO VARY
INITIAL_NO_OF_NEUTRONS = 10.0**23
INITIAL_MASS = 10**3 # grams
ENRICHMENT_PERCENTAGE = np.float64(0.03)

# constants
AVOGADRO_CONSTANT = 6.022*10**23
INITAL_FUEL_PARTICLES = np.multiply(ENRICHMENT_PERCENTAGE, mass_to_particles(INITIAL_MASS,235))
INITIAL_PARTICLES = mass_to_particles(INITIAL_MASS)
INITIAL_UNKNOWN_PARTICLES = no_of_unkown(INITIAL_PARTICLES, ENRICHMENT_PERCENTAGE)

no_of_neutrons = INITIAL_NO_OF_NEUTRONS
fuel_particles = INITAL_FUEL_PARTICLES
remaining_fuel = ENRICHMENT_PERCENTAGE
no_of_unkown_particles = no_of_unkown(INITIAL_PARTICLES, ENRICHMENT_PERCENTAGE)
energy=0
iterator=0

energy_array = []
iterator_array = []


while(no_of_neutrons>1):
    fuel_particles -= no_of_neutrons*remaining_fuel
    print("fuel particles: ", fuel_particles)
    no_of_neutrons = neutrons_produced(remaining_fuel, no_of_neutrons)
    print("no of neutrons: ", no_of_neutrons)
    no_of_unkown_particles = (2 *fuel_particles) + INITIAL_UNKNOWN_PARTICLES
    print("no of unkown particles: ", no_of_unkown_particles)
    remaining_fuel = fuel_particles / (fuel_particles + no_of_unkown_particles)
    print("remaining fuel: ", remaining_fuel)
    energy = 212*(no_of_neutrons / 2.5)*10**-19
    energy_array.append(energy)
    print("energy: ", energy)
    iterator += 1
    iterator_array.append(iterator)
    print("it: ", iterator)
    
print("e array: ", energy_array)
print("it array ", iterator_array)
    
plt.plot(iterator_array, energy_array)
plt.show()

#show_stuff(no_of_neutrons, fuel_particles)
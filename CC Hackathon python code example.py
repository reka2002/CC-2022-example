### Solving Primary School chemistry exercises in Python:


## Exercise 1
# How would you make 4 kg of 15% w/w NaCl solution?

# Converting the mass of the solution to g from kg:
mass_solution = 4 * 1000  # [kg * g / kg]
# Mass percentage is given by:
mass_percentage = 15/100  # [ % ]
# Computing the mass of the solute:
mass_solute = mass_percentage * mass_solution  # [g]
# Computing the mass of the solvent:
mass_solvent = mass_solution-mass_solute  # [g]

## Exercise 2
# An unknown metal reacts with chlorine gas.
# Of the 5.75 grams of metal, 14.625 g is metal chloride.
# 2 moles of metal react with 1 mole of chlorine gas.
# Which metal is it?

# Let Me represent metal.
# 2 Me + 1 Cl₂ = 2 MeCl --> Me has the charge of + 1  --> alkali metal, therefore it can be found
# under column I in the periodic table.

# The mass of the metal is given by:
mass_Me = 5.75  # [g]
# The mass of the metal chloride is:
mass_MeCl = 14.625  # [g]
# Computing the mass of the chlorine gas:
mass_Cl2 = mass_MeCl - mass_Me  # [g]
# Knowing that the Molar mass of the chlorine gas is:
Molar_mass_Cl2 = 71  # [g / mole]
# Computing the mole number of the chlorine gas:
mole_Cl2 = mass_Cl2 / Molar_mass_Cl2  # [mole]
# With 1 mole chlorine gas, 2 moles of metal will react, therefore,
# the mole number of the metal will be:
mole_Me = mole_Cl2 * 2   # [mole]
# Now, we can find the molar mass of the metal:
M_Me = mass_Me / mole_Me  #  [g/mole]

# Based on the molar mass, we can find which is this metal from the periodic table.


# Print the calculated values for Exercise 1:
print("\n For Exercise 1: ")
print("Mass of the solution, mass_solution: ", f"{mass_solution}", " [g]")
print("Mass percentage:, mass_percentage: ", f"{mass_percentage}", " [%]" )
print("Mass of the solute:, mass_solute: ", f"{mass_solute}", " [g]" )
print("GMass of the solvent: , mass_solvent: ", f"{mass_solvent}", " [g]\n")

# Print the calculated values for Exercise 2:
print("\n For Exercise 2: ")
print("Mass of the chlorine gas, mass_Cl2: ", f"{mass_Cl2}", " [g]")
print("Mole of the chlorine gas, mole_Cl2: ", f"{mole_Cl2}", " [g]")
print("Mole of the metal, mole_Me: ", f"{mole_Me}", " [g]")
print("Molar mass of the metal, M_Me: ", f"{M_Me}", " [g]")




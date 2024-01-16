# # Toetsgroep AI
# # Bloeddruk behandeling



# Input: 
medicatie_lijst = ['hydrochloortiazide', 'enalapril', 'amlodipine']
rr_syst = 150
print(f'Oude medicatie lijst: {medicatie_lijst}')
print(f'Bovendruk: {rr_syst}')


# Gegevens verwerking:
if rr_syst > 140:
    medicatie_lijst.append('metoprolol')
elif rr_syst < 110:
    medicatie_lijst.pop()
else:
    pass
print()


# Output:
print(f'Nieuwe medicatie lijst: {medicatie_lijst}')
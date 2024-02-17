# # Toetsgroep AI
# # Bloeddruk behandeling
print('----------------------------------------------------------------')
medicatie_lijst = ['hydrochloortiazide', 'enalapril', 'amlodipine']

while True:
    # Gegevens: 
    rr_syst = int(input('Wat is de systolische druk? '))
    print(f'\tOude medicatie lijst: {medicatie_lijst}')
    print(f'\tBovendruk: {rr_syst}')


    # Verwerking:



    # Uitkomst:
    medicatie_lijst = behandeling(med_lijst=medicatie_lijst, bovendruk=rr_syst)
    print(f'\tNieuwe medicatie lijst: {medicatie_lijst}')
    print('----------------------------------------------------------------', end="\n\n")
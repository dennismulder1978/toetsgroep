# # Toetsgroep AI
# # Bloeddruk behandeling
print('----------------------------------------------------------------')
medicatie_lijst = ['hydrochloortiazide', 'enalapril', 'amlodipine']

while True:
    # Gegevens: 
    rr_syst = int(input('Wat is de systolische druk? '))
    print(f'\tHuidige medicatie lijst: {medicatie_lijst}')
    print(f'\tBovendruk: {rr_syst}')


    # Verwerking:
    def behandeling(med_lijst, bovendruk):
        if (bovendruk > 140): 
            print('\tToevoegen van metoprolol.')
            med_lijst.append('metoprolol')
        elif (bovendruk < 105) & (len(med_lijst)>= 1):
            print('\tVerwijderen van laatste medicijn.')55
            
            med_lijst.pop()
        elif (bovendruk < 105) & (len(med_lijst)==0):
            print('Ambulance!!!!')
        else:
            print('\tGeen aanpassing nodig.')
        return med_lijst


    # Uitkomst:
    medicatie_lijst = behandeling(med_lijst=medicatie_lijst, bovendruk=rr_syst)
    print(f'\tNieuwe medicatie lijst: {medicatie_lijst}')
    print('----------------------------------------------------------------', end="\n\n")
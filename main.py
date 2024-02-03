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
    def behandeling(med_list, bovendruk):
        if bovendruk > 140:
            print('\tToevoegen van metoprolol.')
            med_list.append('metoprolol')
        elif bovendruk < 105:
            print('\tVerwijderen van laatste medicatie.')
            med_list.pop()
        else:
            print('\tGeen aanpassing nodig.')
        return med_list


    # Uitkomst:
    medicatie_lijst = behandeling(med_list=medicatie_lijst, bovendruk=rr_syst)
    print(f'\tNieuwe medicatie lijst: {medicatie_lijst}')
    print('----------------------------------------------------------------', end="\n\n")

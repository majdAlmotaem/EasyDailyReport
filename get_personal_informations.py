def get_personal_informations():
    name = input("Name: ")
    ausbildugsberuf = input("Ausbildungsberuf: ")
    geschaeftsbereich = input("Geschäftsbereich: ")
    ausbildungsjahr = input("Ausbildungsjahr: ")
    personal_informations = name,  ausbildugsberuf, geschaeftsbereich, ausbildungsjahr
    return personal_informations
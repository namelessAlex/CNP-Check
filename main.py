from cnp import CNP, Persoana, Angajat
# in primul rand tu ai denumit acest fisier main, dar tu de fapt nu ai nici un main in el 
#ca sa fie main, trebuie sa ai 
#def main(): 
    #si apoi aici ce mai vrei tu sa faci

# functia de mai jos, nu o lasi in main, cred ca o poti pune in acelasi fisier cu clasele 
# si cred ca poate fi chiar metoda noua in ultima clasa si apoi in acest main al tau , doar o apelezi

# Crearea obiectelor și utilizarea claselor
def show_details_for_person(person):
    try:
        cnp_person = CNP(person.cnp)
        nume = person.nume
        prenume = person.prenume
        cnp_person.check_length()
        sex = cnp_person.check_sex()
        dd = cnp_person.get_dd()
        mm = cnp_person.get_mm()
        yy = cnp_person.get_yy()
        cnp_person.check_cc()
        cc = cnp_person.get_cc()
        year = cc + yy
        luna = cnp_person.check_month()
        cnp_person.get_jj()
        county = cnp_person.check_county()
        cnp_person.check_nnn()

        output = f'''
    {nume} {prenume}, de sex {sex}, 
    nascut la data de: ziua {dd}, luna {luna}, anul {year}
    in judetul {county}
              '''
        print(output)
    except InvalidCNPError as e:
        print(f"Error: {e}")
    
# adica tu in main ar trebui sa ai doar partea de mai jos 
# Obiect de tip Persoana
persoana1 = Persoana("1900102410020", "Popescu", "Ion")
show_details_for_person(persoana1)

# Obiect de tip Angajat
angajat1 = Angajat("1900102410022", "Ionescu", "Maria", "Programator")
show_details_for_person(angajat1)

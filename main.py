from cnp import CNP, Persoana, Angajat

# Crearea obiectelor și utilizarea claselor
def show_details_for_person(person):
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
    

# Obiect de tip Persoana
persoana1 = Persoana("1900102410020", "Popescu", "Ion")
show_details_for_person(persoana1)

# Obiect de tip Angajat
angajat1 = Angajat("1900102410022", "Ionescu", "Maria", "Programator")
show_details_for_person(angajat1)
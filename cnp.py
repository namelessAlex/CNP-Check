import sys # poti renunta la el, in locul lui, poti adauga o exceptie

class InvalidCNPError(Exception):
    pass

class CNP:
    #add a doc string 
    def __init__(self, cnp): #nume mai clare pentru variabile 
        self.cnp = cnp
        self.cc = None
        self.gender = None  
        self.month = None
        self.day = None
        self.jj = None
        self.first_char = None
        #new empty line
    def check_length(self):
        # Logica pentru validarea CNP-ului -> in EN
        #poti simplifica toata partea asta ca mai jos
        length_of_cnp = len(self.cnp)
        if length_of_cnp == 13:
            valid_leng = "length ok"
        else:
            sys.exit(print(f'Length of CNP not ok: length of {length_of_cnp}') )  
        return 

        #varianta simplificata
        if len(self.cnp) != 13:
            raise InvalidCNPError(f'Length of CNP not ok: length of {len(self.cnp)}')
    
    # validare primul caracter din CNP pentru a obtine ccul si sexul persoanei -> in EN
    def check_sex(self):
        first_char = int(self.cnp[0])
        self.first_char = first_char
        #de aici incolo as rescrie sub forma de mai jos si din ce stiu sunt cnpuri si cu 7,8,9, 
        first_char_list = [1,2,3,4,5,6]
        gender_list = ['masculin','feminin']
        if first_char in first_char_list:

            if first_char in (1,3,5):
                return gender_list[0]
            else:
                return gender_list[1]
        else:
            sys.exit(print(f'def validare_sex error, first char not in range(1 thru 6): {first_char}') )    

        #varianta 
        gender_list = ['masculin', 'feminin']
        
        if first_char in (1, 3, 5):
            self.gender = gender_list[0]
        elif first_char in (2, 4, 6):
            self.gender = gender_list[1]
        else:
            raise InvalidCNPError(f'Invalid first character: {first_char}')
        return self.gender
    #new empty line
    def check_cc(self): #ce e cc? nume mai clare pentru functii + comment pentru ce faci in functia asta 
        cc_list = ['18','19','20'] #redenumeste mai clar cc
        if self.first_char in (1,2):
            self.cc = cc_list[self.first_char]
        elif self.first_char in (3,4):
            self.cc = cc_list[self.first_char]
        elif self.first_char in (5,6):
            self.cc = cc_list[self.first_char]   
        #adauga si else + variantele pentru 7,8,9 , 7,8 erau tot sexe... si 9 parca era pentru cetateni nerezidenti
        else:
            raise InvalidCNPError(f"Invalid first character for century calculation: {self.first_char}")
            
        # data nastere  - ce ai vrut sa spui aici?
    def get_cc(self):
        if self.cc:
            return self.cc
        else:
            sys.exit(print(f'Century unknown: {self.cc}') )  #replace with    raise InvalidCNPError(f'Century unknown: {self.cc}')
            #new empty line
    def get_yy(self):    
        # in loc de cele 2 linii poti sa pui pur si simplu return self.cnp[1:3]
        year = self.cnp[1] + self.cnp[2] 
        return year
        #new empty line
    def get_mm(self):  
        self.month = self.cnp[3] + self.cnp[4] # aici la fel, poti pune int(self.cnp[3:5])
        return self.month
        #new empty line
    def get_dd(self):             
        day = self.cnp[5] + self.cnp[6] #la fel, int(self.cnp[5:7])
        self.day = int(day) # o poti scoate
        #tot codul de mai jos il poti rescrie astfel:
        if self.day in range(1,32): 
            return day
        else:
            sys.exit(print(f'def get_dd error: {self.day}') )
        #varianta
        if self.day not in range(1, 32):
            raise InvalidCNPError(f'Invalid day: {self.day}')
        return self.day
        #new empty line
    def get_jj(self): #nume mai clar la functie 
        # o poti rescrie mai scurt 
        self.jj = self.cnp[7] + self.cnp[8]
        jj = int(self.jj)
        return jj
        #varianta
        self.jj = self.cnp[7:9]
        return self.jj
#new empty line
    def check_month(self): # pentru toata chestia asta de mai jos , 
        #poti sparge in 2 functii, una care verifica ce fel de an e si apoi cea de check_month, iti las mai jos variantele:
        month_list = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
        ]
        month_nr = int(self.month)
        if month_nr in (1,3,5,7,8,10,12):
            if self.day in range(1,32):
                return month_list[month_nr-1]
            else:
                sys.exit(print(f'def check month error, day not in range for month {month_nr}: {self.day}') )   
        elif month_nr == 2:
            if self.day in range(1,29):
                return month_list[month_nr-1]
            else:
                sys.exit(print(f'def check month error, day not in range for month {month_nr}: {self.day}') )   
        elif month_nr in (4,6,9,11):
            if self.day in range(1,31):
                return month_list[month_nr-1]
            else:
                sys.exit(print(f'def check month error, day not in range for month {month_nr}: {self.day}') )   
        else:
            sys.exit(print(f'def check month error, day not in range for month {month_nr}: {self.day}') )    

        #varianta
        def is_leap_year(self, year):
                return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        
            def check_month(self):
                month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
                year = int(self.cc + self.get_yy())
                
                if self.month == 2 and self.is_leap_year(year):
                    day_limit = 29
                else:
                    day_limit = month_days.get(self.month, 0)
        
                if self.day > day_limit:
                    raise InvalidCNPError(f'Invalid day for month {self.month}: {self.day}')
                return f"{self.month}"
        
    def check_county(self):
        cnp_county_codes = {
    "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor", "06": "Bistrița-Năsăud",
    "07": "Botoșani", "08": "Brașov", "09": "Brăila", "10": "Buzău", "11": "Caraș-Severin", "12": "Cluj",
    "13": "Constanța", "14": "Covasna", "15": "Dâmbovița", "16": "Dolj", "17": "Galați", "18": "Gorj",
    "19": "Harghita", "20": "Hunedoara", "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș",
    "25": "Mehedinți", "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
    "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș", "36": "Tulcea",
    "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "Bucharest", "41": "Bucharest, Sector 1",
    "42": "Bucharest, Sector 2", "43": "Bucharest, Sector 3", "44": "Bucharest, Sector 4",
    "45": "Bucharest, Sector 5", "46": "Bucharest, Sector 6", "51": "Călărași", "52": "Giurgiu"
                            }
        if self.jj in cnp_county_codes:
            county = cnp_county_codes[self.jj]
            return county
            #aici poti sa scrii direct  return cnp_county_codes[self.jj]
        else:
            sys.exit(print(f'County code incorrect: {cnp_county_codes[self.jj]}')) # replace raise InvalidCNPError(f'Invalid county code: {self.jj}')
            #new empty line
    def check_nnn(self):
        s = int(self.cnp[0])
        nnn = int(self.cnp[9:12])
        #poti rescrie 
        if nnn < 1 or nnn > 999:
            sys.exit(print(f'NNN unknown: {nnn}') )              
        if (s in [1, 3, 5, 7] and nnn >= 500) or (s in [2, 4, 6, 8] and nnn < 500):
            sys.exit("Invalid NNN: Inconsistent with gender.")
        #varianta
        if not (1 <= nnn <= 999) or ((s in [1, 3, 5, 7] and nnn >= 500) or (s in [2, 4, 6, 8] and nnn < 500)):
            raise InvalidCNPError(f"Invalid NNN: {nnn}, inconsistent with gender.")
            #new empty line
    def check_control_digit(self):

    # Weights for the control digit calculation
        weights = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    # Extract the first 12 digits and the control digit    
        digits = [int(self.cnp[i]) for i in range(12)]
        control_digit = int(self.cnp[12])
    # Calculate the sum of products of weights and corresponding digits
        total_sum = sum(weights[i] * digits[i] for i in range(12))
    # Calculate the remainder
        remainder = total_sum % 11
    # Determine the expected control digit
        expected_control_digit = 1 if remainder == 10 else remainder
    # Compare with the provided control digit
        #poti rescrie mai scurt 
        if control_digit == expected_control_digit:
            return 
        else:
            sys.exit(print(f'return digit invalid: {control_digit}') )    
        #varianta
        if control_digit != expected_control_digit:
            raise InvalidCNPError(f'Invalid control digit: {control_digit}')
            #new empty line
class Persoana(CNP):
    def __init__(self, cnp, nume, prenume):
        super().__init__(cnp)
        self.nume = nume
        self.prenume = prenume
    
    def afiseaza_informatii(self):
        return f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}"
        #new empty line 
class Angajat(Persoana):
    def __init__(self, cnp, nume, prenume, pozitie):
        super().__init__(cnp, nume, prenume)
        self.pozitie = pozitie
    
    def afiseaza_detalii_angajat(self):
        return f"{self.afiseaza_informatii()}, Pozitie: {self.pozitie}"


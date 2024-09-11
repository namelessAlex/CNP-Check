import sys
class CNP:
    def __init__(self, cnp):
        self.cnp = cnp
        self.cc = None
        self.gender = None  
        self.month = None
        self.day = None
        self.jj = None
        self.first_char = None
    def check_length(self):
        # Logica pentru validarea CNP-ului
        length_of_cnp = len(self.cnp)
        if length_of_cnp == 13:
            valid_leng = "length ok"
        else:
            sys.exit(print(f'Length of CNP not ok: length of {length_of_cnp}') )   
        
        return 
    # validare primul caracter din CNP pentru a obtine ccul si sexul persoanei
    def check_sex(self):
        first_char = int(self.cnp[0])
        self.first_char = first_char
        first_char_list = [1,2,3,4,5,6]
        gender_list = ['masculin','feminin']
        if first_char in first_char_list:

            if first_char in (1,3,5):
                return gender_list[0]
            else:
                return gender_list[1]
        else:
            sys.exit(print(f'def validare_sex error, first char not in range(1 thru 6): {first_char}') )    
    def check_cc(self):
        cc_list = ['18','19','20']
        if self.first_char in (1,2):
            self.cc = cc_list[self.first_char]
        elif self.first_char in (3,4):
            self.cc = cc_list[self.first_char]
        elif self.first_char in (5,6):
            self.cc = cc_list[self.first_char]   
        # data nastere  
    def get_cc(self):
        if self.cc:
            return self.cc
        else:
            sys.exit(print(f'Century unknown: {self.cc}') )        
    def get_yy(self):    
        year = self.cnp[1] + self.cnp[2]
        return year
    def get_mm(self):  
        self.month = self.cnp[3] + self.cnp[4]
        return self.month
    def get_dd(self):             
        day = self.cnp[5] + self.cnp[6]
        self.day = int(day)
        if self.day in range(1,32):
            return day
        else:
            sys.exit(print(f'def get_dd error: {self.day}') )
    def get_jj(self):
        self.jj = self.cnp[7] + self.cnp[8]
        jj = int(self.jj)
        return jj
    def check_month(self):
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
        else:
            sys.exit(print(f'County code incorrect: {cnp_county_codes[self.jj]}'))
    def check_nnn(self):
        s = int(self.cnp[0])
        nnn = int(self.cnp[9:12])
        if nnn < 1 or nnn > 999:
            sys.exit(print(f'NNN unknown: {nnn}') )              
        if (s in [1, 3, 5, 7] and nnn >= 500) or (s in [2, 4, 6, 8] and nnn < 500):
            sys.exit("Invalid NNN: Inconsistent with gender.")
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
        if control_digit == expected_control_digit:
            return 
        else:
            sys.exit(print(f'return digit invalid: {control_digit}') )    
class Persoana(CNP):
    def __init__(self, cnp, nume, prenume):
        super().__init__(cnp)
        self.nume = nume
        self.prenume = prenume
    
    def afiseaza_informatii(self):
        return f"Nume: {self.nume}, Prenume: {self.prenume}, CNP: {self.cnp}"
class Angajat(Persoana):
    def __init__(self, cnp, nume, prenume, pozitie):
        super().__init__(cnp, nume, prenume)
        self.pozitie = pozitie
    
    def afiseaza_detalii_angajat(self):
        return f"{self.afiseaza_informatii()}, Pozitie: {self.pozitie}"


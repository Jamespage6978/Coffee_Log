class Coffee:
    def __init__(self,brand,R_date,R_taste,proccess,grind,B_method,C_in,C_out,T_complete,taste,notes):
        self.brand = brand
        self.R_date = R_date
        self.R_taste = R_taste
        self.proccess = proccess
        self.grind = grind
        self.B_method = B_method
        self.C_in = C_in
        self.C_out = C_out
        self.T_complete = T_complete
        self.taste = taste
        self.notes = notes
    
    def ratio_calc(self):
        if self.B_method == "espresso":
            rat_calcd = float(self.C_out)/float(self.C_in)
            ratio = f"1:{rat_calcd}"
        else:
            rat_calcd = (1000.0/float(self.C_out))
            C_in_calc = float(self.C_in)*rat_calcd
            ratio = f"{C_in_calc}grams per 1000ml/1L"
        return ratio
    
roast1 = Coffee("Mor welsh coffee company","2/1/2020","","washed","1","espress","32.5","500","30",["tart","cherry","Full"],"notes section")

print(roast1.ratio_calc())
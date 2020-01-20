from PyInquirer import prompt, print_json,ValidationError,Validator
import datetime
from pprint import pprint
import json
class DateValidator(Validator):
    def validate(self,document):
        try:
            datetime.datetime.strptime(document.text, '%d-%m-%Y')
        except ValueError:
            raise ValidationError(
                message ="Incorrect data format, should be YYYY-MM-DD",
                 cursor_position=len(document.text))

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

##roast1 = Coffee("Mor welsh coffee company","2/1/2020","","washed","1","espress","32.5","500","30",["tart","cherry","Full"],"notes section")

questions = [
    {
        'type': 'input',
        'name': 'brand',
        'message': 'Enter Coffee name',
    },

    {
        'type': 'input',
        'name': 'R_date',
        'message': 'Enter Roast date (DD-MM-YYYY)',
        'validate': DateValidator
    },
    
    {
        'type': 'editor',
        'name': 'R_taste',
        'message': 'Please write the roasters taste notes',
        'default': 'Roasters Taste Notes: ',
        'eargs': {
            'editor':'default',
            'ext':'.txt'
                }
    },

    {
        'type':'list',
        'name':'proccess',
        'message':'Select the coffee proccess',
        'choices':['Natural','Washed','Honey']
    },

    {
        'type':'input',
        'name':'grind',
        'message':'Enter Grind setting/notes',
    },

        {
        'type':'list',
        'name':'B_method',
        'message':'Select the Brew method',
        'choices':['V60','Aeropress','Mellita Look IV','Espresso','French press','Stove top - Moka pot']
    },

    {
        'type':'input',
        'name':'C_in',
        'message':'Enter how much coffee was used in grams'
        #need validation it is a number
    },

    {
        'type':'input',
        'name':'C_out',
        'message':'Enter final yield of coffee/how much water was used in grams'
    },

    {
        'type':'input',
        'name':'T_complete',
        'message':'Enter total brew time in seconds'
    },
    
    {
        'type': 'editor',
        'name': 'taste',
        'message': 'Please write your taste notes',
        'default': 'Taste Notes: ',
        'eargs': {
            'editor':'default',
            'ext':'.txt'
                }
    },

    {
        'type': 'editor',
        'name': 'R_taste',
        'message': 'Please write any notes',
        'default': 'Notes: ',
        'eargs': {
            'editor':'default',
            'ext':'.txt'
                }
    },
]   


answers = prompt(questions)
print(json.dumps(answers, indent=1))
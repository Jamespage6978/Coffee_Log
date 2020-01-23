from config import configuration as config
from read_proccess import write_html
##
from PyInquirer import prompt, print_json,ValidationError,Validator
import datetime, json, os, pandas
from pprint import pprint
from uuid import uuid1
############

def Dict_output_create (C_tolog):
    C_toOutput = C_tolog.__dict__
    C_toOutput["ID"] = C_tolog.id_create()
    C_toOutput["Ratio"] = C_tolog.ratio_calc()
    C_toOutput["Date_created"] = datetime.datetime.now().strftime("%Y%m%d")
    return C_toOutput

def WriteOut_Log(C_toOutput):
    if config['Switches']['location'] == 'local':
        path = f"{config['Local']['location']}Coffe_Log.json"
        if os.path.exists(path) == False:
            with open(path,'a') as outfile:
                json.dump([], outfile)
        else:
            with open(path,'r') as feedsjson:
                feeds = json.load(feedsjson)
            with open(path,'w') as outfile:
                feeds.append(C_toOutput)
                json.dump(feeds,outfile,indent=4)
    elif config['Switches']['location'] == 'cloud':
        pass

def input_Log():
    ################ Define and ask questions
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
            'type': 'input',
            'name': 'R_taste',
            'message': 'Please write the ',
            'default': 'Roasters Taste Notes: '
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
            'message':'Enter how much coffee was used in grams',
            'validate': NumberValidator
        },

        {
            'type':'input',
            'name':'C_out',
            'message':'Enter final yield of coffee/how much water was used in grams',
            'validate': NumberValidator
        },

        {
            'type':'input',
            'name':'T_complete',
            'message':'Enter total brew time '
        },
        
        {
            'type': 'input',
            'name': 'taste',
            'message': 'Please write your ',
            'default': 'Taste Notes: '
        },

        {
            'type': 'input',
            'name': 'notes',
            'message': 'Please write any ',
            'default': 'Notes: '
        },
    ]   
    answers = prompt(questions)
    ##################
    C_tolog = Coffee(
        answers['brand'],
        answers['R_date'],
        answers['R_taste'],
        answers['proccess'],
        answers['grind'],
        answers['B_method'],
        answers['C_in'],
        answers['C_out'],
        answers['T_complete'],
        answers['taste'],
        answers['notes']
        )

    C_toOutput = Dict_output_create(C_tolog)
    return C_toOutput

class DateValidator(Validator):
    def validate(self,document):
        try:
            datetime.datetime.strptime(document.text, '%d-%m-%Y')
        except ValueError:
            raise ValidationError(
                message ="Incorrect data format, should be YYYY-MM-DD",
                 cursor_position=len(document.text))

class NumberValidator(Validator):
    def validate(self, document):
        try:
            float(document.text)
        except ValueError:
            raise ValidationError(
                message ="Input is not a number",
                 cursor_position=len(document.text))

class Coffee(object):
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

    def id_create(self):
        date_today = datetime.datetime.now().strftime("%Y%m%d")
        uid = str(uuid1())
        unique_id = f"{date_today}_{uid}"
        return unique_id



if __name__ == '__main__':
    WriteOut_Log(input_Log())
    write_html()
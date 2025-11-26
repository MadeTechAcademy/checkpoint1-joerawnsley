from duty import Duty
from duties_and_themes_data import *

class Theme:
    def __init__(self, title, duties):
        self.title = title
        self.duties = duties
        
    def plainText(self):
        return ("Theme: Automate!"
        "Duties:"
        f"Duty 5: {duty_5.plainText()}."
        f"Duty 7: {duty_7.plainText()}."
        f"Duty 10: {duty_10.plainText()}."
         )
        


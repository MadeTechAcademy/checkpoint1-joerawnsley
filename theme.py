from duty import Duty
from duties_and_themes_data import *

class Theme:
    def __init__(self, title, duties):
        self.title = title
        self.duties = duties
        
    def plainText(self):
        text = ("Theme: Automate!\n\n"
        "Duties:\n\n"
        f"{duty_5.plainText()}\n"
        f"{duty_7.plainText()}\n"
        f"{duty_10.plainText()}"
         )
        print(text)
        return text
        


from duty import Duty
from duties_and_themes_data import *

class Theme:
    def __init__(self, title, duties):
        self.title = title
        self.duties = duties
        
    def plainText(self):
        theme_text = f"Theme: {self.title}\n\nDuties:\n"
        for duty in self.duties:
            theme_text += f"\n{duty.plainText()}"
        
        print(theme_text)
        return theme_text

    def htmlString(self):
        return ""


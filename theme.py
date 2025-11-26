from duties_and_themes_data import *

class Theme:
    def __init__(self, title, duties):
        self.title = title
        self.duties = duties
        
    def plainText(self):
        theme_text = f"Theme: {self.title}\n\nDuties:\n"
        for duty in self.duties:
            theme_text += f"\n{duty.plainText()}"
        return theme_text

    def htmlString(self):
        html_string = f"<h2>Theme: {self.title}</h2><ul>"
        for duty in self.duties:
            html_string += duty.htmlListElement()
        html_string += "</ul>"
        return html_string


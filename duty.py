class Duty:
    def __init__(self, duty_number, duty_text):
        self.duty_number = duty_number
        self.duty_text = duty_text
    
    def plainText(self):
        return f"Duty {self.duty_number} {self.duty_text}.\n"

    def htmlListElement(self):
        return f"<li>Duty {self.duty_number} {self.duty_text}.</li>\n"
    

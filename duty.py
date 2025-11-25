class Duty:
    def __init__(self, duty_number, duty_text):
        self.duty_number = duty_number
        self.duty_text = duty_text
    
    def toText(self):
        return f"Duty {self.duty_number}: {self.duty_text}."

    def toListElement(self):
        return f"<li>Duty {self.duty_number}: {self.duty_text}.</li>\n"
    

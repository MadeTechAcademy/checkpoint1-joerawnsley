from duties_and_themes_data import *
import webbrowser
import os


def print_duties_to_terminal(theme):
    print(theme.plainText())
    
def create_html_document(filename, duties):
    with open(filename, "x") as html_file:
        html_file.write("<h1>Devops Engineer: Occupation Duties</h1>")
        html_file.write("<ul>")
        for duty in duties:
            html_file.write(duty.htmlListElement())
        html_file.write("</ul>")

def choose_output(theme):
    user_choice_of_output = input("""
    Press (1) to list the duties in the terminal, or press (2) to see them in the browser.\n
    Enter your choice:
    """)
    match user_choice_of_output:
        case "1":
            print("\n")
            print_duties_to_terminal(theme)
        case "2":
            create_html_document(html_file_name, theme)
            file_path = "file://" + os.path.realpath(html_file_name)
            webbrowser.open(file_path)

def choose_theme():
    user_choice_of_theme = input("""
    Please select a theme to see the duties for that theme.\n
    (1) All duties
    (2) Bootcamp
    (3) Automate
    (4) Houston, Prepare to Launch
    (5) Going Deeper
    (6) Assemble!
    (7) Call Security
    
    Enter your choice: """)
    
    match user_choice_of_theme:
        case "1": choose_output(all_duties)
        case "2": choose_output(bootcamp_duties)
        case "3": choose_output(automate_duties)
        case "4": choose_output(houston_duties)
        case "5": choose_output(deeper_duties)
        case "6": choose_output(assemble_duties)
        case "7": choose_output(security_duties)


if __name__=="__main__":
    
    print("""
    Welcome to APPRENTICE THEMES!""")
    choose_theme()
    
   
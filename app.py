from data.themes import *
from data.duties import *
from data.filenames import html_file_name
import webbrowser
import os


######### Please see README.md for notes ###############


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
        case "1": display_duties(full_apprenticeship)
        case "2": display_duties(bootcamp)
        case "3": display_duties(automate)
        case "4": display_duties(houston)
        case "5": display_duties(deeper)
        case "6": display_duties(assemble)
        case "7": display_duties(security)

def display_duties(theme):
    theme.confirm_choice()
    user_choice_of_output = input(f"""Press (1) to list the duties in the terminal, or press (2) to see them in the browser.\n
    Enter your choice: """)
    match user_choice_of_output:
        case "1":
            print("\n")
            print_duties_to_terminal(theme)
        case "2":
            create_html_document(html_file_name, theme)
            file_path = "file://" + os.path.realpath(html_file_name)
            webbrowser.open(file_path)
            
def print_duties_to_terminal(theme):
    print(theme.plainText())

    
def create_html_document(filename, theme):
    with open(filename, "x") as html_file:
        html_file.write("<h1>Devops Engineer: Occupation Duties</h1>")
        html_file.write(theme.htmlString())
        

if __name__=="__main__":
    
    print("""
    Welcome to APPRENTICE THEMES!""")
    choose_theme()
    
   
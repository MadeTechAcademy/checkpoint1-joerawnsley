from duties_and_names import *
import webbrowser
import os


def print_duties_to_terminal(duties):
    for duty in duties:
        print(duty.plainText())
    
def create_html_document(filename, duties):
    with open(filename, "x") as html_file:
        if len(duties) <= 1:
            html_file.write("<h1>Devops Engineer: Occupation Duties</h1>")
            html_file.write("<ul>")
            html_file.write(duty_4.htmlListElement())
            html_file.write("</ul>")
            
        else:
            html_file.write("<h1>Devops Engineer: Occupation Duties</h1>")
            html_file.write("<ul>")
            for duty in duties:
                html_file.write(duty.htmlListElement())
            html_file.write("</ul>")

    

if __name__=="__main__":
    
    user_choice = input("""
    Welcome to apprentice themes!\n
    Press (1) to list all the duties, or press (2) to see them in the browser.\n
    Enter your choice:
    """)
    if user_choice == '1':
        print("\n")
        print_duties_to_terminal(all_duties)
    
    if user_choice == '2':
        create_html_document(html_file_name, all_duties)
        file_path = "file://" + os.path.realpath(html_file_name)
        webbrowser.open(file_path)
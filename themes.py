from duties import *
import webbrowser
import os


def print_duties_to_terminal(duties):
    for duty in duties:
        print(duty.plainText())
    
def create_html_document(duties):
    with open("list_of_duties.html", "x") as html_file:
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
        create_html_document(all_duties)
        file_path = "file://" + os.path.realpath("list_of_duties.html")
        webbrowser.open(file_path)
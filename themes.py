from duties import *



def print_duties_to_terminal():
    for duty in all_duties:
        print(duty.plainText())
    
def create_html_document(duties):
    with open("list_of_duties.html", "x") as html_file:
        html_file.write("<h1>Devops Engineer: Occupation Duties</h1>")
        html_file.write("<ul>")
        for duty in duties:
            html_file.write(duty.htmlListElement())
        html_file.write("</ul>")

    

if __name__=="__main__":
    # user_choice = input("""
    # Welcome to apprentice themes!\n
    # Press (1) to list all the duties\n
    # Enter your choice:
    # """)
    # # if user_choice == '1
    # #     print_duties_to_terminal()
        
    create_html_document(all_duties)
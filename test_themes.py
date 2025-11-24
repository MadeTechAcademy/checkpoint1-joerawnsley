from themes import list_of_duties

class TestListOfDuties():
        def test_length(self):
            assert len(list_of_duties) == 13
        
        def test_includes_duties(self):
            duty_3 = "Duty 3 Engage in productive pair/mob programming to underpin the practice of peer review."
            duty_8 = "Duty 8 Evolve and define architecture, utilising the knowledge and experience of the team to design in an optimal user experience, scalability, security, high availability and optimal performance."
            duty_13 = "Duty 13 Accept ownership of changes; embody the DevOps culture of 'you build it, you run it', with a relentless focus on the user experience."
            assert duty_3 in list_of_duties
            assert duty_8 in list_of_duties
            assert duty_13 in list_of_duties


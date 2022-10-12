import unittest 
from Desing_Patterns_2 import  Developer, Project,AssignManagement,Task
from datetime import datetime

class Test_test_Desing_Patterns_2(unittest.TestCase):
    def test_add(self):
        dan=Developer(12,"Dan Hul","street","djhdhd","da",50)
        glam=Developer(1,"Glam Bool","street2","gyujhbgh","net",45)
        pj=Project("qwerty",datetime(2022,9,12),datetime(2023,9,12),2)
        pjj=Project("fvvf",datetime(2020,4,12),datetime(2022,12,12),3)
        ts1=Task(14,"rewwq",datetime(2022,9,12),[1,2],"in process",pj.title)
        pj.add_task(ts1)


        AssignManagement(pj, dan).assign()
        AssignManagement(glam,pj).assign()
        

        self.assertEqual(pj.developers[0].name,"Dan")
        self.assertEqual(pj.developers[1].name,"Glam")
        self.assertEqual(dan.projects[0].title,'qwerty')
        AssignManagement(dan,pj).unassign()
        self.assertEqual(pj.developers[0].name,'Glam')


         
if __name__ == '__main__':
    unittest.main()

from abc import abstractclassmethod, abstractmethod
import abc
from ast import Str
import dataclasses
from datetime import datetime
from pickle import LIST, NONE
from sre_constants import ANY
from tkinter import PROJECTING
from turtle import title
from dataclasses import dataclass
 



@dataclass
class personal_information:
    id:int 
    name:str
    adress:str 
    email:str 
    rank:str 
    salary:int 
    sname:str=''

    @property
    def namer(self):
        return self.name

    @namer.setter
    def namer(self,l):
        temp=self.name.split(" ")
        self.name=temp[0]
        self.sname=temp[1]
        del temp

class Employe(personal_information):
    @abstractclassmethod
    def calculate_salary(self):pass
    @abstractclassmethod
    def ask_sick_leave(project_manager) -> bool:pass

class Project:pass
class AssignManagement:
    employee: Employe
    project: Project
    def __init__(self,employee,project) -> None:
        if isinstance(employee,Employe):
           self.employee, self.project=employee,project
        else:
            self.employee,self.project=project,employee
           
    def assign(self) -> None:
         if (self.project.i<self.project.limit):
             if self.project in self.employee.projects:
                     print("this developer already work on this projectmm")
                     return
             self.employee.projects.append(self.project)
             self.project.i+=1
             self.project.developers.append(self.employee)
             return self.employee, self.project
         else:
            print("no free places")

    def unassign(self) -> None:
        if self.project.i!=0:
            self.employee.projects.remove(self.project)
            self.project.i-=1
            self.project.developers.remove(self.employee)
        else:
            print("list empty")
        
#class Project:pass##!!!!!!!!!!!!!!!!!!!!!!
class Developer(Employe,AssignManagement):
    #projects:Project=[]
    def __init__(self, id, name, adress, email, rank, salary):
        super().__init__(id, name, adress, email, rank, salary)
        self.projects:Project=[]
        self.namer=1

    def assing_possibility(self,project)->bool: 
        if (project.i<project.limit):
            return True
        else:
            return False        
    def asssigned_projects(self):
        for i in self.projects:
            print(i.title," ")
    
    def calculate_salary(self):
        return self.salary*8*21*12
    def ask_sick_leave(project_manager) -> bool:
            if project_manager.employee_requests==1:
                return True
            else:
                return False

class Task:
        id: int
        title: str
        deadline: datetime
        items:str=[]#str
        status: ANY # is_done or in_progress
        related_project: str # project title
        def __init__(self,id,title,deadline,items,status,related_project=None) -> None:
            self.id=id
            self.title=title 
            self.deadline=deadline
            self.items=items
            self.status=status
            self.related_project=related_project

        def implement_item(self,item_name: str) -> str:
            self.items.append(item_name)
        def add_comment(self,comment: str) -> None:
            self.comment=comment

    
class Project():
    title:str 
    start_date:datetime
    finish_time:datetime
    task_list:Task=[] #task
    developers=[]#Developers
    i=0
    limit:int
    def __init__(self, title, start_date,finish_time , limit,task_list=None):
        self.title=title 
        self.start_date=start_date
        self.limit=limit
        self.finish_time=finish_time
        self.task_list:Task=[]
        self.developers:Developer=[]
    def add_task(self,task:Task):
        self.task_list.append(task)

    @abstractmethod
    def add_employe (self,developer:Developer)->None:
       if(self.i<self.limit):
            for i in self.developers:
                if developer.name ==  i.name:
                    print("this developer already work on this project")
                    return
            self.developers.append(developer)
            developer.projects.append(self)
            self.i+=1  
       else:
            print("no more")
    @abstractmethod
    def remove_employe(abs,self,developer)->None:
        self.developers.remove(developer)
        developer.projects.remove(self)
        self.i-=1
        
class Assignment(Project):
    def __init__(self,task_list):
         self.received_tasks=dict() 
         self.is_done=bool()
         self.description:str 
         self.status:str
         self.g=0
         for i in task_list:
            self.received_tasks[i]=None
    def get_tasks_to_date(self,current_time:datetime,project:Project)->str:
        self.received_tasks=dict.fromkeys(project.task_list,project.start_date) 
        if(project.start_date>=current_time):
            self.status="is done"
            self.is_done=1
        else:
            finish = project.finish_time
            start =  project.start_date
            now= current_time
            time_for_work = (finish- start).days
            
            time= (now - start).days

            prosent= (time*100)/time_for_work
            self.status=str(prosent)+"% of work is done"

@dataclass
class Team:
    def __init__(self,id,title,member_list,project_id) -> None:
        self.id :int =id
        self.title:Str=title
        self.member_list:list()=member_list
        self.project_id:int=project_id
       
            
class Web(Project):
    def __init__(self):
        print("You make a Web progect")
        super().__init__("Web progect", datetime(2022,9,12), datetime(2023,9,12), 2)
        self.add_task(Task(14,"rewwq",datetime(2022,9,12),[1,2],"in process",self.title))

    def add_employe(self) -> None:
        print("You add developer to Web progect\n")
        return super().add_employe(Developer(12,"Dan Hul","street","djhdhd","da",50))

class Mobile(Project):
    def __init__(self):
        print("You make a Mobile progect")
        super().__init__("Mobile progect", datetime(2020,9,12), datetime(2023,9,12), 2)
       

    def add_employe(self) -> None:
        
        print("You add developer to Mobile progect\n")
        return super().add_employe(Developer(32,"notDen Hul","street","djhdhd","da",50))

class Embedded(Project):
    def __init__(self):
        print("You make a Embedded progect")
        super().__init__("Web progect", datetime(2020,9,12), datetime(2023,9,12), 2)
        self.add_task(Task(14,"rewwq",datetime(2022,9,12),[1,2],"in process",self.title))

    def add_employe(self) -> None:
        print("You add developer to Embedded progect\n")
        return super().add_employe(Developer(34,"booble Boobles ","street","djhdhd","da",50))

     


class SoftwareArchitect:
    def fill_project(team: Team, *args) -> None:pass

    @abstractmethod
    def create_project(self,*args) -> Project:pass
    
class WebArchitect(SoftwareArchitect):
     def create_project(self,*args):
         return Web()
class MobileArchitect(SoftwareArchitect):
    def create_project(self,*args):
         return Mobile()
class EmbeddedArchitect(SoftwareArchitect):
    def create_project(self,*args):
         return Embedded()


class QAEngineer(Employe):
    position:str

    def __init__(self, id, name, adress, email, rank, salary,position=None):
        super().__init__(id, name, adress, email, rank, salary)
        self.position=position

    def calculate_salary(self):
            return self.salary*8*21

    def ask_sick_leave(project_manager) -> bool:
            if project_manager.employee_requests==1:
                return True
            else:
                return False
    def add_ticket() -> None:pass

    def test_feature(self,test)->str:
        test=test.create_project() 
        test.add_employe()

        #ts1.implement_item("3ec")
        #print(pj.task_list[0].items)

        #AssignManagement(pj, dan).assign()
        #AssignManagement(glam,pj).assign()
        #AssignManagement(dan,pj).unassign()
        

        #print(pj.developers[0].name)
        #print(dan.projects[0].title)
       


        #1
        #pj.add_developer(dan)
        #pj.add_developer(glam)
        #pjj.add_developer(glam)
        #dan.assign(pjj)
        ##glam.unassign(pj)
        #
        #print(pj.developers[1].name)
        #print(pjj.developers[0].name)
        #print("------------------------")
        #glam.asssigned_projects()
        #print("----------")
        #dan.asssigned_projects()
        #print("------------------------")
        #da=Assignment(pjj.task_list)
        #da.get_tasks_to_date(datetime(2022,10,12),pjj)
        #print(da.status)

class ProjectManager(Employe):
    project:Project

    employee_requests:ANY

    def __init__(self, id, name, adress, email, rank, salary,employee_requests,project=None) :
        super().__init__(id, name, adress, email, rank, salary)
        self.employee_requests=employee_requests
        self.project=project
        self.namer=1
    
    def ask_sick_leave(project_manager) -> bool:
        return False

    def discuss_progress(self):
        print("all fine")




# main 
tester=QAEngineer(1,"pd20 h","homeless","qwerty","-",21)

test=WebArchitect()
tester.test_feature(test)

test=MobileArchitect()
tester.test_feature(test)

test=EmbeddedArchitect()
tester.test_feature(test)
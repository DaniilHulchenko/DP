from datetime import datetime
from pickle import LIST
from tkinter import PROJECTING
from turtle import title
from typing import List



class personal_information:
    id:int 
    name:str 
    adress:str 
    email:str 
    rank:str 
    salary:int 
    def __init__(self,id,name,adress,email,rank,salary):
        self.id=id 
        self.name=name 
        self.adress=adress 
        self.email=email 
        self.rank=rank 
        self.salary=salary

class Project:pass##!!!!!!!!!!!!!!!!!!!!!!
class Developer(personal_information):
    projects:Project=[] #(Project)
    def __init__(self, id, name, adress, email, rank, salary):
        super().__init__(id, name, adress, email, rank, salary)
        self.projects:Project=[]
    def assing_possibility(self,project)->bool: 
        if (project.i<project.limit):
            return True
        else:
            return False        
    def asssigned_projects(self):
        for i in self.projects:
            print(i.title," ")
    def assign(self,project)->None:
        if (project.i<project.limit):
             if project in self.projects:
                     print("this developer already work on this projectmm")
                     return
             self.projects.append(project)
             project.i+=1
             project.developers.append(self)
        else:
             print("no free plases")
    def unassign(self,project)->None:
        if project.i!=0:
            self.projects.remove(project)
            project.i-=1
            project.developers.remove(self)
        else:
            print("list empty")

class Project:
    title:str 
    start_date:datetime
    finish_time:datetime
    task_list:str(list) #str
    developers:Developer=[]#Developers
    i=0
    limit:int
    def __init__(self, title, start_date,finish_time, task_list, limit):
        self.title=title 
        self.start_date=start_date
        self.task_list=task_list
        self.limit=limit
        self.finish_time=finish_time
        self.developers:Developer=[]
    def add_developer(self,developer:Developer)->None:
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
    def remove_developer(self,developer)->None:
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
            

                


class QAEngineer(personal_information):
    position:str
    def __init__(self, id, name, adress, email, rank, salary,position=None):
        super().__init__(id, name, adress, email, rank, salary)
        self.position=position
    def test_feature(self)->str:
        dan=Developer(12,"dan","street","djhdhd","da",20)
        glam=Developer(1,"glam","street2","gyujhbgh","net",90)
        pj=Project("qwerty",datetime(2022,9,12),datetime(2023,9,12),("somphing","somphing 2"),2)
        pjj=Project("fvvf",datetime(2020,4,12),datetime(2022,12,12),("somphing3","somphing 4"),3)

        pj.add_developer(dan)
        pj.add_developer(glam)
        pjj.add_developer(glam)
        
        #dan.assign(pj1)
        #glam.assign(pj1)
        #print(pj.developers[0].name)
        #print(pj1.developers[0].name) 
        print(pjj.developers[0].name)
        print("------------------------")
        glam.asssigned_projects()
        print("----------")
        dan.asssigned_projects()
        print("------------------------")
        da=Assignment(pjj.task_list)
        da.get_tasks_to_date(datetime(2022,10,12),pjj)
        print(da.status)


        


class ProjectManager(personal_information):
    project:Project
    def __init__(self, id, name, adress, email, rank, salary,project=None)  :
        super().__init__(id, name, adress, email, rank, salary)
        self.project=project
    def discuss_progress(self):
        print("all fine")




# main 
tester=QAEngineer(1,"pd-20","homeless","qwerty","-",21)
tester.test_feature()

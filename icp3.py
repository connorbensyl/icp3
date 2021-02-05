import requests
from bs4 import BeautifulSoup
import numpy as np
from numpy import random
class Employee:
    num_employees = 0 #instantiate static variables
    sum_salaries = 0

    def __init__(self, the_name, the_family, the_salary, the_dept):
        self.name = the_name
        self.family = the_family
        self.salary = the_salary
        self.dept = the_dept
        Employee.sum_salaries += self.salary #increment static variables for every new instance created
        Employee.num_employees += 1

    @staticmethod
    def avg_salary(): #calculate average from all employee instances
        return Employee.sum_salaries / Employee.num_employees


class Fulltime_Employee(Employee): #fulltime employee and regular employee are the same so nothing here
    pass



def main():
    emp1 = Employee("John", "Smith", 50000, "Sales") #create some employee instances
    emp2 = Employee("Joe", "Williams", 30000, "Marketing")
    emp3 = Employee("Theo", "Von", 100000, "Executive")
    print(emp3.avg_salary())
    emp4 = Fulltime_Employee("Peter", "Jackson", 40000, "Movies")
    emp4 = Fulltime_Employee("Sarah", "Johnson", 90000, "Accounting")
    emp5 = Fulltime_Employee("Gina", "Peters", 110000, "Executive")
    print(emp5.avg_salary())
    getLinks()



    x = np.random.uniform(0,20,size=(1,20)) #create array of random floats between 1 and 20
    x = x.reshape(4,5)

    x[0] = np.where(x[0] == x[0].min(), 0,x[0])#change max in each row to 0
    x[1] = np.where(x[1] == x[1].min(), 0, x[1])
    x[2] = np.where(x[2] == x[2].min(), 0, x[2])
    x[3] = np.where(x[3] == x[3].max(), 0, x[3])




    print(x)


def getLinks():
    file = open("links.txt", "w")
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    source_code = requests.get(url) #get source code of page
    plain_text = source_code.text #convert to plain text
    soup = BeautifulSoup(plain_text, "html.parser") #parse
    title = soup.find("title") #output title
    print(title.get_text)

    for link in soup.findAll('a'):#iterate through all "a" tags




        href = link.get('href') #find link in each "a" tag and output to file
        file.write("https://en.wikipedia.org"+str((href)))
        file.write('\n')







main()
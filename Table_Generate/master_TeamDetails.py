# %%
import pandas as pd
import sys

ocNames = ["2021MT10697", "2021EE10636"]
acNames = ["2021MT10143", "2021EE10653", "2021MT10703", "2021EE10137", "2021EE10984", "2021EE10638"]
subtribeNames = ["Documentation", "Research", "Survey and Business Development", "Electronic Design and Simulation", "Mechanical Design", "Fabrication and Testing"]


class Student:
    def __init__(self, name, entry_number, vertical , IF, link):
        self._name_ = self.capitalize_name(name)
        self._entry_number_ = entry_number.upper()
        self._vertical_ = vertical.split('(', 1)[0].strip()    
        self._email_ = self._get_email_(entry_number)
        self._IF_  = IF
        self._link_ = link
    
    def capitalize_name(self , full_name):
        words = full_name.split()
        capitalized_words = [word.capitalize() for word in words]
        capitalized_name = ' '.join(capitalized_words)
        return capitalized_name
    
    def _get_email_(self , entry_num):
        dict = {'EE': 'ee', 'MT':'maths', 'CS':'cse'}
        email = entry_num[4 : 7] + entry_num[2 : 4] + entry_num[7 : 11] + '@'+dict[entry_num[4 : 6]]+'.iitd.ac.in'
        return email.lower()
    
    def latex_row(self, flag):
        if self._entry_number_ in acNames and flag:
            return '\href{'+f'{self._link_}'+'}{\\textbf{'+f'{self._name_}'+'} }'+f' & {self._entry_number_} & '+ '\href{'+f'mailto:{self._email_}'+'}{'+f'{self._email_}'+'}'+f' & {self._IF_}\\\\ \n\hline \n'
        return '\href{'+f'{self._link_}'+'}{'+f'{self._name_}'+'}'+f' & {self._entry_number_} & '+ '\href{'+f'mailto:{self._email_}'+'}{'+f'{self._email_}'+'}'+f' & {self._IF_}\\\\ \n\hline \n'


sheetAdd = './members_IF.xlsx'
textAdd = '../Tex_files/Chapters/Introduction/Members.tex'
df = pd.read_excel(sheetAdd)
file = open(textAdd, 'w')
lowIF_head = 0


  
def makeTable1():
    file.write("""\section{Overall Coordinators}
    \\begin{center}
	    \\label{table:oc}
	    \\begin{longtable}{ | c | c | c | c | c | }
		    \\hline
		    \\textbf{Name}                                                                & \\textbf{Entry Number} & \\textbf{Email ID}                                                    & \\textbf{IF} \\\\
		    \\hline \\hline""")
    
    students = []
    for index, row in df.iterrows():
        student = Student(name = row['Name'] , entry_number = row['Entry Number'], vertical = row['Vertical'] , IF = row['IF'], link = row['Link'])
        if row['Entry Number'] in ocNames:
            students.append(student)
    
    for student in students:
        file.write(student.latex_row(1))
    
    file.write("""
		    \\caption{Overall Coordinators}
	    \\end{longtable}
    \\end{center}
    """)
    file.write('\section{Subtribes\\footnote{\\textbf{\\textit{Activity Coordinator} written in bold}}}')



def makeTable2(subtribeName, label):
    
    file.write("""
    \subsection{""" + subtribeName + """}
    \\begin{center}
    \\label{table:"""+label+"""1}
    \\begin{longtable}{| c | c | c | c | }
        \\hline
        \\textbf{Name}                                                                                                      & \\textbf{Entry Number} & \\textbf{Email ID}                                                    & \\textbf{IF} \\\\
        \\hline \\hline""")
    
    students = []
    for index, row in df.iterrows():
        student = Student(name = row['Name'] , entry_number = row['Entry Number'], vertical = row['Vertical'] , IF = row['IF'], link = row['Link'])
        if subtribeName in row['Vertical']:
            students.append(student)
    
    for i in range(len(students)):
        if students[i]._entry_number_ in acNames:
            students[0], students[i] = students[i], students[0]
            break
        
    for student in students:
        file.write(student.latex_row(1))

    file.write("""\\hline
		    \\caption{""" + subtribeName+"""}
	    \\end{longtable}
    \\end{center}""")


def makeTable3(subtribeName, label):
    students = []
    for index, row in df.iterrows():
        student = Student(name = row['Name'] , entry_number = row['Entry Number'], vertical = row['Vertical'] , IF = row['IF'], link = row['Link'])
        if student._IF_ < 1 and  subtribeName in row['Vertical'] and (not student._entry_number_ in ocNames):
            students.append(student)
    
    if len(students) == 0:
        return
    
    if lowIF_head == 0:
        file.write("\n\section{Tribe Members with IF less than 1}")
    
    file.write("""
    \subsection{""" + subtribeName + """}
    \\begin{center}
    \\label{"""+label+"""2}
    \\begin{longtable}{| c | c | c | c | }
        \\hline
        \\textbf{Name}                                                                                                      & \\textbf{Entry Number} & \\textbf{Email ID}                                                    & \\textbf{IF} \\\\
        \\hline \\hline""")
    
    
    for student in students:
        file.write(student.latex_row(0))

    file.write("""\\hline
		    \\caption{IF $< 1 - $ """ + subtribeName+"""}
	    \\end{longtable}
    \\end{center}""")


makeTable1()
for subtribe in subtribeNames:
    makeTable2(subtribe, subtribe[0:4])

for subtribe in subtribeNames:
    makeTable3(subtribe, subtribe[0:4])

    if lowIF_head == 0:
        lowIF_head = 1



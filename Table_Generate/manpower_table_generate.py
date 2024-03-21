#!/usr/bin/env python3
import pandas as pd
import sys

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
    # def __str__(self):
    #     return \
    #     f'         Name: {self._name_}\n \
    #     Entry Number: {self._entry_number_}\n \
    #     Vertical: {self._vertical_}\n \
    #     Email: {self._email_}\n \
    #     IF: {self._IF_}\n\n'


    def latex_row(self):
        # return f'{self._name_} & {self._entry_number_} & {self._vertical_} & {self._email_} & {self._IF_}\\\\ \n\hline \n'
        # print(self._email_)
        return '\href{'+f'{self._link_}'+'}{'+f'{self._name_}'+'}'+f' & {self._entry_number_} & '+ '\href{'+f'mailto:{self._email_}'+'}{'+f'{self._email_}'+'}'+f' & {self._IF_}\\\\ \n\hline \n'

team_names = ['documentation', 'research', 'survey', 'edesign', 'mdesign', 'fabrication']
sheet_names = ['Documentation', 'Research', 'Survey', 'Electronic', 'Mechanical', 'Fabrication']
if __name__ == '__main__':
    for i in range(len(team_names)):
        team = team_names[i]
        sheet_name = sheet_names[i]
        df = pd.read_excel('c:/Users/archi/OneDrive/Desktop/ELL305_work/Documentation/Table_gen/members_IF.xlsx')
        students = []
        for index, row in df.iterrows():
            student = Student(name = row['Name'] , entry_number = row['Entry Number'], vertical = row['Vertical'] , IF = row['IF'], link = row['Link'])
            if sheet_name in row['Vertical']:
                students.append(student)

        students = sorted(students , key = lambda x: x._vertical_)

        with open('c:/Users/archi/OneDrive/Desktop/ELL305_work/Documentation/Table_gen/' + team + '.txt', 'w') as file:
            for student in students:
                file.write(student.latex_row())

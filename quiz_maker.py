import json
from json import JSONDecodeError
from re import U
import random
import string
from datetime import datetime,timedelta

class mentor:

    def Register(self,type,name,institute_name,email_id,password):
        self.type,self.name,self.institute_name,self.email_id,self.password = type,name,institute_name,email_id,password
        temp=0
        if self.type=='mentor':
            f=open('mentor.json','r+')
        else:
            f=open('student.json','r+')
        d={
            "Full Name":self.name,
            "Institute Name":self.institute_name,
            "Email ID":self.email_id,
            "Password":self.password
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                temp=1
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
            temp=1
        if temp==1:
            f.close()
            return True
        else:
            f.close()
            return False

    def Login(self,type,email_id,password):
        self.type,self.email_id,self.password = type,email_id,password
        d=0
        if self.type=='mentor':
            f=open('mentor.json','r+')
        else:
            f=open('student.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Email ID"]==self.email_id and content[i]["Password"]==self.password:
                d=1
                break
        if d==0:
            f.close()
            return False
        f.close()
        return True

    def New_Quiz_Creation(self,mentor_email_id,subject_name,quiz_title,number_of_questions,start_date,end_date) :
        self.Quiz_ID=''.join(random.choices(string.ascii_uppercase+string.digits,k=3))
        self.mentor_email_id,self.subject_name,self.quiz_title,self.number_of_questions,self.start_date,self.end_date = mentor_email_id,subject_name,quiz_title,number_of_questions,start_date,end_date
        self.quiz_questions = []
        temp=0
        for i in range(1,self.number_of_questions+1):
            self.temp_list = []
            self.ques_number = i
            print(f"Question number {self.ques_number} :")
            self.ques = input("Enter Question: ")
            self.option_1 = input("Enter Option 1: ")
            self.option_2 = input("Enter Option 2: ")
            self.option_3 = input("Enter Option 3: ")
            self.option_4 = input("Enter Option 4: ")
            self.correct_answer = input("Enter Correct answer's option number(for eg. 1 for option 1)): ")
            self.temp_list.append(self.ques_number)
            self.temp_list.append(self.ques)
            self.temp_list.append(self.option_1)
            self.temp_list.append(self.option_2)
            self.temp_list.append(self.option_3)
            self.temp_list.append(self.option_4)
            self.temp_list.append(self.correct_answer)
            self.quiz_questions.append(self.temp_list)
        f=open('quiz.json','r+')
        d={
            "Mentor Email ID":self.mentor_email_id,
            "Subject Name":self.subject_name,
            "Quiz Title":self.quiz_title,
            "Quiz ID":self.Quiz_ID,
            "Start Date":self.start_date,
            "End Date":self.end_date,
            "Quiz":self.quiz_questions
        }
        try:
            content=json.load(f)
            if d not in content:
                content.append(d)
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                temp=1
        except JSONDecodeError:
            l=[]
            l.append(d)
            json.dump(l,f)
            temp=1
        if temp==1:
            f.close()
            return True
        f.close()
        return False

    def View_Student_Marks(self,quiz_id,mentor_email_id) :
        self.quiz_id,self.mentor_email_id=quiz_id,mentor_email_id
        d=0
        f=open('quiz_marks.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Mentor Email ID"]==self.mentor_email_id and content[i]["Quiz ID"]==self.quiz_id:
                print("Student Email ID:",content[i]["Student Email ID"])
                print("Mark:",content[i]["Quiz Marks"])
                d=1
        if d==1:
            f.close()
            return True
        f.close()
        return False

    def Update_Existing_Quiz(self,quiz_id,question_number,mentor_email_id) :
        self.quiz_id,self.question_number,self.mentor_email_id = quiz_id,question_number,mentor_email_id
        d=0
        f=open('quiz.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False       
        for i in range(len(content)):
            endDate=datetime.strptime(content[i]["End Date"],'%m/%d/%Y')
            date2=datetime.today()
            date_diff=endDate-date2
            if date_diff.days>=0:
                if content[i]["Mentor Email ID"]==self.mentor_email_id and content[i]["Quiz ID"]==self.quiz_id:
                    self.temp_list=[]
                    self.ques = input("Enter Question: ")
                    self.option_1 = input("Enter Option 1: ")
                    self.option_2 = input("Enter Option 2: ")
                    self.option_3 = input("Enter Option 3: ")
                    self.option_4 = input("Enter Option 4: ")
                    self.correct_answer = input("Enter Correct answer's option number(for eg. 1 for option 1)): ")
                    self.temp_list.append(self.question_number)
                    self.temp_list.append(self.ques)
                    self.temp_list.append(self.option_1)
                    self.temp_list.append(self.option_2)
                    self.temp_list.append(self.option_3)
                    self.temp_list.append(self.option_4)
                    self.temp_list.append(self.correct_answer)
                    content[i]["Quiz"][self.question_number-1] = self.temp_list
                    f.seek(0) 
                    json.dump(content,f)
                    f.truncate()
                    f.close()
                    d=1
                    break
            if d==1:
                return True
        return False

    def Delete_Quiz(self,quiz_id):
        d=0
        self.quiz_id = quiz_id
        f=open('quiz.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Quiz ID"]==self.quiz_id:
                content.remove(content[i])
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                d=1
                break
        if d==0:
            f.close()
            return False
        f.close()
        return True

    def Update_Personal_Details(self,type,email_id,detail_to_be_updated_,updated_detail) :
        self.type,self.email_id,self.detail_to_be_updated_,self.updated_detail = type,email_id,detail_to_be_updated_,updated_detail
        if self.type=='mentor':
            f=open('mentor.json','r+')
        else:
            f=open('student.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Email ID"]==self.email_id :
                content[i][detail_to_be_updated_] = updated_detail
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                d=1
                break
        if d==0:
            f.close()
            return False
        f.close()
        return True

    def Update_Password(self,type,email_id,old_password,new_password) :
        self.type,self.email_id,self.old_password,self.new_password = type,email_id,old_password,new_password
        if self.type=='mentor':
            f=open('mentor.json','r+')
        else:
            f=open('student.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Email ID"]==self.email_id and content[i]["Password"]==self.old_password:
                content[i]["Password"] = new_password
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                d=1
                break
        if d==0:
            f.close()
            return False
        f.close()
        return True

    def Delete_Profile(self,type,email_id) :
        self.type,self.email_id = type,email_id
        if self.type=='mentor':
            f=open('mentor.json','r+')
        else:
            f=open('student.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Email ID"]==self.email_id:
                content.remove(content[i])
                f.seek(0)
                f.truncate()
                json.dump(content,f)
                d=1
                break
        if d==0:
            f.close()
            return False
        f.close()
        return True

    def View_Quizzes(self,mentor_email_id):
        self.mentor_email_id=mentor_email_id
        f=open('quiz.json','r+')
        d=0
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Mentor Email ID"]==self.mentor_email_id:
                print("Quiz ID:",content[i]["Quiz ID"],"\tSubject Name:",content[i]["Subject Name"],"\tQuiz Title:",content[i]["Quiz Title"],"\tDue Date:",content[i]["End Date"])
                d=1
        if d==0:
            f.close()
            return False
        f.close()
        return True


class student(mentor) :

    def View_Quiz_available(self):
        f=open('quiz.json','r+')
        d=0
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            endDate=datetime.strptime(content[i]["End Date"],'%m/%d/%Y')
            date2=datetime.today()
            date_diff=endDate-date2
            if date_diff.days>=0:
                print("Quiz ID:",content[i]["Quiz ID"],"\tSubject Name:",content[i]["Subject Name"],"\tQuiz Title:",content[i]["Quiz Title"],"\tDue Date:",content[i]["End Date"])
                d=1
        if d==0:
            f.close()
            return False
        f.close()
        return True
        

    def Take_Quiz(self,student_email_id,quiz_id):
        self.student_email_id,self.quiz_id=student_email_id,quiz_id
        d=0
        f=open('quiz.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Quiz ID"]==self.quiz_id:
                self.quiz_temp = content[i]["Quiz"]
                self.mentor_email = content[i]["Mentor Email ID"]
                self.subject_temp = content[i]["Subject Name"]
                self.quiz_title_temp = content[i]["Quiz Title"]
                self.count=0
                for i in range(len(self.quiz_temp)):
                    print(self.quiz_temp[i][0],".",self.quiz_temp[i][1])
                    print("1.",self.quiz_temp[i][2],"\n2.",self.quiz_temp[i][3],"\n3.",self.quiz_temp[i][4],"\n4.",self.quiz_temp[i][5])
                    self.correct_ans = input("Enter your answer(enter 1 for option 1): ")
                    if self.quiz_temp[i][6]==self.correct_ans:
                        self.count=self.count+1
                        d=1
                print(f"Your mark is {self.count}")
                f.close()
                f=open('quiz_marks.json','r+')
                d={
                    "Quiz ID":self.quiz_id,
                    "Student Email ID":self.student_email_id,
                    "Mentor Email ID":self.mentor_email,
                    "Subject Name":self.subject_temp,
                    "Quiz Title":self.quiz_title_temp,
                    "Quiz Marks":self.count
                }
                try:
                    content=json.load(f)
                    if d not in content:
                        content.append(d)
                        f.seek(0)
                        f.truncate()
                        json.dump(content,f)
                except JSONDecodeError:
                    l=[]
                    l.append(d)
                    json.dump(l,f)
                    f.close()
                return True
        if d==0:
            f.close()
            return False


    def View_Marks(self,student_email_id):
        self.student_email_id=student_email_id
        d=0
        f=open('quiz_marks.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
            return False
        for i in range(len(content)):
            if content[i]["Student Email ID"]==self.student_email_id:
                print("Quiz ID:",content[i]["Quiz ID"])
                print("Subject Name:",content[i]["Subject Name"])
                print("Quiz Title:",content[i]["Quiz Title"])
                print("Mark:",content[i]["Quiz Marks"])
                d=1
        if d==1:
            f.close()
            return True
        f.close()
        return False

    def View_Rank(self,student_email_id,rank_choice):
        self.student_email_id,self.rank_choice=student_email_id,rank_choice
        d=0
        f=open('quiz_marks.json','r+')
        try:
            content=json.load(f)
        except JSONDecodeError:
            f.close()
        self.temp_marks_list=[]
        self.temp_my_mark=0
        self.rank=0
        for i in range(len(content)):
            if content[i]["Quiz ID"]==self.rank_choice:
                self.temp_marks_list.append(content[i]["Quiz Marks"])
                if content[i]["Student Email ID"]==self.student_email_id and content[i]["Quiz ID"]==self.rank_choice:
                    self.temp_my_mark=content[i]["Quiz Marks"]
                    d=1
        if d==1:
            self.temp_sort_marks=[]
            self.temp_marks_list.sort(reverse=1)
            self.rank=self.temp_marks_list.index(self.temp_my_mark)
            print("Your rank is",self.rank+1)
            f.close()
            return True
        f.close()
        return False



    
mentor = mentor()
student = student()
temp=1
while temp == True:
    choice = input("Welcome to Quiz App !!! \n1.Mentor Register \n2.Mentor Login \n3.Student Register \n4.Student Login \n5.Exit \nEnter your Choice(for eg. enter 1 for mentor register): ")
    if choice == '1':
        type = "mentor"
        print("*** \nMentor Registration:-")
        mentor_name = input("Enter your Name: ")
        mentor_institute_name = input("Enter Institute Name: ")
        mentor_email_id  = input("Enter your Email ID: ")
        mentor_password = input("Enter your password: ")
        temp = mentor.Register(type,mentor_name,mentor_institute_name,mentor_email_id,mentor_password)
        if temp==True:
            print("Successfully registered as Mentor!!! \n***")
        else:
            print("User Already Exists! \n***")
        temp=True

    elif choice == '2':
        type = "mentor"
        print("Mentor Login:-")
        mentor_email_id  = input("Enter your Email ID: ")
        mentor_password = input("Enter your password: ")
        mentor_login_status = mentor.Login(type,mentor_email_id,mentor_password)
        if mentor_login_status == True:
            temp_1 = 1
            print("*** \nWelcome Mentor !!! ")
            while temp_1 == True:
                choice_2 = input("*** \n1.Create New Quiz \n2.View marks obtained by students \n3.Update Existing Quiz \n4.Delete Quiz \n5.Update Personal Details \n6.Update Password \n7.Delete My Profile \n8.Logout \n\nEnter your Choice(for eg. enter 1 for creating new quiz): ")
                if choice_2 == '1':
                    print("*** \nNew Quiz Creation:-")
                    subject_name = input("Enter Subject name of the Quiz: ")
                    quiz_title = input("Enter title for the Quiz: ")
                    number_of_questions = int(input("Enter total number of Questions you wish to add in the Quiz: "))
                    start_date = input("Enter Quiz Start Date(MM/DD/YYYY): ")
                    end_date = input("Enter Quiz End Date(MM/DD/YYYY): ")
                    if len(subject_name)*len(quiz_title)*len(start_date)*len(end_date)!=0 and number_of_questions!=0:
                        temp_1 = mentor.New_Quiz_Creation(mentor_email_id,subject_name,quiz_title,number_of_questions,start_date,end_date)
                        if temp_1==True:
                            print("Quiz Added Successfully \n***")
                        else:
                            print("Invalid Input! \n***")
                        temp_1=True
                    else:
                        print("Invalid Input \n***")
                        temp_1=True

                elif choice_2 == '2':
                    temp=mentor.View_Quizzes(mentor_email_id)
                    if temp==True:
                        quiz_id = input("*** \nEnter Quiz ID of the Quiz that you wish to see the Student's marks: ")
                        temp1 = mentor.View_Student_Marks(quiz_id,mentor_email_id)
                        if temp1==False:
                            print("Invalid Quiz ID \n***")
                            temp_1=True
                        temp_1=True
                    else:
                        print("No quiz created so far ! \n***")
                        temp_1=True

                elif choice_2 == '3':
                    temp=mentor.View_Quizzes(mentor_email_id)
                    if temp==True:
                        quiz_id = input("*** \nQuiz Updation:- \nEnter Quiz ID of the Quiz that you wish to update: ")
                        question_number = int(input("Enter Question number of the Quiz that you wish to update: "))
                        temp1 = mentor.Update_Existing_Quiz(quiz_id,question_number,mentor_email_id)
                        if temp1==True:
                            print("Quiz Updated!!! \n***")
                            temp_1=True
                        else:
                            print("Quiz ID invalid! \n***")
                            temp_1=True
                    else:
                        print("No Quiz created so far! \n***")
                        temp_1=True

                elif choice_2 == '4':
                    temp=mentor.View_Quizzes(mentor_email_id)
                    if temp==True:
                        quiz_id = input("*** \nQuiz Deletion: \nEnter Quiz ID of the Quiz that you wish to Delete: ")
                        temp1 = mentor.Delete_Quiz(quiz_id)
                        if temp1==True:
                            print("Quiz deleted Successfully!!! \n***")
                            temp_1=True
                        else:
                            print("Invalid Quiz ID \n***")
                            temp_1=True
                    else:
                        print("No Quiz Available! \n***")
                        temp_1=True

                elif choice_2 == '5':
                    type = "mentor"
                    detail_to_be_updated = input("***\nPersonal Details Updation:- \n1.Name \n2.Institute Name \nEnter your choice(enter 1 for Name): ")
                    if detail_to_be_updated == '1':
                        detail_to_be_updated_ = "Full Name"
                        updated_detail = input("Enter new value: ")
                        if len(updated_detail)*len(detail_to_be_updated_)!=0:
                            temp1 = mentor.Update_Personal_Details(type,mentor_email_id,detail_to_be_updated_,updated_detail)
                            if temp1==True:
                                print("Details updated successfully!!! \n***")
                                temp_1=True
                            else:
                                print("Invalid Input! \n***")
                                temp_1=True
                        else:
                            print("Invalid Input \n***")
                            temp_1=True
                    elif detail_to_be_updated == '2':
                        detail_to_be_updated_ = "Institute Name"
                        updated_detail = input("Enter new value: ")
                        if len(updated_detail)*len(detail_to_be_updated_)!=0:
                            temp1 = mentor.Update_Personal_Details(type,mentor_email_id,detail_to_be_updated_,updated_detail)
                            if temp1==True:
                                print("Details updated successfully!!! \n***")
                                temp_1=True
                            else:
                                print("Invalid Input! \n***")
                                temp_1=True
                        else:
                            print("Invalid input !!!")
                            temp_1=True
                    else :
                        print("Invalid input !!!")
                        temp_1=True
                    

                elif choice_2 == '6':
                    type = "mentor"
                    print("*** \nPassword Change:-")
                    old_password = input("Enter Old Password: ")
                    new_password = input("Enter New Password: ")
                    if len(new_password)!=0:
                        temp1 = mentor.Update_Password(type,mentor_email_id,old_password,new_password)
                        if temp1==True:
                            print("Password updated Successfully!!! \n***")
                            temp_1=True
                        else:
                            print("Incorrect Old password \n***")
                            temp_1=True
                    else:
                        print("New Password cannot be empty! \n***")
                        temp_1=True

                elif choice_2 == '7':
                    type = "mentor"
                    mentor.Delete_Profile(type,mentor_email_id)
                    temp_1 = 0

                elif choice_2 == '8':
                    temp_1 = 0
                    print("Logged out Successfully!!! \n***")

                else:
                    print("Enter numbers only between 1 to 8 !")

        else:
            print("Invalid Credentials \n***")
            temp = True

    elif choice == '3':
        type = "student"
        print("***")
        print("Student Registration:-")
        student_name = input("Enter your Name: ")
        student_institute_name = input("Enter Institute Name: ")
        student_email_id  = input("Enter your Email ID: ")
        student_password = input("Enter your password: ")
        temp = student.Register(type,student_name,student_institute_name,student_email_id,student_password)
        if temp==True:
            print("Successfully registered as Student!!! \n***")
        else:
            print("User Already Exists")

    elif choice == '4':
        type = "student"
        print("***")
        print("Student Login:-")
        student_email_id  = input("Enter your Email ID: ")
        student_password = input("Enter your password: ")
        student_login_status = student.Login(type,student_email_id,student_password)
        if student_login_status == True:
            temp_2 = 1
            print("*** \nWelcome Student!!!")
            while temp_2 == True:
                choice_3 = input("*** \n1.View All available Quiz \n2.Take Quiz \n3.View my Marks \n4.View My Rank \n5.Update Personal Details \n6.Update Password \n7.Delete My profile \n8.Logout \n\nEnter your Choice: ")
                if choice_3 == '1':
                    temp2 = student.View_Quiz_available()
                    if temp2==True:
                        temp_2=True
                    else:
                        print("No Quiz Available \n***")
                        temp_2=True

                elif choice_3 == '2':
                    temp_3=student.View_Quiz_available()
                    if temp_3==True:
                        quiz_id = input("*** \nEnter Quiz ID that you wish to attend: ")
                        temp2 = student.Take_Quiz(student_email_id,quiz_id)
                        if temp2==True:
                            print("Done")
                        else:
                            print("Invalid Quiz ID! \n***")
                        temp_2=True
                    else:
                        print("No Quiz Available \n***")
                        temp_2=True

                elif choice_3 == '3':
                    temp2 = student.View_Marks(student_email_id)
                    if temp2==False:
                        print("No Quiz Attended so far! \n***")
                    temp_2=True

                elif choice_3 == '4':
                    d=0
                    f=open('quiz_marks.json','r+')
                    try:
                        content=json.load(f)
                    except JSONDecodeError:
                        f.close()
                    for i in range(len(content)):
                        if content[i]["Student Email ID"]==student_email_id:
                            print("Quiz ID:",content[i]["Quiz ID"])
                            print("Subject Name:",content[i]["Subject Name"])
                            print("Quiz Title:",content[i]["Quiz Title"])
                            d=1
                        f.close()
                    if d==1:
                        rank_choice=input("*** \nEnter the Quiz ID of the Quiz you wish to see your Rank(exactly same as you seen..case sensitive): ")
                        temp2 = student.View_Rank(student_email_id,rank_choice)
                        if temp2==True:
                            temp_2=True
                        else:
                            print("Invalid Input! \n***")
                            temp_2=True
                    else:
                        print("No Quiz Attended so far! \n***")
                        temp_2=True

                elif choice_3 == '5':
                    type="student"
                    print("*** \nPersonal Details Updation:-")
                    detail_to_be_updated = input("1.Name \n2.Institute Name \nEnter your choice(enter 1 for Name): ")
                    if detail_to_be_updated == '1':
                        detail_to_be_updated_ = "Full Name"
                        updated_detail = input("Enter new value: ")
                        if len(updated_detail)*len(detail_to_be_updated_)!=0:
                            temp1 = student.Update_Personal_Details(type,student_email_id,detail_to_be_updated_,updated_detail)
                            if temp1==True:
                                print("Details updated successfully!!! \n***")
                                temp_2=True
                            else:
                                print("Invalid Input! \n***")
                                temp_2=True
                        else:
                            print("Invalid Input \n***")
                            temp_2=True
                    elif detail_to_be_updated == '2':
                        detail_to_be_updated_ = "Institute Name"
                        updated_detail = input("Enter new value: ")
                        if len(updated_detail)!=0:
                            temp1 = student.Update_Personal_Details(type,student_email_id,detail_to_be_updated_,updated_detail)
                            if temp1==True:
                                print("Details updated successfully!!! \n***")
                                temp_2=True
                            else:
                                print("Invalid Input! \n***")
                                temp_2=True
                        else :
                            print("Invalid input !!!")
                            temp_2=True
                    else :
                        print("Invalid input !!!")
                        temp_2=True

                elif choice_3 == '6':
                    type = "student"
                    print("*** \nPassword Change:-")
                    old_password = input("Enter Old Password: ")
                    new_password = input("Enter New Password: ")
                    if len(new_password)!=0:
                        temp1 = student.Update_Password(type,student_email_id,old_password,new_password)
                        if temp1==True:
                            print("Password updated Successfully!!! \n***")
                            temp_2=True
                        else:
                            print("Incorrect Old password \n***")
                            temp_2=True
                    else:
                        print("New Password cannot be empty! \n***")
                        temp_2=True

                elif choice_3 == '7':
                    type = "student"
                    student.Delete_Profile(type,student_email_id)
                    print("Deleted Successfully!!! \n***")
                    temp_2 = 0

                elif choice_3 == '8':
                    temp_2 = 0
                    print("Logged out Successfully!!! \n***")

                else:
                    print("Enter numbers only between 1 to 8 ! \n***")

        else:
            print("Invalid Credentials \n***")
            temp = True
    
    elif choice == '5':
        exit()
    
    else:
        print("\nEnter a number only between 1 to 5 ! \n***") 
        temp = True
class student:
    def __init__(self,name,idd,sem):
        self.name=name
        self.idd=idd
        self.sem=sem
        if "CE" in idd:
            self.branch="CE"
        elif "IT" in idd:
            self.branch="it"
        else:
            self.branch="cse"
class exam(student):
    def __init__(self,name,idd,sem,marks):
        super().__init__(name,idd,sem)
        self.marks=marks
    
class result(exam):
    def __init__(self,name,idd,sem,marks):
        super().__init__(name,idd,sem,marks) 
        self.sum=0
        for x in marks:
            self.sum+=x 
    def printResult(self):
        print("************RESULT**************")
        print("Name:",self.name,"\nidd:",self.idd,"\nSem:",self.sem,"\nBranch:",self.branch,"\nSum:",self.sum,"\nCgpa:",self.sum/100*1.5)    
        print("**********************************")
    
name=input("ENTER NAME: ")
idd=input("ENTER YOUR ID: ")
yr=int(input("ENTER YOUR SEM: "))
marks=[]
print("ENTER MARKS FOR ALL SUBJECTS: ")
for x in range(6):
    a=int(input())
    marks.append(a)
s1=result(name,idd,yr,marks)
s1.printResult()
print("\nAuthor: Ayush Luhar\nID NO. 21DCE052")

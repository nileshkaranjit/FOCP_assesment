from operator import contains
from random import choice

class mail:


    def __init__(self):
        pass
    def Check_mail(self):
        try:
            Email=input("Enter your popppleton email address:") # asks user for popppleton email address
            if "@" in Email:
                subemail=Email.split("@")
                
                
                if len(subemail)==2 and len(subemail[0])>=2 and subemail[1]== "pop.ac.uk": # to check the condition in email address
                    print("Hi",subemail[0],"! Thank you, and Welcome to PopChat!")
                    self.Charc(subemail[0])

                else:
                    print("Your Email is Invalid")
                    exit()
            else:
                print("Your Email is Invalid")
                exit()
        except Exception as error :

            print(f'UNEXPECTED ERROR: {error}')
            
    def Charc(self,name:str):
        try:


           
            User=input("Please enter some inputs:") # ask user for question
            if User.upper()=="NI!":
                exit()
            else:
                if "LIBRARY" in User.upper():
                    print("The library is closed today.")
                elif "WIFI" in User.upper():
                    print("WiFi is excellent across the campus.")
                elif "DEADLINE" in User.upper():
                    print("Your deadline has been extended by two working days.")
                elif "COFFEE" in User.upper():
                    print("The coffee is tasteless")
                elif "COLLEGE" in User.upper():
                    print("Welcome to your college!")
                elif "Class" in User.upper():
                    print("Be attentive in a class.")
                elif "Dress" in User.upper():
                    print("Your dress is dirty")
                elif User.upper()=="BYE" or User.upper()=="EXIT" or User.upper()=="DONE": # to exit the code if the given words are input
                    exit()
                

                else:
                    List_string=["Hmmm", "Oh, yes, I see","Tell me more"] # list that contains random value
                    print(choice(List_string))
            self.Charc(name)        
        except Exception as error :

            print(f'UNEXPECTED ERROR: {error}')            

if __name__=='__main__':
    _main_obj=mail()
    _main_obj.Check_mail()               


    
             


                
         


            
    


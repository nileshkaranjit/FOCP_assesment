class main():
    
    
    European_swallow_speed:float=0
    min_European_swallow_speed:float=0
    max_European_swallow_speed:float=0
    no_of_reading:int=0
    _main_obj=None
    def __init__(self):
        pass


    def func(self):
        reading=str(input("Enter your next reading:")) #takes user input for reading
        Val_per_hour=reading[1:]
        if reading == "":
            avg=0
            avg_under_MPH= 0
            max_under_MPH= 0
            min_under_MPH= 0
            if self.no_of_reading!=0:                
                avg=self.European_swallow_speed/self.no_of_reading # calculates the average 
                avg_under_MPH= avg/1.609344 # translate KPH to MPH
                max_under_MPH= self.max_European_swallow_speed / 1.609334 # converts max of kph into mph
                min_under_MPH= self.min_European_swallow_speed/1.609334 # converts min of kph into mph
            print("Max speed:",str(max_under_MPH)+"MPH" ,str(self.max_European_swallow_speed)+"KPH")
            print("Min speed:", str(min_under_MPH)+"MPH",str(self.min_European_swallow_speed)+"KPH")
            print("Avg speed",str(avg_under_MPH)+"MPH",str(avg)+"KPH")
        else:    
        
                
                
            try:
                Val_per_hour=float(Val_per_hour)
                if reading.upper().startswith('E'):
                    Float_val=float(Val_per_hour)
                    self.European_swallow_speed+=Float_val
                    if self.no_of_reading==0 or self.min_European_swallow_speed>Float_val:
                        self.min_European_swallow_speed=Float_val
                    if self.no_of_reading==0 or self.max_European_swallow_speed<Float_val:
                        self.max_European_swallow_speed=Float_val
                    self.no_of_reading+=1
                    self.func()  
            
                elif reading.upper().startswith('U'):
                    converted_val=float(Val_per_hour)*1.609344
                    self.European_swallow_speed+=converted_val
                    if self.no_of_reading==0 or self.min_European_swallow_speed>converted_val:
                        self.min_European_swallow_speed=converted_val
                    if self.no_of_reading==0 or self.max_European_swallow_speed<converted_val:
                        self.max_European_swallow_speed=converted_val
                    self.no_of_reading+=1  
                    self.func()

                else:
                    print("The value you entered is incorrect")
                    
                
            except ValueError: # checks the error in program
                print("The value you entered is incorrect")
            



if __name__=='__main__':
    _main_obj=main()
    _main_obj.func()



                

                
            
            

   

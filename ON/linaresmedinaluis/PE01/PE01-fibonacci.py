#function GetFibonacciSequence Param: integer SequenceNumber
def GetFibonacciSequence(SequenceNumber): 
    
    #Get the current length of the existing fibonnacci list
    Length=len(CacheFibonacci)
    
    #Minimal number allowed in Fibonacci is 0
    if SequenceNumber<0: 
        
        #Display the error on console
        print("Incorrect input") 
        
    #Number is lower than list length  
    elif SequenceNumber<=Length:
        
        #Return the current fibonacci list for edge
        return CacheFibonacci[SequenceNumber-1] 
    
    else: 
        #Calculate the sum sequence from exiting and previous numbers 
        CurrentFibonacci = GetFibonacciSequence(SequenceNumber-1)+GetFibonacciSequence(SequenceNumber-2) 
        
        #Add the new sum to the fibonacci list
        CacheFibonacci.append(CurrentFibonacci) 
        
        #Return the fibonacci list
        return CurrentFibonacci 
  
#Main module
try:
    Value = int(input("Please enter a number to get fibonacci sequence:\n"))
    
    #List for fibonacci numbers with initial numbers 0 and 1
    CacheFibonacci = [0,1]   
    
    #Call function
    Sequence = GetFibonacciSequence(Value)
    
    #Display sequence
    print(f'The fibonacci sequence for {Value} is {Sequence}') 
    
except ValueError:
  print (f'That was not a number, Please run it again')

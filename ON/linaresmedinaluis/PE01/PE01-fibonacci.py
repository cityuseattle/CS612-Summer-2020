#function GetFibonacciSequence Param: integer SequenceNumber
def GetFibonacciSequence(SequenceNumber): 
    
    #Get the current length of the existing fibonnacci list
    Length=len(CacheFibonacci)
        
    #Number is lower than list length  
    if SequenceNumber<=Length:
        
        #Return the current fibonacci list for edge
        return CacheFibonacci[SequenceNumber-1] 
    
    else: 
        #Calculate the sum sequence from exiting and previous numbers 
        CurrentFibonacci = GetFibonacciSequence(SequenceNumber-1)+GetFibonacciSequence(SequenceNumber-2) 
        
        #Add the new sum to the fibonacci list
        CacheFibonacci.append(CurrentFibonacci) 

        print(f'{CurrentFibonacci}\n') 
        #Return the fibonacci list
        return CurrentFibonacci 
  
#Main module
    
#Default value
Value = 100

#List for fibonacci numbers with initial numbers 0 and 1
CacheFibonacci = [0,1]   

print(f'The fibonacci sequence :\n0\n\n1\n ')

#Call function
Sequence = GetFibonacciSequence(Value)

#Display sequence
print(f'The fibonacci sequence for {Value} is {Sequence}\n\n') 
print(f'Good bye!\n\n') 


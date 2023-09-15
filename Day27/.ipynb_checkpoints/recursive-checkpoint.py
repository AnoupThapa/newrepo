#IF a function is called from the definition of the same function then it is called as a recursive function

a= 0
def repeat():
    global a
    print(a)
    a+=1
    if a ==10:
        return
    repeat()

repeat()
#Calculate the factorial of 5 in three different ways; normal loop, reduce() and recursive function
    
    
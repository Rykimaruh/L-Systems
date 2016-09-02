def AlgaeSystem(Iters,axiom): 
    startStr=axiom
    endStr = "" 
    for i in range(Iters): 
        endStr = algaeProcess(startStr) 
        startStr = endStr

    return endStr   

def algaeProcess(oldStr):
    newstr = ""
    for choice in oldStr:
        newstr = newstr + algaeRules(choice) #appends the old string and the new string like the A->B | B -> AB | AB -> BAB...etc

    return newstr

def algaeRules(choice):
    newStr=""
    if choice == 'A':
        newStr = 'AB'
    elif choice == 'B':
        newStr = 'A'
    else:
        newStr=choice
            
    return newStr 

def source():
    Algaeinstance = AlgaeSystem(7, "A")
    print(Algaeinstance)
source()
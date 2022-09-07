import pickle

informations=[]

f1=open("informations.pkl","rb")
informations=pickle.load(f1)
f1.close

def add():
    global informations

    num=int(input("学生序号： "))
    name_=input("学生姓名： ")
    inform={num:name_}

    informations.append(inform)

def delete():
    global informations
    del_one=int(input("被删除学生的序号： "))
    for i in informations:
        if del_one in i:
            del i[del_one]
        else:
            print(del_one)
    while {} in informations:
        informations.remove({})
    

def check():
    global informations
    print(informations)

def save():
    f1=open("informations.pkl","wb")
    pickle.dump(informations,f1,True)
    f1.close


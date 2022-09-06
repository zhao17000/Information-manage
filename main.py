import numpy as np

informations = []

def add():
    global informations

    num=int(input("学生序号： "))
    name_=input("学生姓名： ")
    inform={num:name_}

    informations.append(inform)

def delete():
    global informations
    del_one=input("被删除学生的序号： ")
    for i in informations:
        if del_one in informations:
            informations.pop(del_one)

def save():
    m=np.array(informations)
    np.save('informations.npy',m)

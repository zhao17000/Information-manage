import pickle

a=[]
b=pickle.dumps(a)
pickle.dump(b,open("test.dbl",mode="wb"))
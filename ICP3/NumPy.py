import numpy as np

vector=np.random.randint(0,high=20,size=15,dtype=np.int32)
print(vector)

reshape=vector.reshape((3,5))
print(reshape)

#maxRep=np.max(reshape,axis=1)
#print(maxRep)

reshape[np.where(reshape==np.max(reshape,axis=1,keepdims=True))] = 0
print("Result:\n",reshape)

import numpy as np

a = np.array([[1,2],[3,4]])

(sign , logdet) = np.linalg.slogdet(a)
print((sign,logdet))
print(sign * np.exp(logdet))


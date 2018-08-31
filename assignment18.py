question no1.
"
import numpy as np
a=np.random.random((10,1))
>>> np.mean(a)
0.5989342172167671


"

question no2.
"
import numpy as np
>>> a=np.random.random((20,1))
>>> print(np.std(a))
0.2574241603822529
>>> print(np.var(a))
0.06626719834850786
 
"


question no3.

"
import numpy as np
>>> a=np.random.random((10,20))
>>> b=np.random.random((20,25))
>>> c=np.matmul(a,b)
>>> np.shape(c)
(10, 25)
print(c.sum())
1179.5001125395986



"
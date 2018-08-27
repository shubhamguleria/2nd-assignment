question no.1
"
email1="zuck26@facebook.com"
>>> email2="page33@google.com"
>>> email3="jeff42@amazon.com"
>>> out=re.split(r'[@.]',email1)
>>> out2=re.split(r'[@.]',email2)
>>> out3=re.split(r'[@.]',email1)
print(out,out2,out3)
['zuck26', 'facebook', 'com'] ['page33', 'google', 'com'] ['zuck26', 'facebook', 'com']
"


question no.2

"
import re
>>> text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
var=re.findall("[bB]\w*",text)
>>> print(var)
['Betty', 'bought', 'bit', 'butter', 'But', 'butter', 'bitter', 'bought', 'better', 'butter', 'bitter', 'butter', 'better']

"


question no.3

"
import re
st=A, very very; irregular_sentence
txt=re.sub(r'\W'," ",st)
>>> sys=re.sub(r'\_'," ",txt)
>>> print(sys)
A  very very  irregular sentence
>>> 


"
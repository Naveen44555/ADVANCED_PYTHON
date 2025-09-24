# x=['8849398290','9642159329','8790163240']
# op=(map() lambda  x:x(x.push('+91')))
# print(op)

x=[1,2,3,[1,2,3],4,5,6,[3,4,5,[2,3,4,[1,2,3]]]]
sum=0
for i in x:
    for j in i:
        print(j)


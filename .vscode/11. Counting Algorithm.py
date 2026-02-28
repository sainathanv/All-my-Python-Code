# Simply writing a code which counts the number of pass and failures in a class!!
a=(35,40,25,50,70,97,86,43)
count=0
i=0
fail=0
for i in range(8):
    if a[i]>=40:
        count=count+1
        i+=1
    else:
        fail=fail+1
        i+=1
print("The number of pass marks: ", count)
print("The number of Failures = ", fail,"     Sad eyy :(")
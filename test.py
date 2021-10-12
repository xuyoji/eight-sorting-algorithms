import os, time, random

n = int(input('please input n '))
testcase = open(os.getcwd()+'/testcase', "w")
testcase.write(str(n)+'\n')
print('generating testcase')
for i in range(n):
	testcase.write(str(random.randint(-n,n)) + '\n')
testcase.close()
print('finished!')

print('sorting...')
algorithms = ["bubble", "altbubble", "insertion", "heap", "merge", "quick", "bucket", "radix"]

for i in algorithms:
	start = time.time()
	os.system("./test -" + i + "< testcase >" + i)
	end = time.time()
	print('	' + i + 'sort', "=", end - start, "s")
		
os.system("diff radix " + "bucket")

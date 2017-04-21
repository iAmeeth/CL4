#Ameeth Kanawaday 4430
#Assignment A3 
from mpi4py import MPI
import test
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
	i=size-1
	while i>0:
		data = comm.recv(source=i)#,tag=11)
		print "--------processor ", i, "---------"
		print "filename: ", data[0], "\nExecutable stmts: ", data[1], "\nMiss:", data[2], "\nMissing: ", data[3]
		i=i-1
		print data
		
elif rank ==1:
	import coverage
	import test
	c=coverage.Coverage()
	c.erase()
	c.start()
	test.func1()
	c.stop()
	a=c.analysis(test)
	comm.send(a, dest=0)# tag=11)
elif rank ==2:
	import coverage
	import test
	c=coverage.Coverage()
	c.erase()
	c.start()
	test.func2()
	c.stop()
	a=c.analysis(test)
	comm.send(a, dest=0)# tag=11)

#test.py
def func1():
	a=10
	if a<50:
		a=a*2
	else:
		a=a/2
	print "a in function 1: ", a

def func2():
	a=60
	if a<50:
		a=a*2
	else:
		a=a/2
	print "a in function 2: ", a

[pict@ARCH_pict A3]$ mpiexec -np 2 python2 a3.py               
a in function 1:  20
--------processor  1 ---------
filename:  /home/pict/CL4/A3/test.py 
Executable stmts:  [1, 2, 3, 4, 6, 7, 9, 10, 11, 12, 14, 15] 
Miss: [1, 6, 9, 10, 11, 12, 14, 15] 
Missing:  1, 6, 9-15
[pict@ARCH_pict A3]$ coverage test.py

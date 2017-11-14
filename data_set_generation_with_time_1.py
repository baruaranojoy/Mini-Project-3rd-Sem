from random import randint
sorte = []
counter = 0
flag = 0
negative = []
posetive = []
k = 0
jj = 0
total_time = 60

fobj = open("facebook_combined.txt")

#def nego(c):
#    time = c[0]
#    #addtime = total_time - randint(0,time)
#    addtime = 61
#    frompoint = c[1]
#    topoint = c[2]
#    topoint = topoint * -1
#    total = [time , frompoint , topoint]
#    postopoint = topoint * 1;
#    postotal = [addtime , frompoint , postopoint ]
#    negative.append(total)
#    posetive.append(postotal)

def nego(c):
    t = 0
    a = 0
    b = 0
    c1 = c[0]
    c2 = c[1]
    c3 = c[2]
    c3 = c3 * -1
    #print "__________________________________"
    #print c1
    #print "----------------"
    #t = total_time - randint(t,total_time)
    c1 = c1 + randint(c1,total_time)
    #print c1
    final = [c1 , c2 , c3]
    #print "-----------------"
    #print final
    #print "__________________________________"
    negative.append(final)

for line in fobj:
    a,b = map(int,line.rstrip().split())
    t = randint(0,total_time)
    c = [t , a , b]
    d = randint(0,100)
    if d > 30 and d < 75 and d % 2 == 0:
        nego(c)
    sorte.append(c)
    
fobj.close()
sorte.sort()
negative.sort()
counter_nego = 0

for k in range(len(negative)):
    h = negative[k]
    #print h
    sorte.append(h)
    counter_nego = counter_nego + 1
print "-----------------------------------------------"
print "Total number of negative number generated is : "
print counter_nego
print "________________________________________________"

#for jj in range(len(posetive)):
#    g = posetive[jj]
#    sorte.append(g)

sorte.sort()

jj = 0
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"
print "------------------------------------------------"

count = 0

f = open("mini_project_data_set_with_time_only.txt", "w")

for jj in range(len(sorte)):
    #print sorte[jj]
    loaf = sorte[jj]
    a1 = loaf[0]
    a2 = loaf[1]
    a3 = loaf[2]
    final = str(a1)+' '+str(a2)+' '+str(a3)+'\n'
    f.write(final)
    count = count + 1
f.close

print "Total number of elements is.."
print count

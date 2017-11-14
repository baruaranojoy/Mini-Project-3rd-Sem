fpos = open("final_formated_cutted_dataset_posetive.txt")
fneg = open("final_formated_cutted_dataset_negative.txt")
f_final = open("final_formated_cutted_procressed_dataset.txt", "w")


posetive = []
negative = []

for line in fpos:
    a,b = map(int,line.rstrip().split())
    c = [a , b]
    posetive.append(c)

for line in fneg:
    a,b = map(int,line.rstrip().split())
    c = [a , b]
    negative.append(c)

posetive.sort()
negative.sort()

count_pos = 0
k = 0
#print "________________________"
#print "Printing posetive ::"
#print "________________________"
for k in range(len(posetive)):
    #print posetive[k]
    count_pos = count_pos + 1
#print "________________________"
#print "Total number of posetive terms is ::"
#print "------------------------"
#print count_pos
#print "________________________"

count_neg = 0
k = 0
#print "________________________"
#print "Printing negative ::"
#print "________________________"
for k in range(len(negative)):
    #print negative[k]
    count_neg = count_neg + 1
#print "________________________"
#print "Total number of negative terms is ::"
#print "------------------------"
#print count_neg
#print "________________________"


k = 0
l = 0
counter = 0
position = []
for k in range(len(negative)):
    nego = negative[k]
    neg0 = nego[0]
    neg1 = nego[1]
    neg1 = neg1 * -1
    nego = [neg0 , neg1]
    for l in range(len(posetive)):
        pose = posetive[l]
        if nego == pose:
            counter = counter + 1
            position.append(l)
            #final.append(pose)
        #else:
            #final.append(pose)
#print "____________________________"
#print "Total number of matches : "
#print "----------------------------"
#print counter
#print "____________________________"


k = 0
counter_position = 0
for k in range(len(position)):
    #print position[k]
    counter_position = counter_position + 1
#print "____________________________"
#print "Total number of elements in the final list is : "
#print "----------------------------"
#print counter_final
#print "____________________________"
    

final = []
counter_final = 0 
def procress(g):
    posetive[g] = [0, 0]
    
k = 0
for k in range(len(position)):
    procress(position[k])


k = 0
for k in range(len(posetive)):
    if posetive[k] != [0, 0]:
        final.append(posetive[k])
k = 0
for k in range(len(final)):
    d = final[k]
    #print d
    d0 = d[0]
    d1 = d[1]
    ff = str(d0) + ' ' + str(d1) + '\n'
    f_final.write(ff)

    
fpos.close()
fneg.close()


print "________________________"
print "Total number of posetive terms is ::"
print "------------------------"
print count_pos
print "________________________"

print "________________________"
print "Total number of negative terms is ::"
print "------------------------"
print count_neg
print "________________________"

print "____________________________"
print "Total number of matches : "
print "----------------------------"
print counter
print "____________________________"

print "____________________________"
print "Total number of elements matched with valid position : "
print "----------------------------"
print counter_position
print "____________________________"

print "____________________________"
print "Total number of elements present in final : "
print "----------------------------"
print len(final)
print "____________________________"   

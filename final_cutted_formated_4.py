fobj = open("final_cutted_dataset.txt")
f = open("final_formated_cutted_dataset.txt", "w")

for line in fobj:
    a,b,c = map(int,line.rstrip().split())
    e = [b,c]
    d1 = e[0]
    d2 = e[1]
    final = str(d1) + ' ' + str(d2) + '\n'
    f.write(final)
    #print e
fobj.close()
f.close()

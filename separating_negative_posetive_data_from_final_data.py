fobj = open("final_formated_cutted_dataset.txt")
fneg = open("final_formated_cutted_dataset_negative.txt", "w")
fpos = open("final_formated_cutted_dataset_posetive.txt", "w")

for line in fobj:
    a,b = map(int,line.rstrip().split())
    if b < 0:
        final = str(a) + ' ' + str(b) + '\n'
        fneg.write(final)
    if b > 0 or b == 0:
        final = str(a) + ' ' + str(b) + '\n'
        fpos.write(final)
fobj.close()
fneg.close()
fpos.close()

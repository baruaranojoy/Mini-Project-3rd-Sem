f = open("mini_project_data_set_with_time_only.txt")
fopen = open("final_cutted_dataset.txt", "w")
time = 60
count = 0
for line in f:
    a,b,c = map(int,line.rstrip().split())
    count = a
    if count < time+1:
        final = str(a) + ' ' + str(b) + ' ' + str(c) + '\n'
        fopen.write(final)
f.close()
fopen.close()

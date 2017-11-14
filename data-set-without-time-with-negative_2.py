fobj = open("mini_project_data_set_with_time_only.txt")
f = open("mini_project_dynamic_graph_data_set_without_time.txt", "w")

for line in fobj:
    a,b,c = map(int,line.rstrip().split())
    e = [b,c]
    d1 = e[0]
    d2 = e[1]
    final = str(d1) + ' ' + str(d2) + '\n'
    f.write(final)
    #print e
fobj.close()

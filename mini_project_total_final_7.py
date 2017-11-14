import time
import numpy as np
import matplotlib.pyplot as plt
from scipy import linalg as LA

from matplotlib import style
style.use("ggplot")
from sklearn.cluster import KMeans
from array import array

start_time = time.clock()

tota = []
total_data = []
total_data_set = []
clustered_data = []
cluster_0 = []
cluster_1 = []
cluster_2 = []
cluster_node_0 = []
cluster_node_1 = []
cluster_node_2 = []

# this function is used to count the total number of entries in the given dataset i.e., number of edges
def count():
    c = []
    counter = 0
    fobj = open("final_formated_cutted_procressed_dataset.txt")
    counter = 0
    for line in fobj:
        a,b = map(int,line.rstrip().split())
        c = [a, b]
        total_data_set.append(c)
        counter = counter + 1
    fobj.close()
    return counter



# this function is used to find the node to which maximum number of edges are connected 
def edge_check(total):
    x=0
    y=0
    prev=0
    count = 0
    maxx=0
    fobj = open("final_formated_cutted_procressed_dataset.txt")
    for line in fobj:
        x,y = map(int,line.rstrip().split())
        if x==prev:
            count = count + 1
            if count > maxx:
                maxx = count
                num = x
        else:
            prev = x
            count = 1
    print ("The number is to which maimum number of edges are connected is : ")
    print (num)
    fobj.close()
    return maxx


# this function is used to clculate the total number of nodes in the graph
def calculate_nodes():
    fobj = open("final_formated_cutted_procressed_dataset.txt")
    total = 0
    count = 1
    array = []
    ckeck = 0
    i = 0
    for line in fobj:
        a,b = map(int,line.rstrip().split())
        array.append(a)
        total = total + 1
    array.sort()
    prev = array[0]
    count = 1
    for h in range(total):
        if prev != array[h]:
            tota.append(prev)
            count = count + 1
            prev = array[h]
    fobj.close()
    return count

def centrality_denominator(f):
    summ = 0
    ma = 0
    total = 0
    length = len(f)
    for i in range(length-2):
        q = f[i+1]
        for j in range(maxx-1):
            p = two_two[j]
            if q == p[0]:
                summ = summ + p[1] - 1
                if ma < p[1]:
                    ma = p[1]
    total = ma*length - summ
    return total

def centrality_neumarator(f):
    summ = 0
    ma = 0
    total = 0
    length = len(f)
    for i in range(length-1):
        q = f[i]
        for j in range(maxx-1):
            p = two_two[j]
            if q == p[0]:
                summ = summ + p[1]
                if ma < p[1]:
                    ma = p[1]
    total = ma*length - summ
    return total

two_two = []
two = []

def get_row(x):
    z = []
    g = len(two)
    for i in range(g):
        c = two[i]
        if c[0] == x:
            z = c
            break
    return z

def compare(f,q,count_total):
    x = len(f)
    y = len(q)
    for i in range(y-1):
        k = q[i+1]
        for j in range(x-1):
            l = f[j+1]
            if k == l:
                count_total = count_total + 1
    #print count_total
    return count_total

    
def multiplier_neumarator_func(f):
    count_total = 0
    for i in range(len(f)-1):
        x = f[i+1]
        q = get_row(x)
        count_total = compare(f,q,count_total)
    return count_total
                

central = []
##################################
# thses 3 are only used at last
cc_node = []
freeman_degree_node = []
degree_centrality_node = []
##################################
def centrality():
    degree_centrality = 0.0
    for i in range(maxx-1):
        multiplier_neumarator = 0
        f = two[i]
        k = len(f)
        k = k-1
        multiplier = float((k*(k-1))/2)
        if multiplier == 0 or k == -1:
            multiplier = 1.0
        multiplier_neumarator = float(multiplier_neumarator_func(f))
        total_multiplier = multiplier_neumarator / multiplier
        # total_multiplier is the cc value
        xyz = [f[0] , total_multiplier]
        cc_node.append(xyz)
        #print "---------------"
        #print total_multiplier
        #print "---------------"
        neumarator = float(centrality_neumarator(f))
        denominator = float(centrality_denominator(f))
        if denominator == 0:
            denominator = 1
        # neumarator/denominator gives freemans degree centrality
        llll = neumarator/denominator
        yzx = [f[0] , llll]
        freeman_degree_node.append(yzx)
        degree_centrality = (neumarator/denominator) * total_multiplier
        # degree_centrality gives the more enhanced degree centrality
        zxy = [f[0] , degree_centrality]
        degree_centrality_node.append(zxy)
        sweet = [degree_centrality,f[0]]
        central.append(sweet)
    #print "######################################################"    
    central.sort()
    #for xy in range(len(central)):
        #print central[xy]



# check
def check(x):
    count = 0
    one = []
    one.append(x)
    one_one = []
    one_one.append(x)
    fobj = open("final_formated_cutted_procressed_dataset.txt")
    for line in fobj:
        a,b = map(int,line.rstrip().split())
        if a == x:
            one.append(b)
            count = count + 1
    one_one.append(count)
    two_two.append(one_one)
    two.append(one)
    #print one_one
    #print "**********************************************************"
    #print one
    #print "----------------------------------------------------------"
    

# function used to make the edge list
def two_D_list():
    for i in range(maxx-1):
        x = tota[i]
        check(x)

total_data = tota


# this function is used for clustering 
def clustering():
    x = total_data
    
    plt.scatter(x,x)

    X = np.array(total_data_set)

    kmeans = KMeans(n_clusters=3)
    kmeans.fit(X)

    centroids = kmeans.cluster_centers_
    labels = kmeans.labels_

    #print(centroids)
    #print(labels)

    colors = ["g.","r.","c."]

    for i in range(len(X)):
        #print("coordinate:",X[i],"label:", labels[i])
        if labels[i] == 0:
            cluster_0.append(X[i])
        if labels[i] == 1:
            cluster_1.append(X[i])
        if labels[i] == 2:
            cluster_2.append(X[i])
        plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)

    plt.scatter(centroids[:, 0],centroids[:, 1], marker = "x", s=150, linewidth = 5, zorder = 10)
    
    for i in range(len(cluster_0)):
        d = cluster_0[i]
        cluster_node_0.append(d[0])

    for i in range(len(cluster_1)):
        d = cluster_1[i]
        cluster_node_1.append(d[0])

    for i in range(len(cluster_2)):
        d = cluster_2[i]
        cluster_node_2.append(d[0])

        
# **********this part is for the processing of the clusters********** 


def procress_cluster(cluster_node):
    done_central = []
    for za in range(len(cluster_node)):
        element = cluster_node[za]
        for xy in range(len(central)): 
            kl = central[xy]
            reqd_element = kl[1]
            if reqd_element == element:
                done_central.append(kl)
    return done_central

# **********in this part the processing of the clusters ends**********


# finding the largest element entered in the file		
total = count()
print ("Total number of edges : ")
print (total)
maxx = calculate_nodes()
print ("Total number of nodes in the graph : ")
print (maxx)
maxx_edge = edge_check(total)
print ("Maximum number of nodes to which one node is connected : ")
print (maxx_edge)
two_D_list()
centrality()

#################################################################
#################################################################
#####       Cluster part is commented here
#####       reveeve when needed
#################################################################
#################################################################

#print "Now starting the clustering part wait......"
#clustering()

##################################################################
##################################################################
####
####    --------------------------------------------------------
####
###################################################################
###################################################################




# "Cluster 0"
#print cluster_node_0
#print "Cluster 1"
#print cluster_node_1
#print "Cluster 2"
#print cluster_node_2
ss = len(cluster_node_0) + len(cluster_node_1) + len(cluster_node_2)
print ("-------------------------------------")
print ("total size")
print (ss)
print ("-------------------------------------")

# calling of functions to procress the clusters..
done_1 = []
done_2 = []
done_3 = []

done_1 = procress_cluster(cluster_node_0)
done_2 = procress_cluster(cluster_node_1)
done_3 = procress_cluster(cluster_node_2)


# taking out the final nodes from the various small variables for final processing
# the variables for this purpous are 
# 1) central ____ it stores data about the total given data set in he format [[degree_centrality , unique_edge],[degree_centrality , unique_edge],.....]
# 2) done_1 ____ it stores data about the cluster number 1 in he format [[degree_centrality , unique_edge],[degree_centrality , unique_edge],.....]
# 3) done_2 ____ it stores data about the cluster number 2 in he format [[degree_centrality , unique_edge],[degree_centrality , unique_edge],.....]
# 4) done_3 ____ it stores data about the cluster number 3 in he format [[degree_centrality , unique_edge],[degree_centrality , unique_edge],.....]

# now main aim is to sort out all the nodes from these 4 lists whose degree_centrality is 0

# sorting the central list\\\\\

final_sweet_list = []         # stores the list in format [degree_centrality , element] 
final_sweet_element = []	   # stores the list of all the required elements

for abc in range(len(central)):
	element = central[abc]
	reqd_element = element[0]
	if reqd_element == 0:
		final_sweet_list.append(element)
		final_sweet_element.append(element[1])

# sorting the done_1 list\\\\\

final_sweet_list_done_1 = []         # stores the list in format [degree_centrality , element] 
final_sweet_element_done_1 = []	   # stores the list of all the required elements

for abc in range(len(done_1)):
	element = done_1[abc]
	reqd_element = element[0]
	if reqd_element == 0:
		final_sweet_list_done_1.append(element)
		final_sweet_element_done_1.append(element[1])

# sorting the done_2 list\\\\\

final_sweet_list_done_2 = []         # stores the list in format [degree_centrality , element] 
final_sweet_element_done_2 = []	   # stores the list of all the required elements

for abc in range(len(done_2)):
	element = done_2[abc]
	reqd_element = element[0]
	if reqd_element == 0:
		final_sweet_list_done_2.append(element)
		final_sweet_element_done_2.append(element[1])

# sorting the done_3 list\\\\\

final_sweet_list_done_3 = []         # stores the list in format [degree_centrality , element] 
final_sweet_element_done_3 = []	   # stores the list of all the required elements

for abc in range(len(done_3)):
	element = done_3[abc]
	reqd_element = element[0]
	if reqd_element == 0:
		final_sweet_list_done_3.append(element)
		final_sweet_element_done_3.append(element[1])









#this function is used to process the edge list and store data
#in the form of [node , degree]
degree_node = []
k = 0
for k in range(len(two)):
    first = two[k]
    first_element = first[0] 
    length = len(first) - 1
    h = [first_element , length]
    degree_node.append(h)
print ("Length of degree_node")
print (len(degree_node))


#finding the max. possible size of each element in degree_node
k = 0
max_size = 0.0
for k in range(len(degree_node)):
    h = degree_node[k]
    size = h[1]
    if size > max_size:
        max_size = size
print ("Max size is")
print (max_size)

#finding how many are comparable of 50% with respect to max
k = 0
counter_ee = 0
afford = 0.0
selected_eigen_elements = []
for k in range(len(degree_node)):
    h = degree_node[k]
    size = h[1]
    afford = max_size *(50.0/100.0)
    #print afford
    if size > afford:        
        counter_ee = counter_ee + 1
        selected_eigen_elements.append(h[0])
print ("Possible data entry is")
print (counter_ee)
selected_eigen_elements.sort()

#creating the matrix for the purpous for the eigane value purpouse
print ("Printing data for eigen value matrix")
print (len(final_sweet_list))
k = 0
Matrix = [[0 for x in range(counter_ee)] for y in range(counter_ee)]


#entering data in the matrix as the substraction of degree of both
#rows and columns of the matrix of a particular element

#find the degree of the required elements requested from below part
def check_degree(recieved_elements):
    k = 0
    for k in range(len(degree_node)):
        h = degree_node[k]
        #print h
        if recieved_elements == h[0]:
            #print h[0]
            return h[1] 
#k=0
#for k in range(len(degree_node)):
#    print degree_node[k]

#print "Selected eigen elements are : "
#print selected_eigen_elements
k = 0
j = 0
total = 0
first = 0
second = 0
first_element = 0
second_element = 0
total = 0
for k in range(len(selected_eigen_elements)):
    for j in range(len(selected_eigen_elements)):
        if k == j:
            Matrix[k][j] = 0
        else:
            first = selected_eigen_elements[k]
            second = selected_eigen_elements[j]
            first_element = check_degree(first)
            second_element = check_degree(second)
            #first_element = 0
            #second_element = 0
            total = abs(first_element - second_element)
            Matrix[k][j] = total

#printing the matrix created for value of eigen vector
#print "Printing the matrix for the igaen vector calculation"
#for k in range(counter_ee):  
    #print Matrix[k]

#processsing the matrix created to get the eigen value
selected_eigen_vector_node = []
eigen_vectors_of_matrix,eigen_values_of_matrix = LA.eig(Matrix)
print ("--------------------")
print ("Eigen value are : ")
print ("____________________")
#print eigen_values_of_matrix
print ("--------------------")
print ("Eigen vectors are : ")
print ("____________________")
#print eigen_vectors_of_matrix
print ("--------------------")
#k = 0
#for k in range(len(eigen_vectors_of_matrix)):
#    if eigen_vectors_of_matrix[k] > 0:
#        #h = eigen_vectors_of_matrix[k]
#        selected_eigen_vector_node.append(selected_eigen_elements[k])

#creating modified version of selected_eigen_vector_node is selected_eigen_vector_node_2
k = 0
selected_eigen_vector_node = []
for k in range(len(eigen_vectors_of_matrix)):
    selected_eigen_vector_node.append(selected_eigen_elements[k])

#now sorting selected_eigen_vector_node
selected_eigen_vector_node.sort()


#print "The selected eigrn vector nodes are : "
#print selected_eigen_vector_node

print ("The selected eigrn vector nodes are : ")
print (selected_eigen_vector_node)


#finding out the posetive elements and their locations
#so that the perfect edge can be found..
k = 0
j = 0
final_procressed_eigen = []
for k in range(counter_ee):
    tupple = eigen_values_of_matrix[k]
    for j in range(counter_ee):
        element = tupple[j]
        if element >= 0:
            h = [k , j]
            final_procressed_eigen.append(h)


print ("the final_procressed_eigen : ")
print (final_procressed_eigen)  


#finding the edges
def find(recieved_element):
    k = 0
    for k in range(len(selected_eigen_elements)):
        if recieved_element == k:
            #print selected_eigen_elements[k]
            return selected_eigen_elements[k]


k = 0
first_element = 0
second_element = 0
ultimate_list = []
for k in range(len(final_procressed_eigen)):
    element = final_procressed_eigen[k]
    first = element[0]
    second = element[1]
    first_element = find(first)
    second_element = find(second)
    ultimate_list.append(first_element)
    ultimate_list.append(second_element)


#sorting and printing the ultimate list
ultimate_list.sort()
#print ultimate_list


#finding out the unique elements in the ultimate_list
k = 0
f_ultimate_list = set(ultimate_list)
final_ultimate_list = list(f_ultimate_list)

#printing the final_ultimate_list
final_ultimate_list.sort()
print ("final_ultimate_list is : ")
print (final_ultimate_list)




###################################################################
###################################################################
#    final procressing of the data collected and procressed 
#    starts at this place
###################################################################
###################################################################

#declaering all the function definations

# declairing eigen_returned function (1)
def pos(rec):
    k = 0
    for k in range(len(selected_eigen_elements)):
        if rec == selected_eigen_elements[k]:
            return k

def eigen_returned(recieved_element):
    k = 0
    count = 0
    counter  = 0
    position = pos(recieved_element)
    for k in range(len(eigen_values_of_matrix)):
        if position == 0 and k == 0:
            counter = counter - 1
            count = count - eigen_values_of_matrix[0][0]
        if eigen_values_of_matrix[position][k] > 0:
            count = count + eigen_values_of_matrix[position][k]
            counter = counter + 1
        if eigen_values_of_matrix[k][position] > 0:
            count = count + eigen_values_of_matrix[k][position]
            counter = counter + 1
    gg = count / counter
    #print "_____________________"
    #print "Eigen value : "
    return gg
            
# declairing degree_return function (2)

def degree_return(recieved_element):
    k = 0
    for k in range(len(degree_node)):
        l = degree_node[k]
        if l[0] == recieved_element:
            #print "_____________________"
            #print " Degree value : "
            return l[1]

# declareing cc_return function (3)

def cc_return(recieved_element):
    k = 0
    for k in range(len(cc_node)):
        ll = cc_node[k]
        if ll[0] == recieved_element:
            #print "_____________________"
            #print "CC value : "
            return ll[1]

# declareing free_man_degree_centrality_return function (4)

def free_man_degree_centrality_return(recieved_element):
    k = 0
    for k in range(len(freeman_degree_node)):
        ll = freeman_degree_node[k]
        if ll[0] == recieved_element:
            #print "_____________________"
            #print "Free man degree centrality value : "
            return ll[1]


# declareing degree_return function (5)

def degree_centrality_node_return(recieved_element):
    k = 0
    for k in range(len(degree_centrality_node)):
        ll = degree_centrality_node[k]
        if ll[0] == recieved_element:
            #print "_____________________"
            #print "Degree value : "
            return ll[1]




            

# checking the number of elements that passed the eigen
# value test if its one(1) then its the most influential
# node if its more than one then comparison needs to take place
final_ultimate = []

h = len(selected_eigen_vector_node)
if h == 1:
    print ("________________________________________________________________________________")
    print ("The most influential node in all these nodes and the whole of the graph is :")
    print (selected_eigen_vector_node[0])
    print ("________________________________________________________________________________")

else:
    k = 0
    eigen_ret = 0
    degree_ret = 0
    cc_ret = 0
    free_man_degree_centrality_ret = 0
    degree_ret = 0
    for k in range(len(selected_eigen_vector_node)):
        element = selected_eigen_vector_node[k]
        #getting eigen value of the element
        eigen_ret = eigen_returned(element)
        #getting degree of the element
        degree_ret = degree_return(element)
        #getting CC value of the element
        cc_ret = cc_return(element)
        #getting freeman's degree centrality
        free_man_degree_centrality_ret = free_man_degree_centrality_return(element)
        #getting degree centrality
        degree_centrality_ret = degree_centrality_node_return(element)
        #geting all these data in a variable
        total = [eigen_ret, degree_ret, cc_ret, free_man_degree_centrality_ret, degree_centrality_ret]
        final_ultimate.append(total)
    print ("___________________________________________________")
    print ("Final ultimate is : ")
    print ("---------------------------------------------------")
    k = 0
    for k in range(len(final_ultimate)):
        l = final_ultimate[k]
        print (l)
    print ("___________________________________________________")

    ###############################################################
    #########       Comparison part follows from here      ########
    ###############################################################

    


###################################################################
###################################################################
#     final procerss ends here
#
###################################################################
###################################################################





# printing the final lists for central is are 

#print "The elements selected from the total given data set is: "
#print final_sweet_element
#print "The elements selected with its degree centrality is: "
#print final_sweet_list

# printing the final lists for the done_1 are 

#print "The elements selected from the calculated cluster_1 is: "
#print final_sweet_element_done_1
#print "The elements selected with its degree centrality is: "
#print final_sweet_list_done_1

# printing the final lists for the done_2 are 

#print "The elements selected from the calculated cluster_2 is: "
#print final_sweet_element_done_2
#print "The elements selected with its degree centrality is: "
#print final_sweet_list_done_2

# printing the final lists for the done_3 are 

#print "The elements selected from the calculated cluster_3 is: "
#print final_sweet_element_done_3
#print "The elements selected with its degree centrality is: "
#print final_sweet_list_done_3

print ("Total time required is :: ")
print (time.clock() - start_time, "seconds")
#time.sleep(100)
    

        
    
        

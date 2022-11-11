#Name: Sahil Mahendra Mody
#Cwid: 20007262
#Assignment4


import csv
from gurobipy import*

node = open ('node.csv', 'r')
csv_node = csv.reader(node)

demand = {}
supply = {}

for row in csv_node:
    if 'd' in row [2]:
        demand[(row[0])] = float(row[1])
    if 's' in row [2]:
        supply[row[0]]= float (row[1])

print("Demand : ",demand)
print ("-"*100)
print("Supply : ",supply)
print ("-"*100)

link= open ('link.csv', 'r')
csv_link = csv.reader (link)

capacity = {}
for row1 in csv_link:
    capacity [(row1[0], row1[1])]= float (row1[2])
print("Capacity: ",capacity)
print ("-"*100)

dnode , d_value = multidict(demand)
print("Demand Nodes: ",dnode)
print ("-"*100)

snode , s_value = multidict(supply)
print("Supply Nodes: ",snode)
print ("-"*100)

link, mydict_links = multidict(capacity)
#print("Link capacity: ",link, end="")
#print ("-"*100)

model = Model ("minimum cost flow problem")

X = model.addVars(link,vtype=GRB.CONTINUOUS, lb = 0 , ub=GRB.INFINITY, name="x")
F = model.addVars(dnode,vtype=GRB.CONTINUOUS, lb = 0 , ub=GRB.INFINITY, name="f")

for i in snode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select(i,'*')) - quicksum(X[j,i] for j, i in link.select('*',i)) <= supply[(i)])

for j in dnode:
    model.addConstr(quicksum(X[i,j] for i, j in link.select('*',j)) - quicksum(X[j,i] for j, i in link.select(j,'*')) == F[j])
    
for i, j in link:
    model.addConstr (X[i,j] <= capacity[i,j]) 
    
for j in dnode:
    model.addConstr (F[j] <= demand[j]) 
    
Z = quicksum((demand[i]-F[i]) for i in dnode)/997

model.setObjective(Z,GRB.MINIMIZE)
model.update()
model.optimize()

model.printAttr ('x')

if model.status==GRB.OPTIMAL:
    print ("-"*100)
    print ("Optimal value: $",model.objVal)
    print ("-"*100)
    print ("--------- Quantity ----------")
    for i, j in link: 
        print ("Flow From",i, "To", j,"is --->", X[i,j].X)
        
        


import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph(name = 'Sample Network')
#print(G)
position= open ('position.csv', 'r')
csv_position = csv.reader (position)

for posi in csv_position:
    G.add_node(int(posi[0]),pos=(float(posi[1]),float(posi[2])))


nodeA=[]
nodeB=[]
for edges in capacity:
    [A,B]=edges
    G.add_edge(int(A),int(B))

print ("-"*100)
print("Graph Details: ",nx.info(G))
print ("-"*100)
print("Nodes are: ",G.nodes())
print ("-"*100)
print ("Edges are: ",G.edges())
print ("-"*100)

#label all nodes (e.g., node numbers: 1, 2, ...) 
#Display demand nodes as blue squares 
nx.draw(G,nx.get_node_attributes(G, "pos"), edge_color='black',node_shape='s',
        nodelist = [node for node in G.nodes() if int(node)<=15],
        width=2,node_size=400,node_color='blue', alpha=0.9,
        labels={node:node for node in G.nodes()})
#Display supply nodes as green circles 
nx.draw(G,nx.get_node_attributes(G, "pos"), edge_color='black',
        node_shape='o',nodelist = [node for node in G.nodes() if int(node)>15],
        width=2,node_size=500,node_color='green', alpha=0.9,
        labels={node:node for node in G.nodes()})

# Degree centrality
degree_central = nx.degree_centrality(G)
print("Degree Centrality: ", degree_central)
print ("-"*100)

sorted_degree_central = dict(sorted(degree_central.items(), key=lambda item: item[1], reverse=True))
print("Degree Centrality Sorted: ", sorted_degree_central)
print ("-"*100)


# Closeness centrality
closeness_central = nx.closeness_centrality(G)
print("Closeness Centrality: ", closeness_central)
print ("-"*100)

sorted_closeness_central = dict(sorted(closeness_central.items(), key=lambda item: item[1], reverse=True))
print("Closeness Centrality Sorted: ", sorted_closeness_central)
print ("-"*100)


# Betweeness centrality
betweeness_central = nx.betweenness_centrality(G)
print("Betweeness Centrality: ", betweeness_central)
print ("-"*100)
 
sorted_betweeness_central = dict(sorted(betweeness_central.items(), key=lambda item: item[1], reverse=True))
print("Betweeness Centrality Sorted:  ", sorted_betweeness_central)
print ("-"*100)


plt.show()


#Remove the first 5 nodes ranked based on degree centrality.

first_5 = list(sorted_degree_central.keys())[:5]
print("First 5 nodes ranked based on degree centrality: ",first_5)
print ("-"*100)


#Solve the model and find the optimum solution. Compare the results with respect to part (3) and make a discussion in 5 -10 sentences.   
node = open ('node.csv', 'r')
csv_node = csv.reader(node)
mydict_demand = {}
mydict_supply = {}


for row in csv_node:
    if 'd' in row [2]:
        if int(row[0]) not in first_5:
            mydict_demand[(row[0])] = float(row[1])
    if 's' in row [2]:
        mydict_supply[row[0]]= float (row[1])
        
#print(mydict_demand)      
capacity= open ('link.csv', 'r')
csv_capacity = csv.reader (capacity)
mydict_capacity = {}
for row in csv_capacity:
   if int(row[0]) not in first_5 and int(row[1]) not in first_5:
       mydict_capacity [(row [0], row[1])]= float (row[2])
    


dnode1, d_value1 = multidict(mydict_demand)
print("Demand Nodes after removing first 5 nodes: ",dnode1)
print ("-"*100)


snode1, supply_value = multidict(mydict_supply)
print("Supply Nodes after removing first 5 nodes: ",snode1)
print ("-"*100)


link1, mydict_links1 = multidict(mydict_capacity)
#print("Link capacity: ",link1,end="")
#print ("-"*100)




model = Model ("minimum cost flow problem")


X = model.addVars(link,vtype=GRB.CONTINUOUS, lb = 0 , ub=GRB.INFINITY, name="x")
F = model.addVars(dnode,vtype=GRB.CONTINUOUS, lb = 0 , ub=GRB.INFINITY, name="f")


for i in snode1:
    model.addConstr(quicksum(X[i,j] for i, j in link1.select(i,'*')) - quicksum(X[j,i] for j, i in link1.select('*',i)) <= mydict_supply[(i)])
    

for j in dnode1:
    model.addConstr(quicksum(X[i,j] for i, j in link1.select('*',j)) - quicksum(X[j,i] for j, i in link1.select(j,'*')) == F[j])
    
    

for i, j in link1:
    model.addConstr (X[i,j] <= mydict_capacity[i,j]) 
    
    

for j in dnode1:
    model.addConstr (F[j] <= mydict_demand[j]) 


Z = quicksum((mydict_demand[i]-F[i]) for i in dnode1)/997
model.setObjective(Z,GRB.MINIMIZE)
model.update()
model.optimize()


model.printAttr ('x') 

if model.status==GRB.OPTIMAL:
    print ("-"*100)
    print ("Optimal value: $",model.objVal)
    print ("-"*100)
    print ("--------------------- Quantity ---------------------------------")
    for i, j in link1: 
        print ("Flow From",i, "To", j,"is --->", X[i,j].X)
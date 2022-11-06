
# -------------------------------------------
# Transshipment  problems
# -------------------------------------------

# Define the model parameters 
# List containing suuply points 
print ("-"*100)
supply_p = ["Ohio", "Pennsylvania", "New York"] 
print ("Supply places: ", supply_p)
print ("-"*100)
# List containing transshipment points    
transshipment_p = ['Indiana', 'Georgia'] 
print ("Transshipment places: ", transshipment_p)
print ("-"*100)
# List containing demand points    
demand_p = ['Virginia', 'Kentucky', 'Louisiana']  
print ("Demand places: ", demand_p)
print ("-"*100)  
# Dictionary containing the tarnsportaion cost information between the points
cost = {
    (supply_p[0], transshipment_p[0]): 16,
    (supply_p[0], transshipment_p[1]): 21,
 
    (supply_p[1], transshipment_p[0]): 18,
    (supply_p[1], transshipment_p[1]): 16,
 
    (supply_p[2], transshipment_p[0]): 22,
    (supply_p[2], transshipment_p[1]): 25,
   
    (transshipment_p[0], demand_p[0]): 23,
    (transshipment_p[0], demand_p[1]): 15,
    (transshipment_p[0], demand_p[2]): 29,
    
    (transshipment_p[1], demand_p[0]): 20,
    (transshipment_p[1], demand_p[1]): 17,
    (transshipment_p[1], demand_p[2]): 24,
    
    }
print ("Transportation cost: ", cost)
print ("-"*100)

# Dictionary containing amount of supply at each origion point (supply point)
supply_v = {
    supply_p[0]: 72,
    supply_p[1]: 105,
    supply_p[2]: 83
    
    }
print ("Supply: ", supply_v)
print ("-"*100)
# Dictionary containing demand required at each destination point (demand point)
demand_v = {
    demand_p[0]: 90,
    demand_p[1]: 80,
    demand_p[2]: 120
    }

print ("Demand: ", demand_v)
print ("-"*100)
# Import gurobi
from gurobipy import *
# Create the model as an object
model = Model ("transshipment")
# Mute the Gurobi
model.setParam ('OutputFlag', False)
# Create the decison variables for each link from supply points to trashsipment 
#points
X = model.addVars(supply_p, transshipment_p, vtype=GRB.INTEGER, 
lb=0,ub=GRB.INFINITY, name="x")
# Create the decison variables for each link from trashsipment points to demand 
#points
Y = model.addVars(transshipment_p, demand_p, vtype=GRB.INTEGER, 
lb=0,ub=GRB.INFINITY, name="y")
# Supply constraints
for i in supply_p:
    model.addConstr(quicksum(X[i,j] for j in transshipment_p) == supply_v[i])
# Demand constraints
for j in demand_p:
    model.addConstr(quicksum(Y[i,j] for i in transshipment_p) <= demand_v[j])
# Transshipment constraints: Balance constraints
for i in transshipment_p:
    model.addConstr((quicksum(Y[i,j] for j in demand_p) - quicksum(X[k, i] for k in
supply_p) == 0))
# Define the objective function
Z = quicksum(X[i,j] * cost[i,j] for i in supply_p for j in transshipment_p)+ quicksum(Y[m,n] * cost[m,n] for m in transshipment_p for n in demand_p)
# Specify the type of the model: minimization or maximization
model.setObjective (Z, GRB.MINIMIZE)
# Update the model
model.update()
# Solve the model    
model.optimize()     
        
# Print out the optimal solutions: the decion variables values
model.printAttr ('x') 
# Print out the outputs
if model.status==GRB.OPTIMAL:
    print ("-"*100)
    print ("Optimal value: $",model.objVal)
    print ("-"*100)
    print ("-------------------------- Quantity (From - To) --------------------------")
    for i in supply_p: 
        for j in transshipment_p:
            print ("From",i, "To ", j,":", X[i,j].X,"$")
    for i in transshipment_p: 
        for j in demand_p:
            print ("From",i, "To ", j,":", Y[i,j].X,"$")
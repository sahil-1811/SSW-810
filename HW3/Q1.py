

# -------------------------------------------
# Transportation problems
# -------------------------------------------
# Define the model parameters 
# List containing each suuply point 
print ("-"*100)
supply_p = ['W1','W2'] 
print ("Supply points: ", supply_p)
print ("-"*100)
# List containing each demand point    
demand_p = ['Retailer 1', 'Retailer 2', 'Retailer 3','Retailer 4','Retailer 5']    
print ("Demand points: ", demand_p)
print ("-"*100)
# Dictionary containing tarnsportaion cost information from every origin (supply 
#point) to each destination (demand point)
cost = {
    (supply_p[0], demand_p[0]): 2,
    (supply_p[0], demand_p[1]): 4,
    (supply_p[0], demand_p[2]): 5,
    (supply_p[0], demand_p[3]): 2,
    (supply_p[0], demand_p[4]): 1,
    (supply_p[1], demand_p[0]): 3,
    (supply_p[1], demand_p[1]): 1,
    (supply_p[1], demand_p[2]): 3,
    (supply_p[1], demand_p[3]): 2,
    (supply_p[1], demand_p[4]): 3
    }

print ("Transportation cost: ", cost)

print ("-"*100)
# Dictionary containing amount of supply at each origion point (supply point)
supply_v = {
    supply_p[0]: 2000,
    supply_p[1]: 3000,
    }
print ("Supply: ", supply_v)
print ("-"*100)
# Dictionary containing demand required at each destination point (demand point)
demand_v = {
    demand_p[0]: 500,
    demand_p[1]: 800,
    demand_p[2]: 1800,
    demand_p[3]: 300,
    demand_p[4]: 700
    }
print ("Demand: ", demand_v)




from gurobipy import *

# Create the model as an object
model = Model ("transportation")

# Mute the Gurobi
model.setParam ('OutputFlag', False) 

# Create the decison variables for each link
#X = model.addVars(supply_p, demand_p, vtype=GRB.INTEGER, lb=0,ub=GRB.INFINITY, name="x")
X = {}
for s in supply_p:
    for d in demand_p:
        X[s,d] = model.addVar(obj=cost[s,d], name='flow_%s_%s' % (s, d))


# Supply constraints
for s in supply_p:
    model.addConstr(quicksum(X[s,d] for d in demand_p) <= supply_v[s])
# Demand constraints
for d in demand_p:
    model.addConstr(quicksum(X[s,d] for s in supply_p) == demand_v[d])

# Define the objective function
Z = quicksum(X[s,d] * cost[s,d] for s in supply_p for d in demand_p)

# Specify the type of the model: minimization or maximization
model.setObjective (Z, GRB.MINIMIZE)
# Update the model
model.update()
# Solve the model    
model.optimize()  

model.printAttr ('X')      

if model.status==GRB.OPTIMAL:
    print ("-"*100)
    print ("Optimal value: $",model.objVal)
    print ("-"*100)
    print ("-------------- Quantity (origin to destination)--------------------")
    for i in supply_p: 
        for j in demand_p:
            print ("From",i, "To ", j,":" ,X[i,j].X,"$")

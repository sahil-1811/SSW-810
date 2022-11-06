# -------------------------------------------
# Assignment problems
# -------------------------------------------

# Import gurobi
from gurobipy import *
print("-"*100)
# Define the model parameters 
# List containing officials
caterer = ["AI's", 'Bon Apetit', 'Custom', 'Divine','Epicurean',"Fouchess","University"] 
print ("Caterers: ", caterer )
print("-"*100)
# List containing game sites    
event_name = ['Alumni Brunch', 'Parents Brunch', 'Booster Club Lunch', 'Postgame Party',"Lettermen's Dinner","Contributors' Dinner"]  
print ("Events: ", event_name)
print("-"*100)
# Dictionary containing distance information from every official to each game site
events = {
    (caterer[0], event_name[0]): 12.6,
    (caterer[0], event_name[1]): 10.3,
    (caterer[0], event_name[2]): 14.0,
    (caterer[0], event_name[3]): 19.5,
    (caterer[0], event_name[4]): 25.0,
    (caterer[0], event_name[5]): 30.0,
    
    (caterer[1], event_name[0]): 14.5,
    (caterer[1], event_name[1]): 13.0,
    (caterer[1], event_name[2]): 16.5,
    (caterer[1], event_name[3]): 17.0,
    (caterer[1], event_name[4]): 22.5,
    (caterer[1], event_name[5]): 32.0,
    
    (caterer[2], event_name[0]): 13.0,
    (caterer[2], event_name[1]): 14.0,
    (caterer[2], event_name[2]): 17.6,
    (caterer[2], event_name[3]): 21.5,
    (caterer[2], event_name[4]): 23.0,
    (caterer[2], event_name[5]): 35.0,
    
    (caterer[3], event_name[0]): 11.5,
    (caterer[3], event_name[1]): 12.6,
    (caterer[3], event_name[2]): 13.0,
    (caterer[3], event_name[3]): 18.7,
    (caterer[3], event_name[4]): 26.2,
    (caterer[3], event_name[5]): 33.5,
    
    (caterer[4], event_name[0]): 10.8,
    (caterer[4], event_name[1]): 11.9,
    (caterer[4], event_name[2]): 12.9,
    (caterer[4], event_name[3]): 17.5,
    (caterer[4], event_name[4]): 21.9,
    (caterer[4], event_name[5]): 28.5,
    
    (caterer[5], event_name[0]): 13.5,
    (caterer[5], event_name[1]): 13.5,
    (caterer[5], event_name[2]): 15.5,
    (caterer[5], event_name[3]): 22.3,
    (caterer[5], event_name[4]): 24.5,
    (caterer[5], event_name[5]): 36.0,
    
    (caterer[6], event_name[0]): 12.5,
    (caterer[6], event_name[1]): 14.3,
    (caterer[6], event_name[2]): 16.0,
    (caterer[6], event_name[3]): 22.0,
    (caterer[6], event_name[4]): 26.7,
    (caterer[6], event_name[5]): 34.0,
    }


print("Events: ",events)
print("-"*100)

# Create the model as an object
model = Model ("Assignment")
# Mute the Gurobi
model.setParam ('OutputFlag', False)
# Create the decison variables for each link from every official to every game site
X = model.addVars(caterer, event_name, vtype=GRB.BINARY, name="x")
# Supply constraints (each official should be assigned to ecah game site)
# Supply of each official is limited to one unit
for c in caterer:
    if c=="Bon Apetit" or c=="Custom" or c=="University":
        model.addConstr(quicksum(X[c,e] for e in event_name) <= 2)
    else:
        model.addConstr(quicksum(X[c,e] for e in event_name) <= 1)
# Demand constraints (each game site sould be assignmed to each official)
# Demand of ecah game site is limited to one unit
for e in event_name:
    model.addConstr(quicksum(X[c,e] for c in caterer) == 1)
        

 
        
# Define the objective function
Z = quicksum(X[c,e] * events[c,e] for c in caterer for e in event_name)
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
    print("-"*100)
    print ("Optimal value:",model.objVal, "dollars")
    print("-"*100)
    for i in caterer: 
        for j in event_name:
            print ("Caterer",i, "is assigned to event: ", j, X[i,j].X)

import gurobipy as gp

#################
### Example 1 ###
#################

Model = gp.Model()

x1 = m.addVar()
x2 = m.addVar()
x3 = m.addVar()

m.setObjective

# Função Objeto
m.setObjective(12*x1 + 18*x2 + 22*x3, sense=gp.GRB.Maximize)

# Restrições
y1 = m.addConstr(1.5*x1 + 1.2*x3 <= 120)
y2 = m.addConstr(2.2*x1 + 1.4*x3 <= 200)
y3 = m.addConstr(1.2*x1 + 2.0*x2 + 2.4*x3 <= 250)

m.optimize

# Combinação ideal de cada variável

#################
### Example 2 ###
#################
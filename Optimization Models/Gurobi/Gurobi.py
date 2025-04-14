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

# Combinação ideal de produtos
print("Produto A:", x1.X)
print("Produto B:", x2.X)
print("Produto C:", x3.X)

# Tempo de uso da máquina ideal de produtos
tempo_m1 = 120 - c1.Slack
tempo_m2 = 200 - c2.Slack
tempo_m3 = 250 - c3.Slack

print("Máquina_1", tempo_m1)
print("Máquina_2", tempo_m2)
print("Máquina_3", tempo_m3)

#################
### Example 2 ###
#################
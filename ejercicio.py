import json

datos = json.load(open("datos.json"))

# TechNova fue fundada en 2005
print(f"{datos["empresa"]} fue fundada en {datos["fundacion"]}")

# La sede principal esta en Barcelona
print(f"La sede principal esta en {datos["sede"]}")

# TechNova tiene 4 empleados
print (f"{datos["empresa"]} tiene {len(datos["empleados"])} empleados")

# Empleados de TechNova -> Laura, Carlos, Andrea, David (con sus apellidos y separados con saltos de linea)
print(f"Empleados de {datos["empresa"]}:")
for empleado in datos ["empleados"]:
    print(empleado)

# TechNova tiene 3 productos en su catálogo
print(f"{datos["empresa"]} tiene {len(datos["productos"])} productos en su catálogo")

# Productos de TechNova a 149.50 euros
print(f"Productos de {datos["empresa"]} a {datos["productos"][1]["precio"]} euros")

# TechNova cotiza en Bolsa
if({datos["cotiza"]} == True):
    print(f"{datos["empresa"]} cotiza en bolsa")

# TechNova tiene sedes en 3 cuidades
print(f"{datos["empresa"]} tiene sedes en {len(datos["sedes"])} cuidades")

# La sede más reciente fundada en 2005 de TechNova esta en Paris
print(f"La sede más reciente fundada en {datos["fundacion"]} de {datos["empresa"]} esta en {datos["sedes"][2]}")
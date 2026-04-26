from pulp import LpProblem, LpMinimize, LpVariable, lpSum, value, PULP_CBC_CMD

def resolver_optimizacion(area_techo, consumo_mensual, horas_sol):
    # Crear el problema de minimización
    prob = LpProblem("Minimizar_Inversion", LpMinimize)

    # Variables de decisión (Enteras, ya que no se pueden comprar fracciones de paneles)
    x = LpVariable("Panel_A", lowBound=0, cat='Integer')
    y = LpVariable("Panel_B", lowBound=0, cat='Integer')
    z = LpVariable("Panel_C", lowBound=0, cat='Integer')

    # Función Objetivo: Minimizar la inversión (Costos del PDF)
    prob += 190*x + 205*y + 255*z

    # Restricción 1: Satisfacer el consumo de energía
    # Energía por mes = Potencia(kW) * HorasSol/día * 30 días/mes
    # Basado en cálculos del PDF: A=54, B=60.75, C=74.25 (para 4.5h sol)
    rend_a = 0.40 * horas_sol * 30
    rend_b = 0.45 * horas_sol * 30
    rend_c = 0.55 * horas_sol * 30
    prob += rend_a*x + rend_b*y + rend_c*z >= consumo_mensual

    # Restricción 2: No exceder el límite del techo (Áreas del PDF)
    prob += 1.9*x + 2.1*y + 2.5*z <= area_techo

    # Resolver el modelo
    prob.solve(PULP_CBC_CMD(msg=0))

    return {
        "status": "Optimal" if prob.status == 1 else "No Solution",
        "x": value(x),
        "y": value(y),
        "z": value(z),
        "costo": value(prob.objective),
        "area_usada": 1.9*value(x) + 2.1*value(y) + 2.5*value(z),
        "total_paneles": value(x) + value(y) + value(z)
    }

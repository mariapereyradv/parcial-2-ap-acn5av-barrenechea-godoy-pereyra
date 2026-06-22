# Módulo: Validación de Consumidores
# Proyecto: Estoy Bien. – Chamana
# Sprint 2 – Milestone M2

respuestas = [
    {"consumidor": "C01", "variedad_preferida": "Modo Avión", "puntaje": 9},
    {"consumidor": "C02", "variedad_preferida": "Touch Grass", "puntaje": 8},
    {"consumidor": "C03", "variedad_preferida": "No Sé, Llora", "puntaje": 10},
]

def analizar_feedback():
    total = sum(r["puntaje"] for r in respuestas)
    promedio = total / len(respuestas)

    print(f"Respuestas relevadas: {len(respuestas)}")
    print(f"Puntaje promedio: {promedio:.1f} / 10")

analizar_feedback()
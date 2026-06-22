# Módulo: Gestión de Variedades
# Proyecto: Estoy Bien. – Chamana
# Sprint 1 – Milestone M1

variedades = [
    {
        "nombre": "Modo Avión",
        "emocion": "Ansiedad y overthinking",
        "ingredientes": ["Manzanilla", "Lavanda", "Melisa", "Lúpulo"]
    },
    {
        "nombre": "Touch Grass",
        "emocion": "Cansancio y falta de energía",
        "ingredientes": ["Jengibre", "Menta", "Romero", "Guaraná suave"]
    },
    {
        "nombre": "No Sé, Llora",
        "emocion": "Tristeza y nostalgia",
        "ingredientes": ["Rosa mosqueta", "Hibisco", "Frutos rojos", "Canela"]
    }
]

def listar_variedades():
    for v in variedades:
        print(f"Variedad: {v['nombre']} | Emoción: {v['emocion']}")
        print(f"Ingredientes: {', '.join(v['ingredientes'])}")
        print("---")

listar_variedades()
# Módulo: Lanzamiento al Mercado
# Proyecto: Estoy Bien. – Chamana
# Sprint 3 – Milestone M3

metricas = {
    "unidades_vendidas": 500,
    "nuevos_seguidores": 200,
    "resenas_recibidas": 10,
    "canal_activo": "Instagram + Tienda Online"
}

def mostrar_metricas():
    print("=== Métricas de Lanzamiento ===")

    for clave, valor in metricas.items():
        print(f"{clave.replace('_', ' ').title()}: {valor}")

mostrar_metricas()
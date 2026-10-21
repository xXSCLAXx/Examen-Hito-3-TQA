"""Verifica los resultados esperados y la cobertura de los casos de caja blanca.

Uso:  python verificar_cobertura.py
"""
from validar_compra import validar_compra

# (edad, cuenta_activa, saldo, monto, resultado_esperado)
CASOS = {
    "3 casos (examen)": [
        (17, True, 100, 50, "Compra no permitida: edad"),
        (25, False, 100, 50, "Compra no permitida: cuenta"),
        (25, True, 100, 50, "Compra aprobada"),
    ],
    "4 casos (ajuste: sentencias y decisiones)": [
        (17, True, 100, 50, "Compra no permitida: edad"),
        (25, False, 100, 50, "Compra no permitida: cuenta"),
        (25, True, 100, 50, "Compra aprobada"),
        (25, True, 10, 50, "Compra rechazada"),
    ],
    "5 casos (ajuste: condiciones)": [
        (17, True, 100, 50, "Compra no permitida: edad"),
        (25, False, 100, 50, "Compra no permitida: cuenta"),
        (25, True, 100, 50, "Compra aprobada"),
        (25, True, 10, 50, "Compra rechazada"),
        (25, True, 100, 0, "Compra rechazada"),
    ],
}


def evaluar(casos):
    ok = all(validar_compra(*c[:4]) == c[4] for c in casos)
    sentencias = {validar_compra(*c[:4]) for c in casos}
    # Se replica la evaluación de Python (cortocircuito) para registrar qué condiciones se evalúan.
    d1, d2, d3 = set(), set(), set()
    c1, c2, c3, c4 = set(), set(), set(), set()
    for edad, activa, saldo, monto, _ in casos:
        v = edad < 18
        d1.add(v); c1.add(v)
        if v:
            continue
        v = not activa
        d2.add(v); c2.add(v)
        if v:
            continue
        a = saldo >= monto
        c3.add(a)
        if a:
            c4.add(monto > 0)
        d3.add(a and monto > 0)
    return ok, len(sentencias), d1, d2, d3, c1, c2, c3, c4


if __name__ == "__main__":
    for nombre, casos in CASOS.items():
        ok, s, d1, d2, d3, c1, c2, c3, c4 = evaluar(casos)
        full = {True, False}
        dec = all(x == full for x in (d1, d2, d3))
        con = all(x == full for x in (c1, c2, c3, c4))
        print(f"{nombre}: resultados esperados OK={ok}")
        print(f"  Sentencias (return) cubiertas: {s}/4 -> {'COMPLETA' if s == 4 else 'incompleta'}")
        print(f"  Decisiones D1/D2/D3 con V y F: {dec} -> {'COMPLETA' if dec else 'incompleta'}")
        print(f"  Condiciones C1..C4 con V y F : {con} -> {'COMPLETA' if con else 'incompleta'}")
        print()

# Análisis de caja blanca — `validar_compra`

## 1. Código analizado
```python
def validar_compra(edad, cuenta_activa, saldo, monto):
    if edad < 18:                               # D1
        return "Compra no permitida: edad"      # S1

    if not cuenta_activa:                       # D2
        return "Compra no permitida: cuenta"    # S2

    if saldo >= monto and monto > 0:            # D3
        return "Compra aprobada"                # S3

    return "Compra rechazada"                   # S4
```

## 2. Decisiones y condiciones simples

| Decisión | Expresión | Condiciones simples |
|---|---|---|
| D1 | `edad < 18` | C1: `edad < 18` |
| D2 | `not cuenta_activa` | C2: `not cuenta_activa` |
| D3 | `saldo >= monto and monto > 0` | C3: `saldo >= monto` · C4: `monto > 0` |

- **3 decisiones** (D1, D2, D3) y **4 condiciones simples** (C1 a C4).
- **4 sentencias de retorno** (S1 a S4), una por cada salida posible.

## 3. Criterio utilizado
Criterio principal: **cobertura de decisiones** (cada decisión debe tomar el resultado verdadero y el falso).
Se comparan también sentencias y condiciones para mostrar la diferencia entre ellos.

## 4. Mínimo de casos y cálculo

Cada ejecución de la función termina en **un solo** `return`, y existen 4 `return` distintos. Por lo tanto, ningún caso de prueba puede cubrir dos sentencias de retorno a la vez.

| Criterio | Qué hay que cubrir | Mínimo | Cálculo |
|---|---|---|---|
| Sentencias | S1, S2, S3, S4 | **4** | 4 `return` mutuamente excluyentes, 1 caso por `return` |
| Decisiones | D1 (V/F), D2 (V/F), D3 (V/F) | **4** | D1=V corta el flujo (caso A). D2=V (caso B). D3=V (caso C). D3=F (caso D). Los casos que dan F en D1 y D2 son los mismos B, C y D, y no hacen falta casos extra |
| Condiciones | C1, C2, C3, C4 con V y F | **5** | En Python `and` hace cortocircuito: C4 solo se evalúa si C3 es verdadera. Para C3=F se necesita un caso (D) y para C4=F otro distinto (E), porque ambos no pueden darse a la vez |

> Cobertura de decisiones **no es** lo mismo que cobertura de condiciones: D3 completa solo necesita que `saldo >= monto and monto > 0` sea V y F, pero no obliga a que `monto > 0` sea F.

## 5. Los 3 casos diseñados (pedidos por el examen)

| Caso | edad | cuenta_activa | saldo | monto | Resultado esperado | Cubre |
|---|---|---|---|---|---|---|
| CB-01 | 17 | True | 100 | 50 | `Compra no permitida: edad` | S1 · D1=V · C1=V |
| CB-02 | 25 | False | 100 | 50 | `Compra no permitida: cuenta` | S2 · D1=F · D2=V · C1=F · C2=V |
| CB-03 | 25 | True | 100 | 50 | `Compra aprobada` | S3 · D2=F · D3=V · C2=F · C3=V · C4=V |

## 6. ¿Alcanzan los 3 casos?
**No.** Resultado de aplicar los 3 casos (verificado con `codigo/verificar_cobertura.py`):

| Criterio | Cubierto | Pendiente |
|---|---|---|
| Sentencias | 3/4 | S4 (`Compra rechazada`) |
| Decisiones | D1 V/F, D2 V/F | D3=F |
| Condiciones | C1 V/F, C2 V/F | C3=F y C4=F |

### Ajuste necesario

| Caso agregado | edad | cuenta_activa | saldo | monto | Resultado esperado | Cubre | Criterio que completa |
|---|---|---|---|---|---|---|---|
| CB-04 | 25 | True | 10 | 50 | `Compra rechazada` | S4 · D3=F · C3=F | Sentencias y decisiones (4 casos) |
| CB-05 | 25 | True | 100 | 0 | `Compra rechazada` | S4 · D3=F · C3=V · C4=F | Condiciones (5 casos) |

## 7. Matriz de justificación final

| Resultado a cubrir | Caso que lo cubre |
|---|---|
| D1 = Verdadero | CB-01 |
| D1 = Falso | CB-02, CB-03, CB-04, CB-05 |
| D2 = Verdadero | CB-02 |
| D2 = Falso | CB-03, CB-04, CB-05 |
| D3 = Verdadero | CB-03 |
| D3 = Falso | CB-04, CB-05 |
| C1 V / F | CB-01 / CB-02 |
| C2 V / F | CB-02 / CB-03 |
| C3 V / F | CB-03 / CB-04 |
| C4 V / F | CB-03 / CB-05 |

## 8. Conclusión
Con 3 casos se cubren 3 de 4 sentencias, pero no se alcanza ningún criterio completo. Con **4 casos** (CB-01 a CB-04) se logra cobertura de sentencias y de decisiones. Con **5 casos** (CB-01 a CB-05) se logra además cobertura de condiciones.

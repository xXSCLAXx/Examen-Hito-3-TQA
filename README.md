# Examen Práctico Hito 3 — Testing & Quality Assurance

**Universidad Privada Franz Tamayo (Unifranz)** · Carrera de Ingeniería en Sistemas · Séptimo semestre
**Materia:** Testing, Quality Assurance · **Docente:** Ing. Reynel Sanchez Chuquimia
**Estudiante:** Sebastián Ariel Camacho Loayza · La Paz, Bolivia · 2026

## Propósito
Aplicar técnicas de caja negra y caja blanca, redactar escenarios Gherkin, documentar bugs y organizar el trabajo con Git y GitHub.

## Aplicación probada
SauceDemo (Swag Labs): https://www.saucedemo.com/ · Pruebas ejecutadas el 20/10/2026 en Google Chrome 155 sobre Windows.

## Resumen de resultados

| Actividad | Resultado |
|---|---|
| Caja negra | 7 casos ejecutados (5 solicitados + 2 adicionales): 4 Passed y 3 Failed |
| Bugs | 6 defectos reproducibles con evidencia |
| Caja blanca | Los 3 casos no alcanzan la cobertura; se necesitan 4 (sentencias y decisiones) o 5 (condiciones) |
| Gherkin | 6 escenarios en 2 features (login y carrito/checkout) |

### Casos de caja negra

| ID | Caso | Estado | Defecto |
|---|---|---|---|
| TC-001 | Inicio de sesión con credenciales válidas | PASS | — |
| TC-002 | Inicio de sesión con contraseña incorrecta | FAIL | BUG-01-UI |
| TC-003 | Agregar productos al carrito | PASS | — |
| TC-004 | Eliminar un producto del carrito | PASS | — |
| TC-005 | Validación de campos obligatorios en el checkout | PASS | — |
| TC-006 | Gestión del carrito desde el catálogo con problem_user (adicional) | FAIL | BUG-02-UI, BUG-03-F, BUG-04-F, BUG-06-F |
| TC-007 | Checkout con datos válidos con problem_user (adicional) | FAIL | BUG-05-F |

### Bugs

| ID | Título | Severidad |
|---|---|---|
| BUG-01-UI | El mensaje de error del login se muestra cortado | Baja |
| BUG-02-UI | Todos los productos muestran la misma imagen con problem_user | Media |
| BUG-03-F | El botón Add to cart no responde en 3 de 6 productos con problem_user | Alta |
| BUG-04-F | El botón Remove del catálogo no responde con problem_user | Media |
| BUG-05-F | El campo Last Name sobrescribe First Name en el checkout con problem_user | Crítica |
| BUG-06-F | El carrito conserva productos al cerrar sesión y cambiar de usuario | Media |

## Estructura del repositorio
```
Examen-Hito-3-TQA/
├── README.md
├── codigo/                     # Función analizada y script de verificación de cobertura
├── docs/
│   ├── casos_caja_negra.md     # Casos en Markdown
│   ├── casos_caja_negra.docx   # Casos con la plantilla de la materia
│   ├── analisis_caja_blanca.md
│   └── escenarios_gherkin.md
├── bugs/
│   ├── bugs_encontrados.md
│   └── bugs_encontrados.docx   # Bugs con la plantilla de la materia
├── evidencias/capturas/        # Capturas de la ejecución
└── entregable/
    └── informe_hito3.pdf       # Informe final consolidado
```

## Cómo verificar la caja blanca
```
cd codigo
python verificar_cobertura.py
```

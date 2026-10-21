# Casos de caja negra — SauceDemo

Aplicación: https://www.saucedemo.com/ · Fecha de ejecución: 20/10/2026 · Tester: Sebastián Ariel Camacho Loayza

Plantilla: *Casos de prueba, plantilla para diseño y ejecución* (TQA). Versión con la plantilla original en `casos_caja_negra.docx`.
PASS = coincide; FAIL = diferencia verificable. TC-006 y TC-007 son casos adicionales a los 5 solicitados.

| ID | Caso | Estado | Defecto |
|---|---|---|---|
| TC-001 | Inicio de sesión con credenciales válidas | PASS | — |
| TC-002 | Inicio de sesión con contraseña incorrecta | FAIL | BUG-01-UI |
| TC-003 | Agregar productos al carrito | PASS | — |
| TC-004 | Eliminar un producto del carrito | PASS | — |
| TC-005 | Validación de campos obligatorios en el checkout | PASS | — |
| TC-006 | Gestión del carrito desde el catálogo con problem_user (adicional) | FAIL | BUG-02-UI, BUG-03-F, BUG-04-F, BUG-06-F |
| TC-007 | Checkout con datos válidos con problem_user (adicional) | FAIL | BUG-05-F |

---

## TC-001 · Inicio de sesión con credenciales válidas

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-001 | Inicio de sesión con credenciales válidas | Alta | Funcional (positiva) | Inicio de sesión | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que un usuario con credenciales válidas pueda iniciar sesión y acceder al catálogo de productos.

**2. Precondiciones**

| Estado inicial | Navegador abierto en https://www.saucedemo.com/ con la sesión cerrada y los campos vacíos. |
|---|---|
| Usuario / permisos | Usuario estándar de demostración, sin permisos especiales. |
| Configuración | Google Chrome 155 en Windows, con conexión a internet. |

**3. Datos de prueba**

| Dato | Usuario / Contraseña |
|---|---|
| Valor | standard_user / secret_sauce |
| Origen | Usuarios de demostración publicados en la página de login |
| Observación | Usuario sin fallos intencionales del sitio. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Abrir la URL de la aplicación | https://www.saucedemo.com/ | Se muestra el formulario de login con Username, Password y el botón Login. |
| 2 | Escribir el usuario en el campo Username | standard_user | El campo muestra el texto ingresado. |
| 3 | Escribir la contraseña en el campo Password | secret_sauce | El campo muestra la contraseña enmascarada. |
| 4 | Hacer clic en el botón Login | — | Se redirige a /inventory.html y se muestra el título Products con los productos. |

**5. Resultado esperado final (criterio de éxito)**: Se accede a la página de productos sin mensajes de error.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-001 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:15 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **PASS**

**2. Resultado observado**: Con standard_user y secret_sauce, el sitio redirigió a /inventory.html. Se mostró el título Products con 6 productos, cada uno con su precio y el botón Add to cart.

**Comparación**: Coincide con lo esperado. No hubo diferencias.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Abrir la URL | Formulario de login visible | PASS | Ver captura 00. |
| 2 | Escribir usuario | Texto visible en Username | PASS | — |
| 3 | Escribir contraseña | Texto enmascarado | PASS | — |
| 4 | Clic en Login | Se abrió /inventory.html (Products) | PASS | Ver captura 01. |

**4. Evidencia**

- `evidencia_TC001_00_login_inicial.png`: Pantalla de login antes de ingresar credenciales, con la lista de usuarios de demostración.

  ![Pantalla de login antes de ingresar credenciales, con la lista de usuarios de demostración.](../evidencias/capturas/evidencia_TC001_00_login_inicial.png)

- `evidencia_TC001_01_pagina_productos.png`: Página de productos (/inventory.html) tras iniciar sesión con standard_user.

  ![Página de productos (/inventory.html) tras iniciar sesión con standard_user.](../evidencias/capturas/evidencia_TC001_01_pagina_productos.png)

**5. Si el resultado es FAIL**: N/A. El resultado fue PASS. Referencia del defecto: N/A

**6. Observaciones de ejecución**: Ninguna.


---

## TC-002 · Inicio de sesión con contraseña incorrecta

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-002 | Inicio de sesión con contraseña incorrecta | Alta | Negativa | Inicio de sesión | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que el sistema rechace el acceso con una contraseña incorrecta y muestre un mensaje de error completo y legible.

**2. Precondiciones**

| Estado inicial | Navegador abierto en https://www.saucedemo.com/ con la sesión cerrada y los campos vacíos. |
|---|---|
| Usuario / permisos | Usuario estándar de demostración, sin permisos especiales. |
| Configuración | Google Chrome 155 en Windows, con conexión a internet. |

**3. Datos de prueba**

| Dato | Usuario / Contraseña |
|---|---|
| Valor | standard_user / clave_incorrecta |
| Origen | Usuario de demostración y contraseña inventada |
| Observación | La contraseña es inválida a propósito. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Abrir la URL de la aplicación | https://www.saucedemo.com/ | Se muestra el formulario de login. |
| 2 | Escribir el usuario en el campo Username | standard_user | El campo muestra el texto ingresado. |
| 3 | Escribir la contraseña inválida en Password | clave_incorrecta | El campo muestra la contraseña enmascarada. |
| 4 | Hacer clic en el botón Login | — | Permanece en el login, los campos se marcan en rojo y el mensaje “Epic sadface: Username and password do not match any user in this service” se ve completo y legible. |

**5. Resultado esperado final (criterio de éxito)**: Se bloquea el acceso y el mensaje de error se muestra completo y legible.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-002 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:13 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **FAIL**

**2. Resultado observado**: El acceso fue rechazado y el sitio permaneció en el login. Los campos se marcaron en rojo y se mostró el texto correcto del mensaje, pero el cuadro rojo lo recorta: se cortan el borde superior de “Epic sadface” y el inferior de “this service”. Se repitió a las 21:16 con el mismo resultado.

**Comparación**: No coincide por completo. La lógica es correcta (acceso rechazado y mensaje correcto), pero el mensaje no es totalmente legible porque aparece recortado.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Abrir la URL | Formulario de login visible | PASS | — |
| 2 | Escribir usuario | Texto visible en Username | PASS | — |
| 3 | Escribir contraseña inválida | Texto enmascarado | PASS | Ver captura 01. |
| 4 | Clic en Login | Acceso rechazado; mensaje con texto cortado arriba y abajo | FAIL | Ver capturas 02 y 03. Reproducido 2 veces. |

**4. Evidencia**

- `evidencia_TC002_01_datos_ingresados.png`: Formulario con el usuario y la contraseña inválida ingresados.

  ![Formulario con el usuario y la contraseña inválida ingresados.](../evidencias/capturas/evidencia_TC002_01_datos_ingresados.png)

- `evidencia_TC002_02_mensaje_error.png`: Mensaje de error tras presionar Login, con el texto recortado.

  ![Mensaje de error tras presionar Login, con el texto recortado.](../evidencias/capturas/evidencia_TC002_02_mensaje_error.png)

- `evidencia_BUG01_01_zoom_mensaje_truncado.png`: Ampliación del mensaje de error que muestra el recorte (repetición a las 21:16).

  ![Ampliación del mensaje de error que muestra el recorte (repetición a las 21:16).](../evidencias/capturas/evidencia_BUG01_01_zoom_mensaje_truncado.png)

**5. Si el resultado es FAIL**: El mensaje de error aparece recortado en los bordes superior e inferior del cuadro rojo; el texto no es completamente legible. Referencia del defecto: BUG-01-UI

**6. Observaciones de ejecución**: El texto completo sí está presente en la página. El recorte es solo visual.


---

## TC-003 · Agregar productos al carrito

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-003 | Agregar productos al carrito | Alta | Funcional (positiva) | Catálogo y carrito | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que al agregar productos desde el catálogo se actualicen el botón del producto, el contador del carrito y el contenido del carrito.

**2. Precondiciones**

| Estado inicial | Sesión iniciada con standard_user en /inventory.html y carrito vacío (ícono sin contador). |
|---|---|
| Usuario / permisos | Usuario estándar de demostración (standard_user). |
| Configuración | Google Chrome 155 en Windows. Ordenamiento por defecto: Name (A to Z). |

**3. Datos de prueba**

| Dato | Productos |
|---|---|
| Valor | Sauce Labs Backpack ($29.99) y Sauce Labs Bike Light ($9.99), cantidad 1 de cada uno |
| Origen | Catálogo de SauceDemo |
| Observación | Se agregan desde el catálogo, no desde el detalle del producto. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Hacer clic en Add to cart del producto Sauce Labs Backpack | Sauce Labs Backpack | El botón cambia a Remove y el contador del carrito muestra 1. |
| 2 | Hacer clic en Add to cart del producto Sauce Labs Bike Light | Sauce Labs Bike Light | El botón cambia a Remove y el contador del carrito muestra 2. |
| 3 | Hacer clic en el ícono del carrito | — | Se abre /cart.html con ambos productos, cantidad 1 y precios $29.99 y $9.99. |

**5. Resultado esperado final (criterio de éxito)**: El contador muestra 2 y el carrito lista exactamente los 2 productos seleccionados.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-003 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:15 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **PASS**

**2. Resultado observado**: Tras cada clic, el botón cambió a Remove y el contador pasó de 1 a 2. El carrito mostró Sauce Labs Backpack ($29.99) y Sauce Labs Bike Light ($9.99), con cantidad 1 cada uno.

**Comparación**: Coincide con lo esperado. No hubo diferencias.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Add to cart en Backpack | Botón Remove, contador 1 | PASS | Ver captura 01. |
| 2 | Add to cart en Bike Light | Botón Remove, contador 2 | PASS | Ver captura 02. |
| 3 | Abrir el carrito | Dos productos con cantidad 1 y sus precios | PASS | Ver captura 03. |

**4. Evidencia**

- `evidencia_TC003_01_un_producto.png`: Catálogo con Backpack agregado: botón Remove y contador 1.

  ![Catálogo con Backpack agregado: botón Remove y contador 1.](../evidencias/capturas/evidencia_TC003_01_un_producto.png)

- `evidencia_TC003_02_dos_productos.png`: Catálogo con Backpack y Bike Light agregados: contador 2.

  ![Catálogo con Backpack y Bike Light agregados: contador 2.](../evidencias/capturas/evidencia_TC003_02_dos_productos.png)

- `evidencia_TC003_03_carrito.png`: Carrito con los dos productos, cantidad 1 y precios correctos.

  ![Carrito con los dos productos, cantidad 1 y precios correctos.](../evidencias/capturas/evidencia_TC003_03_carrito.png)

**5. Si el resultado es FAIL**: N/A. El resultado fue PASS. Referencia del defecto: N/A

**6. Observaciones de ejecución**: Ninguna.


---

## TC-004 · Eliminar un producto del carrito

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-004 | Eliminar un producto del carrito | Media | Funcional (positiva) | Carrito | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que al eliminar un producto desde el carrito este desaparezca de la lista y el contador se actualice.

**2. Precondiciones**

| Estado inicial | Sesión iniciada con standard_user. Carrito con Sauce Labs Backpack y Sauce Labs Bike Light, en /cart.html. |
|---|---|
| Usuario / permisos | Usuario estándar de demostración (standard_user). |
| Configuración | Google Chrome 155 en Windows. |

**3. Datos de prueba**

| Dato | Producto a eliminar |
|---|---|
| Valor | Sauce Labs Bike Light |
| Origen | Producto agregado en TC-003 |
| Observación | El Backpack debe permanecer en el carrito. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Verificar el contenido del carrito | — | Se listan 2 productos y el contador muestra 2. |
| 2 | Hacer clic en Remove del producto Sauce Labs Bike Light | Sauce Labs Bike Light | El producto desaparece de la lista, el contador muestra 1 y el Backpack permanece. |

**5. Resultado esperado final (criterio de éxito)**: El carrito conserva solo el Backpack y el contador muestra 1.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-004 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:15 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **PASS**

**2. Resultado observado**: Al hacer clic en Remove, el Bike Light desapareció del listado. El carrito quedó con Sauce Labs Backpack y el contador cambió a 1.

**Comparación**: Coincide con lo esperado. No hubo diferencias.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Verificar el carrito | 2 productos, contador 2 | PASS | Ver captura 01. |
| 2 | Remove en Bike Light | Queda solo el Backpack, contador 1 | PASS | Ver captura 02. |

**4. Evidencia**

- `evidencia_TC004_01_carrito_antes.png`: Carrito con 2 productos antes de eliminar.

  ![Carrito con 2 productos antes de eliminar.](../evidencias/capturas/evidencia_TC004_01_carrito_antes.png)

- `evidencia_TC004_02_carrito_tras_eliminar.png`: Carrito con 1 producto y contador 1 después de eliminar el Bike Light.

  ![Carrito con 1 producto y contador 1 después de eliminar el Bike Light.](../evidencias/capturas/evidencia_TC004_02_carrito_tras_eliminar.png)

**5. Si el resultado es FAIL**: N/A. El resultado fue PASS. Referencia del defecto: N/A

**6. Observaciones de ejecución**: Ninguna.


---

## TC-005 · Validación de campos obligatorios en el checkout

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-005 | Validación de campos obligatorios en el checkout | Alta | Negativa / Validación | Checkout | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que el formulario de información del checkout exija First Name, Last Name y Zip/Postal Code, y que con los tres completos avance al resumen de compra.

**2. Precondiciones**

| Estado inicial | Sesión iniciada con standard_user. Carrito con Sauce Labs Backpack, en /checkout-step-one.html con los campos vacíos. |
|---|---|
| Usuario / permisos | Usuario estándar de demostración (standard_user). |
| Configuración | Google Chrome 155 en Windows. |

**3. Datos de prueba**

| Dato | Nombre / Apellido / Código postal |
|---|---|
| Valor | Sebastian / Camacho / 0000 |
| Origen | Generado (datos ficticios) |
| Observación | Se completa un campo por intento, en el orden del formulario. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Hacer clic en Continue con los tres campos vacíos | — | Se muestra “Error: First Name is required” y no se avanza. |
| 2 | Escribir First Name y hacer clic en Continue | Sebastian | Se muestra “Error: Last Name is required” y no se avanza. |
| 3 | Escribir Last Name y hacer clic en Continue | Camacho | Se muestra “Error: Postal Code is required” y no se avanza. |
| 4 | Escribir Zip/Postal Code y hacer clic en Continue | 0000 | Se abre /checkout-step-two.html con el resumen: Item total $29.99, Tax $2.40, Total $32.39. |

**5. Resultado esperado final (criterio de éxito)**: Cada campo faltante genera su mensaje de error. Con los tres completos se muestra el resumen con totales correctos.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-005 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:16 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **PASS**

**2. Resultado observado**: Los tres mensajes de error aparecieron en el orden esperado. Con los tres campos completos se abrió el resumen (Checkout: Overview) con Sauce Labs Backpack, Item total $29.99, Tax $2.40 y Total $32.39.

**Comparación**: Coincide con lo esperado. El impuesto corresponde al 8 % del subtotal ($29.99 × 8 % = $2.40).

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Continue con campos vacíos | Error: First Name is required | PASS | Ver captura 02. |
| 2 | First Name y Continue | Error: Last Name is required | PASS | Ver captura 03. |
| 3 | Last Name y Continue | Error: Postal Code is required | PASS | Ver captura 04. |
| 4 | Postal Code y Continue | Resumen con Total $32.39 | PASS | Ver captura 05. |

**4. Evidencia**

- `evidencia_TC005_01_formulario_vacio.png`: Formulario Checkout: Your Information con los campos vacíos.

  ![Formulario Checkout: Your Information con los campos vacíos.](../evidencias/capturas/evidencia_TC005_01_formulario_vacio.png)

- `evidencia_TC005_02_first_name_required.png`: Error “First Name is required” con los campos vacíos.

  ![Error “First Name is required” con los campos vacíos.](../evidencias/capturas/evidencia_TC005_02_first_name_required.png)

- `evidencia_TC005_03_last_name_required.png`: Error “Last Name is required” con solo First Name completo.

  ![Error “Last Name is required” con solo First Name completo.](../evidencias/capturas/evidencia_TC005_03_last_name_required.png)

- `evidencia_TC005_04_postal_required.png`: Error “Postal Code is required” con nombre y apellido completos.

  ![Error “Postal Code is required” con nombre y apellido completos.](../evidencias/capturas/evidencia_TC005_04_postal_required.png)

- `evidencia_TC005_05_resumen_compra.png`: Resumen de compra con Item total, Tax y Total.

  ![Resumen de compra con Item total, Tax y Total.](../evidencias/capturas/evidencia_TC005_05_resumen_compra.png)

**5. Si el resultado es FAIL**: N/A. El resultado fue PASS. Referencia del defecto: N/A

**6. Observaciones de ejecución**: No se presionó Finish: la compra no se confirmó.


---

## TC-006 · Gestión del carrito desde el catálogo con problem_user (adicional)

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-006 | Gestión del carrito desde el catálogo con problem_user (adicional) | Alta | Funcional (exploratoria) | Catálogo y carrito | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que un usuario nuevo (problem_user) vea el catálogo con las imágenes de cada producto, un carrito vacío, y pueda agregar y quitar productos desde el catálogo.

**2. Precondiciones**

| Estado inicial | Sesión cerrada del usuario anterior; pantalla de login. Se espera un carrito vacío para el usuario nuevo. |
|---|---|
| Usuario / permisos | problem_user (usuario de demostración con fallos intencionales). |
| Configuración | Google Chrome 155 en Windows. Ordenamiento por defecto: Name (A to Z). |

**3. Datos de prueba**

| Dato | Usuario / Contraseña / Productos |
|---|---|
| Valor | problem_user / secret_sauce. Los 6 productos del catálogo |
| Origen | Usuarios de demostración publicados en la página de login |
| Observación | Caso adicional a los 5 solicitados, para explorar defectos. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Iniciar sesión como problem_user | problem_user / secret_sauce | Se muestra el catálogo con el carrito vacío. |
| 2 | Revisar la imagen de cada uno de los 6 productos | — | Cada producto muestra su propia imagen. |
| 3 | Hacer clic en Add to cart de Bike Light, Bolt T-Shirt y Fleece Jacket | 3 productos | Los 3 botones cambian a Remove y el contador muestra 4. |
| 4 | Repetir Add to cart en Bolt T-Shirt y Fleece Jacket, y probar Onesie y Test.allTheThings() T-Shirt (Red) | 4 productos | Cada botón cambia a Remove. |
| 5 | Hacer clic en Remove de Backpack, Bike Light y Onesie desde el catálogo | 3 productos | Cada botón vuelve a Add to cart y el contador baja a 0. |
| 6 | Abrir el carrito y hacer clic en Remove del Backpack | Sauce Labs Backpack | El producto se elimina y el contador baja. |

**5. Resultado esperado final (criterio de éxito)**: El catálogo muestra las imágenes correctas, agregar y quitar productos funciona en todos los productos y el carrito del usuario nuevo comienza vacío.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-006 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:18 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **FAIL**

**2. Resultado observado**: Se accedió al catálogo, pero el carrito ya traía el Backpack del usuario anterior (contador 1). Los 6 productos muestran la misma foto de un perro. Add to cart no respondió en Bolt T-Shirt, Fleece Jacket ni Test.allTheThings() T-Shirt (Red); sí funcionó en Bike Light y Onesie. Remove no respondió en el catálogo en ninguno de los 3 productos probados (el contador siguió en 3). Dentro del carrito, Remove sí funcionó.

**Comparación**: No coincide. Se encontraron 4 desviaciones: carrito heredado, imágenes repetidas, Add to cart sin respuesta en 3 de 6 productos y Remove sin respuesta en el catálogo.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Iniciar sesión | Catálogo visible, pero el carrito ya tenía 1 producto | FAIL | BUG-06-F. Ver captura 01. |
| 2 | Revisar imágenes | Los 6 productos muestran la misma foto de un perro | FAIL | BUG-02-UI. Ver captura 01. |
| 3 | Add to cart en 3 productos | Solo Bike Light cambió; Bolt y Fleece sin cambio | FAIL | BUG-03-F. Ver captura 02. |
| 4 | Repetir Add to cart y probar otros | Onesie cambió; Bolt, Fleece y Red no responden | FAIL | BUG-03-F. Ver captura 03. |
| 5 | Remove desde el catálogo | Ningún botón respondió; contador sigue en 3 | FAIL | BUG-04-F. Ver captura 04. |
| 6 | Remove desde el carrito | El Backpack se eliminó; contador 2 | PASS | Ver capturas 05 y 06. |

**4. Evidencia**

- `evidencia_TC006_01_catalogo_imagenes_repetidas.png`: Catálogo de problem_user: imágenes repetidas y Backpack ya en el carrito (contador 1).

  ![Catálogo de problem_user: imágenes repetidas y Backpack ya en el carrito (contador 1).](../evidencias/capturas/evidencia_TC006_01_catalogo_imagenes_repetidas.png)

- `evidencia_TC006_02_agregar_tres_clics.png`: Tras 3 clics en Add to cart, Bolt y Fleece siguen sin cambiar.

  ![Tras 3 clics en Add to cart, Bolt y Fleece siguen sin cambiar.](../evidencias/capturas/evidencia_TC006_02_agregar_tres_clics.png)

- `evidencia_TC006_03_agregar_no_responde.png`: Onesie cambió a Remove; Bolt, Fleece y Test.allTheThings() T-Shirt (Red) siguen en Add to cart.

  ![Onesie cambió a Remove; Bolt, Fleece y Test.allTheThings() T-Shirt (Red) siguen en Add to cart.](../evidencias/capturas/evidencia_TC006_03_agregar_no_responde.png)

- `evidencia_TC006_04_remove_listado_no_responde.png`: Tras hacer clic en Remove, los botones del catálogo no cambian.

  ![Tras hacer clic en Remove, los botones del catálogo no cambian.](../evidencias/capturas/evidencia_TC006_04_remove_listado_no_responde.png)

- `evidencia_TC006_05_carrito_tres_items.png`: Carrito con 3 productos (Backpack, Bike Light y Onesie).

  ![Carrito con 3 productos (Backpack, Bike Light y Onesie).](../evidencias/capturas/evidencia_TC006_05_carrito_tres_items.png)

- `evidencia_TC006_06_remove_en_carrito_funciona.png`: Carrito tras eliminar el Backpack: quedan 2 productos y el contador baja a 2.

  ![Carrito tras eliminar el Backpack: quedan 2 productos y el contador baja a 2.](../evidencias/capturas/evidencia_TC006_06_remove_en_carrito_funciona.png)

**5. Si el resultado es FAIL**: Carrito heredado del usuario anterior; imágenes repetidas; Add to cart sin respuesta en 3 de 6 productos; Remove sin respuesta en el catálogo. Referencia del defecto: BUG-02-UI, BUG-03-F, BUG-04-F, BUG-06-F

**6. Observaciones de ejecución**: El carrito heredado se confirmó con la sesión anterior (standard_user), que había dejado el Backpack en el carrito (ver TC-004).


---

## TC-007 · Checkout con datos válidos con problem_user (adicional)

### Parte 1 · Diseño del caso de prueba

| ID del TC | Título | Prioridad | Tipo | Módulo | Ambiente |
|---|---|---|---|---|---|
| TC-007 | Checkout con datos válidos con problem_user (adicional) | Alta | Funcional (exploratoria) | Checkout | Demo público (saucedemo.com), Chrome 155 / Windows |

**1. Objetivo (¿Qué se quiere validar?)**: Que un usuario con nombre, apellido y código postal válidos pueda completar el formulario de información del checkout y avanzar al resumen.

**2. Precondiciones**

| Estado inicial | Sesión iniciada con problem_user. Carrito con Bike Light y Onesie, en /cart.html. |
|---|---|
| Usuario / permisos | problem_user (usuario de demostración con fallos intencionales). |
| Configuración | Google Chrome 155 en Windows. |

**3. Datos de prueba**

| Dato | Nombre / Apellido / Código postal |
|---|---|
| Valor | Sebastian / Camacho / 0000 |
| Origen | Generado (datos ficticios) |
| Observación | Caso adicional a los 5 solicitados. |

**4. Pasos y resultados esperados**

| # | Paso / acción | Dato utilizado | Resultado esperado |
|---|---|---|---|
| 1 | Hacer clic en Checkout desde el carrito | — | Se muestra el formulario con First Name, Last Name y Zip/Postal Code vacíos. |
| 2 | Escribir el nombre en First Name y el apellido en Last Name | Sebastian / Camacho | Cada campo muestra su valor. |
| 3 | Escribir el código postal en Zip/Postal Code | 0000 | El campo muestra 0000. |
| 4 | Hacer clic en Continue | — | Se abre el resumen de compra (Checkout: Overview). |

**5. Resultado esperado final (criterio de éxito)**: Con los tres campos completos se avanza al resumen de compra sin errores.

### Parte 2 · Ejecución de la prueba

| ID del TC | Ejecutado por | Fecha | Hora | Ambiente | Versión |
|---|---|---|---|---|---|
| TC-007 | Sebastián Ariel Camacho Loayza | 20/10/2026 | 21:19 | Demo público (saucedemo.com), Chrome 155 / Windows | Sin versión visible (sitio de demostración) |

**1. Resultado de la ejecución**: **FAIL**

**2. Resultado observado**: Al escribir el apellido, el texto se ingresó en el campo First Name y lo sobrescribió: First Name quedó con “o” y Last Name vacío. Al presionar Continue apareció “Error: Last Name is required” y no se avanzó.

**Comparación**: No coincide. El sistema no permite registrar el apellido y bloquea el checkout.

**3. Registro de ejecución por paso**

| # | Paso ejecutado | Resultado observado | Estado | Observación |
|---|---|---|---|---|
| 1 | Clic en Checkout | Formulario con campos vacíos | PASS | — |
| 2 | Escribir nombre y apellido | First Name quedó con “o” y Last Name vacío | FAIL | BUG-05-F. Ver captura 01. |
| 3 | Escribir código postal | Zip/Postal Code muestra 0000 | PASS | — |
| 4 | Clic en Continue | Error: Last Name is required; no avanza | FAIL | BUG-05-F. Ver captura 02. |

**4. Evidencia**

- `evidencia_TC007_01_first_name_sobrescrito.png`: Formulario con First Name en “o”, Last Name vacío y Zip en 0000.

  ![Formulario con First Name en “o”, Last Name vacío y Zip en 0000.](../evidencias/capturas/evidencia_TC007_01_first_name_sobrescrito.png)

- `evidencia_TC007_02_last_name_required.png`: Error “Last Name is required” aunque el apellido fue escrito.

  ![Error “Last Name is required” aunque el apellido fue escrito.](../evidencias/capturas/evidencia_TC007_02_last_name_required.png)

**5. Si el resultado es FAIL**: Escribir en Last Name modifica First Name; Last Name queda vacío y no se puede completar el checkout. Referencia del defecto: BUG-05-F

**6. Observaciones de ejecución**: Se verificó con JavaScript el valor de los campos: first=“o”, last=“”, zip=“0000”.


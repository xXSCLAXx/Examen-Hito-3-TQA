# Escenarios Gherkin — SauceDemo

Aplicación: https://www.saucedemo.com/ · Los escenarios describen comportamiento, no automatizan por sí solos las pruebas.

## Feature: Inicio de sesión

```gherkin
Feature: Inicio de sesión
  Como usuario de Swag Labs
  Quiero iniciar sesión con mis credenciales
  Para acceder al catálogo de productos

  Scenario: Acceso exitoso con credenciales válidas
    Given que estoy en la página de login de SauceDemo
    When ingreso el usuario "standard_user" y la contraseña "secret_sauce"
    And presiono el botón "Login"
    Then debería acceder a la página de productos
    And debería ver el título "Products"

  Scenario: Credenciales incorrectas
    Given que estoy en la página de login de SauceDemo
    When ingreso el usuario "standard_user" y la contraseña "clave_incorrecta"
    And presiono el botón "Login"
    Then debería mostrarse el mensaje "Epic sadface: Username and password do not match any user in this service"
    And debería permanecer en la página de login

  Scenario: Usuario bloqueado
    Given que estoy en la página de login de SauceDemo
    When ingreso el usuario "locked_out_user" y la contraseña "secret_sauce"
    And presiono el botón "Login"
    Then debería mostrarse el mensaje "Epic sadface: Sorry, this user has been locked out."
    But no debería acceder al catálogo
```

## Feature: Carrito y checkout

```gherkin
Feature: Carrito y checkout
  Como usuario autenticado
  Quiero agregar productos al carrito y completar la compra
  Para recibir los productos que seleccioné

  Background:
    Given que inicié sesión con el usuario "standard_user"

  Scenario: Agregar un producto al carrito
    When presiono "Add to cart" en el producto "Sauce Labs Backpack"
    Then el botón del producto debería cambiar a "Remove"
    And el ícono del carrito debería mostrar el número 1

  Scenario: Checkout con datos obligatorios incompletos
    Given que tengo el producto "Sauce Labs Backpack" en el carrito
    And estoy en el formulario de información de checkout
    When dejo vacío el campo "First Name"
    And presiono "Continue"
    Then debería mostrarse el mensaje "Error: First Name is required"
    And no debería avanzar al resumen de la compra

  Scenario: Compra completada con éxito
    Given que tengo el producto "Sauce Labs Backpack" en el carrito
    And estoy en el formulario de información de checkout
    When ingreso nombre "Sebastian", apellido "Camacho" y código postal "0000"
    And presiono "Continue"
    And presiono "Finish" en el resumen de la compra
    Then debería mostrarse el mensaje "Thank you for your order!"
```

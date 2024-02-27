# Web Scrapping Game Crawler

## Descripción

El Game Price Scraper es una solución integral diseñada para agilizar la búsqueda y comparación de precios de videojuegos a través de múltiples plataformas de venta en línea, tales como G2A, INSTANT GAMING y PS4 STORE, entre otras. Utilizando tecnologías de vanguardia en el ámbito del desarrollo web y la ingeniería de software, esta herramienta busca optimizar la experiencia de compra de los usuarios al proporcionarles información actualizada sobre las mejores ofertas disponibles.

## Arquitectura Técnica

### Web Scraping con Scrappy

El corazón de la aplicación reside en su capacidad para extraer datos de manera eficiente utilizando Scrapy, un poderoso framework de Python diseñado específicamente para el web scraping. Mediante el desarrollo de spiders personalizados, se realiza la extracción sistemática de información relevante sobre precios y disponibilidad de juegos en las plataformas objetivo.

### Almacenamiento en Mini Database JSON

Para la persistencia de datos, se implementa una base de datos no relacional basada en JSON, optimizada para un acceso rápido y eficiente a la información recabada. Este enfoque permite una manipulación flexible de los datos y facilita la integración con sistemas y tecnologías frontend.

### Backend con Flask

El backend de la aplicación se desarrolla utilizando Flask, un microframework de Python que ofrece la flexibilidad necesaria para construir aplicaciones web robustas y escalables. A través de Flask, se exponen endpoints RESTful que permiten la comunicación entre el frontend y el backend, asegurando una arquitectura desacoplada y modular.

### Frontend con VueJS

En el lado del cliente, se utiliza VueJS para el desarrollo del frontend. Este framework progresivo de JavaScript es elegido por su reactividad y por facilitar la construcción de interfaces de usuario dinámicas e interactivas. A través de VueJS, los usuarios pueden visualizar los juegos y sus precios de manera clara y ordenada, mejorando significativamente la experiencia de búsqueda de promociones.

## Características Principales

- **Búsqueda Eficiente de Juegos:** Capacidad para buscar y comparar precios de videojuegos en varias plataformas de venta en línea.
- **Actualización Automática:** Los spiders de Scrapy se ejecutan periódicamente para mantener actualizada la base de datos con las últimas ofertas.
- **Interfaz Amigable:** Una interfaz de usuario desarrollada con VueJS que facilita la navegación y mejora la experiencia del usuario.
- **API RESTful:** Endpoints bien definidos que permiten la recuperación de datos de juegos de manera programática.

## Cómo Empezar

Para comenzar a utilizar el Game Price Scraper, siga estos pasos:

1. **Clonar el Repositorio:**

```bash
https://github.com/akhoz/Web-Scraping-Game-Crawler
```

### Licencia
Este proyecto está bajo la Licencia MIT. Para más detalles, vea el archivo LICENSE.md

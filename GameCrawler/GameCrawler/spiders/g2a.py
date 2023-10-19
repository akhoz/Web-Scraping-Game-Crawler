import scrapy


class G2aSpider(scrapy.Spider):
    name = "g2a"
    start_urls = ["https://www.g2a.com/es/category/games-c189?drm%5B0%5D=273&f%5Bdrm%5D%5B0%5D=8586&region%5B0%5D=878&region%5B1%5D=8355"]

    def parse(self, response):
        elemento = response.xpath('//*[@id="10000340096028"]/div/div[2]/div[2]/div/div/span')

        # Extrae el texto del elemento
        texto = elemento.get()

        # Imprime el resultado
        partes = texto.split("<!-- -->")

        resultados = []

        # Iterar a través de las partes y extraer lo que está antes de "<:"
        for parte in partes:
            if "<" in parte:
                resultado = parte.split("<")[0]
                resultados.append(resultado)

        # Ahora, resultados contendrá lo que está antes de "<:" en cada sección del texto
        for resultado in resultados:
            print(resultado)




import scrapy
from houseSeeker.config import (
    urlImovel,
    urlPrincipal,
    mainCss,
    cssLink,
    cssTipo,
    cssPreco1,
    cssPreco2,
    cssSpecs,
    cssEndereco,
)


class AptoSpider1(scrapy.Spider):
    name = "aptoFinder"
    allowed_domains = [urlPrincipal]
    start_urls = [
        urlImovel,
    ]

    def parse(self, response):
        aptosDisponiveis = response.css(mainCss)
        for aptoDisponivel in aptosDisponiveis:
            yield {
                "link": aptoDisponivel.css(cssLink).get(),
                "tipo": aptoDisponivel.css(cssTipo).get(),
                "preco1": aptoDisponivel.css(cssPreco1).get(),
                "preco2": aptoDisponivel.css(cssPreco2).get(),
                "specs": aptoDisponivel.css(cssSpecs).get(),
                "endereço": aptoDisponivel.css(cssEndereco).get(),
            }

        # Identifica o link para a próxima página
        # next_page = response.css(nextPage).get()
        # if next_page:
        #    yield response.follow(next_page, callback=self.parse)

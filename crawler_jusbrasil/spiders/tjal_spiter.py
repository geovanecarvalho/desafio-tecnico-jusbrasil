import scrapy


class TjalSpiterPrimeiroGrau(scrapy.Spider):
    name = 'primeiro_grau'
    numero_processo = "0710802-55.2018.8.02.0001"
    start_urls = [f'https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000O7550000&processo.foro=1&processo.numero={numero_processo}']

    def parse(self, response):
        pass

        

    


import scrapy

class ZapImoveis(scrapy.Spider):
    name = "zapimoveis"
    
    def start_requests(self):
        urls = [
            'https://www.zapimoveis.com.br/venda/casas/sp+jundiai/#{%22precomaximo%22:%222147483647%22,%22possuiendereco%22:%22True%22,%22parametrosautosuggest%22:[{%22Bairro%22:%22%22,%22Zona%22:%22%22,%22Cidade%22:%22JUNDIAI%22,%22Agrupamento%22:%22%22,%22Estado%22:%22SP%22}],%22pagina%22:%221%22,%22ordem%22:%22Relevancia%22,%22paginaOrigem%22:%22ResultadoBusca%22,%22semente%22:%221280926929%22,%22formato%22:%22Galeria%22}',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content = response.xpath("//article/@data-clickstream").extract()
        for imovel in content:
            print('inicio')
            print(imovel)
            print('fim')
        

        
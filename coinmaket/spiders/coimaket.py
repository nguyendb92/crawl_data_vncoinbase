import scrapy
from ..items import CoinmaketItem

class CoinmaketSprider(scrapy.Spider):
    name = 'coinmaket'
    start_urls =["https://coinmarketcap.com/all/views/all/",]

    def parse(self,response):
        names = response.xpath('//td/a[@class="currency-name-container link-secondary"]/text()').extract()
        market_cap = response.xpath('//td[@class="no-wrap market-cap text-right"]/text()').extract()
        market_caps = [i.strip() for i in market_cap]
        symbols = response.xpath('//td[@class="text-left col-symbol"]/text()').extract()
        prices = response.xpath('//td/a[@class="price"]/text()').extract()

        ciculating_supplys= response.xpath('//td[@class="no-wrap text-right circulating-supply"]/@data-sort').extract()



        volumes= response.xpath('//td[@class="no-wrap text-right "]/a/text()').extract()

        changes = response.xpath('//td[@data-timespan="24h"]/@data-percentusd').extract()

        item = CoinmaketItem()
        import pdb; pdb.set_trace()

        items = list(zip(names, market_caps, symbols, prices, ciculating_supplys, volumes, changes))
        # import pdb; pdb.set_trace()
        for tup in items[1:-1]:
            item['name'] = tup[0]
            item['market_cap'] = tup[1]
            item['symbol'] = tup[2]
            item['price'] = tup[3]
            item['ciculating_supply']= tup[4]
            item['volume'] = tup[5]
            item['change'] = [True if float(tup[6]) > 0 else False]
            yield item

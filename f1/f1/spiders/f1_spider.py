import scrapy


class F1Spider(scrapy.Spider):
    name = 'f1'

    start_urls = [
        'https://www.formula1.com/en/results.html/2010/drivers.html'
    ]

    def parse(self, response):
        drivers = []

        lines = response.css('.resultsarchive-table tbody tr')
        for line in lines:
            columns = line.css('td')
            drivers_names = columns[2].css('span::text').extract()
            # drivers_position = columns[0].css('::text')
            yield {
                'first_name': drivers_names[0],
                'last_name': drivers_names[1],
                'abreviation_name': drivers_names[2],
                'nationality': columns[3].css('::text').extract()[0],
            }
            # drivers_team = columns[4].css('a::text').extract()

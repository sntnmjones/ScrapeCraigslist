import scrapy
import datetime

class RentalSpider(scrapy.Spider):
    name = "rentals"
    start_urls = [
        'https://redding.craigslist.org/d/apartments-housing-for-rent/search/apa?sort=date&',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]

        rentals = response.xpath('body/section/form/div[@class="content"]/ul/li')
        curDate = datetime.datetime.now()
        # strCurDate = str(curDate.year) + '-' + str(curDate.month) + '-' + str(curDate.day)
        strCurDate = f'{curDate.year}-{curDate.month}-{curDate.day}'

        filename = f'rentalresults'
        f = open(filename, "w")

        for rental in rentals:
            url = rental.xpath('a/@href').get()
            price = rental.xpath('a/span/text()').get()
            date = rental.xpath('div[@class="result-info"]/time/@datetime').get()

            if strCurDate in date:
                f.write(f'{price}, {url}\n')
            else:
                break

        f.close()

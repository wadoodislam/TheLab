import scrapy
from ..items import ArticleItem


class OpinionSpider(scrapy.Spider):
    name = 'opinion'
    start_urls = [
        'https://www.aljazeera.com/indepth/opinion/'
    ]
    count = 1

    def parse(self, response):

        for link in response.css('div h2.topics-sec-item-head a::attr(href)').extract():
            if self.count <= 500:
                self.count += 1
                yield response.follow(link, callback=self.parse_content)

        params = {
            'cmd': 'ajax',
            'cmdtext': response.css('.showmorebutton::attr(cmdtext)').get(),
            'pageid': response.css('#oryxcontext::attr(data-postingguid)').get(),
        }
        fd = {'oryxcontext': 'B8C906090FB19032EA03A7D3B8D5B5D721A1533F29C2BCDE8DF9FACA3DC4A1A912B19BBB727908DD9826CDDA8A46C710A002BF599DA40D825BE8221AA0B76BF2EC07253C0D83D6C0D329C1BB1D6A536435B0FC288AB81B5B517339E0A1C2A8B3231154BAF0EF2B9A063AF0DB243020017E2295BA4FF34390B74254B0BA5C3CB61AB1FAA5A3BCE390D0E5B626DC7FE61C0D680380B382061CE14A5755DD578975CABDF28EF0CDB194A01186F8BE0AC7B150B1F9319E9A41934DCAE97E6E96FF7231D97E040CD0BE7507BBC1B5CA9E47E743485B7455A8D687FC83F56121BF7AD5C45A2A87C3693D636FF5D4F1CB8552520E409A520D95FCAB6D06F229CD83E94DDBCA2084C3A17CF14AC417A324A01DC6A7C6DD5EAC5A02FE877E8B9FB45D831289F26746B0070C39C2CB73589E1701F8'} #response.css('#oryxcontext::attr(value)').get()
        url = f'https://www.aljazeera.com/portal/handlers/HTMLParser.ashx?cmd=ajax&cmdtext={params["cmdtext"]}&pageid={params["pageid"]}'
        if self.count <= 500:
            yield scrapy.FormRequest(url=url, callback=self.parse, formdata=fd, dont_filter=True)

    def parse_content(self, response):
        items = ArticleItem()
        items['title'] = response.css('.post-title::text').extract()
        items['tags'] = response.css('#article-body-topics a::text').extract()
        items['author'] = response.css('.article-heading-author-name a::text').extract()
        items['url'] = response.css('link[rel="amphtml"]::attr(href)').extract()
        
        yield items


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

        req_headers = {
                     # 'Host': 'www.aljazeera.com',
                     'Connection': 'keep-alive',
                     # 'Content - Length': '620',
                     'Accept': '*/*',
                     'X-Requested-With': 'XMLHttpRequest',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 OPR/68.0.3618.173',
                     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                     'Origin': 'https://www.aljazeera.com',
                     'Sec-Fetch-Site': 'same-origin',
                     'Sec-Fetch-Mode': 'cors',
                     'Sec-Fetch-Dest': 'empty',
                     'Referer': 'https://www.aljazeera.com/indepth/opinion/',
                     # 'Accept - Encoding': 'gzip, deflate, br',
                     'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
                     'Cookie': 'AJEUserLocation=PK; AJEUserRegion=Punjab; AJEUserCity=Lahore; AJEUserCountry=Pakistan; __qca=P0-1987531848-1593179578871; ALJAZEERA_ENSIGHTEN_PRIVACY_BANNER_VIEWED=1; _cb_ls=1; _cb=BfuQHeCxl9ScCCCzDt; _ga=GA1.2.548141631.1593179623; _gid=GA1.2.492654449.1593179623; ASP.NET_SessionId=wfmpcokweygw2el04lnoqmpk; xdibx=N4Ig-mBGAeDGCuAnRIBcoAOGAuBnNAjAKwCcAzAEwAMRRFdJVANCBgG6wB22aRLu-VMXLVa9CoxbtcXHkJaIkAGzQgAFtmwZcqAPS6A7kYB0AcwD2500oCmx2OYC2ukCyXLVugJacAJjZw1XXMMHy9zTl1EGwBDWDUbXwBabC8sH1MkjHMfbCTqKgA2CgAWYhKSIjISSuMNRxU3PEJSSho6BioAXxYIGAxotjRQXxiAT0EAbWEyAgAOEqIyiQomGepxOY6AXR7wKGgbNhtuQWA9vrgvX1VIGpiAMxiyGyTfQpsSpJKyEsgkuYAdgoMSS5GKsEW9BsD1gSRm80WJSoVEBRBAXSAA_; owa_v=cdh%3D%3Eb88d6627%7C%7C%7Cvid%3D%3E1593179672171331549%7C%7C%7Cfsts%3D%3E1593179672%7C%7C%7Cdsfs%3D%3E1%7C%7C%7Cnps%3D%3E8; owa_s=cdh%3D%3Eb88d6627%7C%7C%7Clast_req%3D%3E1593259183%7C%7C%7Csid%3D%3E1593257684694626938%7C%7C%7Cdsps%3D%3E0%7C%7C%7Creferer%3D%3E%28none%29%7C%7C%7Cmedium%3D%3Edirect%7C%7C%7Csource%3D%3E%28none%29%7C%7C%7Csearch_terms%3D%3E%28none%29; _chartbeat2=.1593179622946.1593259183717.11.BjBGUgv3CEpB6Q8xBC3jSXpB_g76h.2'
        }

        params = {
            'cmd': 'ajax',
            'cmdtext': response.css('.showmorebutton::attr(cmdtext)').get(),
            'pageid': response.css('#oryxcontext::attr(data-postingguid)').get(),
        }
        fd = {'oryxcontext': 'B8C906090FB19032EA03A7D3B8D5B5D721A1533F29C2BCDE8DF9FACA3DC4A1A912B19BBB727908DD9826CDDA8A46C710A002BF599DA40D825BE8221AA0B76BF2EC07253C0D83D6C0D329C1BB1D6A536435B0FC288AB81B5B517339E0A1C2A8B3231154BAF0EF2B9A063AF0DB243020017E2295BA4FF34390B74254B0BA5C3CB61AB1FAA5A3BCE390D0E5B626DC7FE61C0D680380B382061CE14A5755DD578975CABDF28EF0CDB194A01186F8BE0AC7B150B1F9319E9A41934DCAE97E6E96FF7231D97E040CD0BE7507BBC1B5CA9E47E743485B7455A8D687FC83F56121BF7AD5C45A2A87C3693D636FF5D4F1CB8552520E409A520D95FCAB6D06F229CD83E94DDBCA2084C3A17CF14AC417A324A01DC6A7C6DD5EAC5A02FE877E8B9FB45D831289F26746B0070C39C2CB73589E1701F8'} #response.css('#oryxcontext::attr(value)').get()
        url = f'https://www.aljazeera.com/portal/handlers/HTMLParser.ashx?cmd=ajax&cmdtext={params["cmdtext"]}&pageid={params["pageid"]}'
        if self.count <= 500:
            yield scrapy.FormRequest(url=url, callback=self.parse, method='POST', formdata=fd, dont_filter=True)

    def parse_content(self, response):
        items = ArticleItem()
        title = response.css('.post-title::text').extract()
        tags = response.css('#article-body-topics a::text').extract()
        author = response.css('.article-heading-author-name a::text').extract()
        url = response.css('link[rel="amphtml"]::attr(href)').extract()
        items['author'] = author
        items['title'] = title
        items['url'] = url
        items['tags'] = tags
        yield items


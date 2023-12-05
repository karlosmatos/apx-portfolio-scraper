import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sys
import time
import pandas as pd



class ApxSpiderSpider(scrapy.Spider):
    name = 'apx_spider'
    allowed_domains = ['apx.vc']
    start_urls = ['https://apx.vc/our-portfolio']

    custom_settings = {
        'LOG_LEVEL' : 'ERROR',
        'USER_AGENT' : "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36",
        'DEFAULT_REQUEST_HEADERS' : {
            'Referer': 'https://www.google.com'
        }
        #   'CONCURRENT_REQUESTS' : '20',
    }
        
    def __init__(self):
        # can be replaced for debugging with browser = webdriver.FireFox()
        #self.browser = webdriver.PhantomJS(executable_path=PHANTOMJS_PATH, service_args=['--ignore-ssl-errors=true'])

        options = Options()
        #options.add_argument("--headless")
        
        self.browser=webdriver.Chrome(options=options)
        self.browser.set_window_size(1820, 980)          
        self.start_requests()
        
    def __del__(self):
        self.browser.quit()

    def parse(self, response):
        
        company_values = dict()
        data = []

        self.browser.get("https://apx.network/portfolio")
        self.browser.find_element(By.XPATH, '/html/body/div[5]/div/button/span').click()
        
        for i in range(1, 12):
            time.sleep(5)
            page=Selector(text=self.browser.page_source)
            companies_info = page.xpath("//article[@class='modal modal--portfolio-item']").extract()
            
            for company in companies_info:
                page = Selector(text=company)
                
                company_values['name'] = page.xpath('//div[@class="text-base font-bold uppercase font-display"]//text()').extract()[-1]
                
                try:
                    web_linkedin = page.xpath('//a//@href').extract()
                    for i, web in enumerate(web_linkedin):
                        company_values[f'web_{i}'] = web
                        

                except:
                    company_values['linkedin'] = None
                
                company_add_info = page.xpath('//div[@class="font-bold"]//text()').extract()
                for i, add_info in enumerate(company_add_info):
                    company_values[f'additional_info_{i}'] = add_info.strip().replace('\n', '')

                company_values['description'] = page.xpath('//div[@class="grid grid-cols-2"]//div[2]//text()').extract_first().strip().replace('\n', '')

                print(company_values)

                data.append(company_values)
                company_values = dict()
            
            self.browser.find_element(By.XPATH, "//span[normalize-space()='Next']").click()

        dataset = pd.DataFrame(data)
        dataset.to_csv('apx_portfolio_companies.csv', index=False)

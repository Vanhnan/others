import string
from agent import *
from models.products import *
import re

debug = True

def process_view_category(data, context, session):
    for view_categoryline in data.xpath("//div[@class='child'][@id='chi5']/div/a"): 
        url = view_categoryline.xpath("(.)/@href").string()
        cat = view_categoryline.xpath("(.)/text()").string()
        if url and cat:
           session.queue(Request(url), process_view_category2, {'cat': cat })

def process_view_category2(data, context, session):
    cat = context['cat']  
    for view_categoryline in data.xpath("//span[@class='prti']/a"): 
        url = view_categoryline.xpath("(.)/@href").string()
        name = view_categoryline.xpath("(.)/descendant::text()").string()
        if url and name and cat:
           session.queue(Request(url), process_view_product, {'url': url, 'name': name, 'cat': cat })

    nextref = data.xpath("//a[@title='Next page']//@href").string()
    if nextref:
       session.do(Request(nextref), process_view_category2, {'cat': cat })

def process_view_product(data, context, session):

    product = Product()
    product.category = context['cat']
    product.name = context['name'] 
    product.url = context['url']
    product.ssid = product.name

    #for imgs in data.xpath("//h1/ancestor::td[1]//img"):
    #    img = imgs.xpath("(.)/@src").string()
    #    if img:
    #       product.properties.append(ProductProperty(type="image" , value = {'src': img}))

    test = data.xpath("//span[@itemprop='reviewRating'][span]/span/@class").string()
    if test:
       for rev in data.xpath("//span[@itemprop='reviewRating'][span]"):
           review = Review()  
           review.product = product.name   
           review.url = product.url   
           review.ssid = product.ssid 
   
           date = rev.xpath("(.)/following::span[@itemprop='author']/ancestor::b[1]/preceding-sibling::text()").string()
           if date:
              date = re_search_once("(.+).", date) 
              review.date = date
           else:  
              review.date = "N/A"

           exc = rev.xpath("(.)/following::span[@itemprop='reviewBody'][1]/text()").string(multiple=True)
           if exc:
              review.properties.append(ReviewProperty(type="excerpt", value = exc ))  

           conc = rev.xpath("(.)/following::span[@itemprop='name'][1]/text()").string(multiple=True)
           if conc:
              review.properties.append(ReviewProperty(type="conclusion", value = conc ))  

           aut = rev.xpath("(.)/following::span[@itemprop='author'][1]/text()").string()
           if aut:
              review.authors.append(Person(name = aut, ssid = aut)) 

           fscore = 0
           for scores in rev.xpath("(.)/span[@class='bp-icon-star-on bp-icon-yellow']"):
               fscore = fscore + 1
           review.grades.append(Grade(type='overall', value = fscore, best = 5))                               

           review.type = 'user'

           product.reviews.append(review) 

       session.emit(product)

def run(context, session):
    session.browser.agent = "Explorer 8.0"
    session.queue(Request("http://www.backpackinglight.co.uk/equipment.html", max_age = 0), process_view_category, {})

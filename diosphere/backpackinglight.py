from agent import *
from models.products import *
import re


def run(context, session):
    session.queue(Request("http://www.backpackinglight.co.uk/equipment.html"), process_category, dict())


def process_category(data, context, session):
    for cat in data.xpath('//div[@id="cat-list"]//a'):
        url = cat.xpath("@href").string()
        name = cat.xpath("img//@alt").string()
        if url and name:
           session.queue(Request(url), process_productlist, dict(cat=name, url=url))


def process_productlist(data, context, session):
    for cat in data.xpath('//div[@id="cat-list"]//a'):
        url = cat.xpath('@href').string()
        name = cat.xpath('img//@alt').string()
        if url:
            session.queue(Request(url), process_productlist, dict(cat=context['cat']+'|'+name, url=url))

    for prod in data.xpath('//span[@class="prti"]/a'):
        url = prod.xpath('@href').string()
        name = prod.xpath('text()').string()
        if url:
            session.queue(Request(url), process_product, dict(context, name=name, url=url))

    next_url = data.xpath('(//a[@title="Next page"]//@href)[1]').string()
    if next_url:
       session.do(Request(next_url), process_productlist, dict(context, name=name, url=url))


def process_product(data, context, session):
    product = Product()
    product.category = context['cat']
    product.name = context['name']
    product.url = context['url']
    product.ssid = str(context['url']).split('/')[-1].split('.html')[0]

    for rev in data.xpath("//div[@itemprop='review']"):
       review = Review()
       review.url = product.url
       review.ssid = rev.xpath("@id").string()
       review.title = rev.xpath("(.)/following::div[@class='p'][1]//span[@itemprop='name'][1]//text()").string(multiple=True)

       date = rev.xpath("(.)/following::span[@itemprop='author'][1]/ancestor::b[1]/preceding-sibling::text()").string()
       if date:
          date = re_search_once("(.+).", date)
          review.date = date

       excerpt = rev.xpath("(.)/following::span[@itemprop='reviewBody'][1]/text()").string(multiple=True)
       if excerpt:
          review.properties.append(ReviewProperty(type="excerpt", value = excerpt))

       conclusion = rev.xpath("(.)/following::span[@itemprop='name'][1]/text()").string(multiple=True)
       if conclusion:
          review.properties.append(ReviewProperty(type="conclusion", value = conclusion))

       author = rev.xpath("(.)/following::span[@itemprop='author'][1]/text()").string()
       if author:
          review.authors.append(Person(name = author, ssid = author))

       rate = rev.xpath("(.)//span[@itemprop='reviewRating'][1]/following::meta[1]//@content").string()
       review.grades.append(Grade(type='overall', value = int(rate), best = 5))

       review.type = 'user'

       product.reviews.append(review)

       session.emit(product)


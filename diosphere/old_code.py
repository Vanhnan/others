from agent import *
from models.products import *
debug = True


def process_frontpage(data, context, session):
    for link in data.xpath("//div[@class='article-title']/a"):
        url = link.xpath("@href").string()
        title = link.xpath("descendant::text()").string(multiple=True)
        date = link.xpath("./../following-sibling::div[@class='article-info']/span[@class='article-date']//text()").string()

        excerpt = link.xpath("./../../following-sibling::div[@class='article txt-justify']/p//text()").string(multiple=True)

        product = Product()
        product.name = title
        product.url = url
        product.ssid = title
        product.category = 'Mobile Devices'

        review = Review()
        review.type = 'pro'
        review.title = title
        review.ssid = title
        review.url = url
        review.date = date

        product.reviews.append(review)

        review.add_property(type='excerpt', value=excerpt)

        if excerpt:
            session.emit(product)

    nexturl = data.xpath("//div[@class='pagination txt-center']/a[@class='btn-next']/@href").string()
    if nexturl:
        session.queue(Request(nexturl), process_frontpage, {})


def run(context, session):
    session.queue(Request('http://pcpinside.tistory.com/category/%EB%A6%AC%EB%B7%B0%26%EB%A6%AC%EB%B7%B0'), process_frontpage, {})


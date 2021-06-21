from agent import *
from models.products import *


def run(context, session):
    session.sessionbreakers = [SessionBreak(max_requests=3000)]
    session.queue(Request('http://pcpinside.tistory.com/category/%EB%A6%AC%EB%B7%B0%26%EB%A6%AC%EB%B7%B0'), process_revlist, dict())


def process_revlist(data, context, session):
    revs = data.xpath("//div[@class='article-title']/a")
    for rev in revs:
        name = rev.xpath("text()").string()
        url = rev.xpath("@href").string()
        session.queue(Request(url), process_review, dict(name=name, url=url))

    nexturl = data.xpath("//div[@class='pagination txt-center']/a[@class='btn-next']/@href").string()
    if nexturl:
        session.queue(Request(nexturl), process_revlist, dict(context))


def process_review(data, context, session):
    product = Product()
    product.name = context['name']
    product.url = context['url']
    product.category = data.xpath("//div[@class='article-tags']/a[1]//text()").string()
    if not product.category:
        product.category = str(context['url']).split('category=')[1]

    if 'http://pcpinside.tistory.com/' in str(context['url']):
        product.ssid = str(context['url']).replace('http://pcpinside.tistory.com/', '').split('?')[0]
    if 'https://pcpinside.tistory.com/' in str(context['url']):
        product.ssid = str(context['url']).replace('https://pcpinside.tistory.com/', '').split('?')[0]

    review = Review()
    review.type = 'pro'
    review.title = context['name']
    review.url = product.url
    review.date = data.xpath('//span[@class="article-date"]//text()').string()[:-1]
    review.ssid = product.ssid

    excerpt = data.xpath('//div[@class="article txt-justify"]//p//text()').string(multiple=True)
    if excerpt:
        review.add_property(type='excerpt', value=excerpt)

        product.reviews.append(review)
        session.emit(product)

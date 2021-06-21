def process_frontpage(data, context, session):
    for link in data.xpath("//div[@class='article-title']/a"):
        url = link.xpath("@href").string()
        title = link.xpath("descendant::text()").string(multiple=True)
        date = link.xpath(
            "./../following-sibling::div[@class='article-info']/span[@class='article-date']//text()").string()

        excerpt = link.xpath(
            "./../../following-sibling::div[@class='article txt-justify']/p//text()").string(multiple=True)

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
        review.grades.append(Grade(type='overall', value=None))

        product.reviews.append(review)

        review.add_property(type='excerpt', value=excerpt)

        if excerpt:
            session.emit(product)

    nexturl = data.xpath(
        "//div[@class='pagination txt-center']/a[@class='btn-next']/@href").string()
    if nexturl:
        session.queue(Request(nexturl), process_frontpage, {})

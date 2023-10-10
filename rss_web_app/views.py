from django.shortcuts import render
import feedparser
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    rss_feed_url = 'https://vnexpress.net/rss/tin-moi-nhat.rss'
    feed = feedparser.parse(rss_feed_url)
    
    items_rss = []
    #print(feed.entries)
    for item in feed.entries:
        item_title = item.get("title")
        item_pub_date = item.get("published")
        item_link = item.get("link")

        #print(item_title)

        description = item.get("summary")
        description_soup = BeautifulSoup(description, 'html.parser')
        description_text = description_soup.get_text()

        imag_tag = description_soup.find('img')
        image_src ="https://baogiaothong.mediacdn.vn/zoom/600_315/upload/images/2019-4/profile_avatar_img/2019-11-18/tin-tuc-trong-ngay-hom-nay-1574061980-width1004height565.png"
        
        if imag_tag:
            image_src = imag_tag['src']

        item_rss = {
            "title": item_title,
            "pub_date": item_pub_date,
            "link": item_link,
            "description": description_text,
            "image": image_src
        }
        items_rss.append(item_rss)

    return render(request, 'index.html',{"items_rss": items_rss})

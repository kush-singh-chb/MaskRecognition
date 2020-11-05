from icrawler.builtin import GoogleImageCrawler

google_crawler = GoogleImageCrawler(storage={'root_dir': 'data/without_mask'})
google_crawler.crawl(
    keyword='face portrait',
    filters={'size': "medium"},
    file_idx_offset=1231,
    max_num=100)

google_crawler = GoogleImageCrawler(storage={'root_dir': 'data/with_mask'})
google_crawler.crawl(
    keyword='images of face with mask',
    filters={'size': "medium"},
    file_idx_offset=2131,
    max_num=200)

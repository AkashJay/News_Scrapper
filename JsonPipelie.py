
BOT_NAME = 'newsbot'

SPIDER_MODULES = ['newsbot.spiders']
NEWSPIDER_MODULE = 'newsbot.spiders'



ROBOTSTXT_OBEY = True


ITEM_PIPELINES = {
   'newsbot.pipelines.JsonWriterPipeline': 300,
   # 'newsbot.pipelines.MongoDBPipeline': 800
}



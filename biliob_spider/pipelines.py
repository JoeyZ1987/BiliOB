# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from db import settings
import datetime
import logging

class VideoPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['video']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'aid': int(item['aid'])
            }, {
                '$set': {
                    'c_view':item['current_view'],
                    'c_favorite':item['current_favorite'],
                    'c_danmaku':item['current_danmaku'] ,
                    'c_coin':item['current_coin'],
                    'c_share':item['current_share'] ,
                    'c_like':item['current_like'],
                    'c_dislike':item['current_dislike'],
                    'c_datetime':item['current_datetime'],
                    'author': item['author'],
                    'subChannel': item['subChannel'],
                    'channel': item['channel'],
                    'mid': item['mid'],
                    'pic': item['pic'],
                    'title': item['title'],
                    'datetime': datetime.datetime.fromtimestamp(
                        item['datetime'])
                },
                '$push': {
                    'data': {
                        '$each':[item['data']],
                        '$position':0
                    }
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

class BangumiPipeLine(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['bangumi']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'title': item['title']
            }, {
                '$set': {
                    'title': item['title'],
                    'cover': item['cover'],
                    'isFinish': item['is_finish'],
                    'isStarted': item['is_started'],
                    'newest': item['newest_ep_index'],
                    'currentPts': item['data']['pts'],
                    'currentPlay': item['data']['play'],
                    'squareCover': item['square_cover'],
                    'currentWatch': item['data']['watch'],
                    'currentReview': item['data']['review'],
                    'currentDanmaku': item['data']['danmaku']
                },
                '$addToSet': {
                    'data': item['data']
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

class DonghuaPipeLine(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['donghua']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'title': item['title']
            }, {
                '$set': {
                    'title': item['title'],
                    'cover': item['cover'],
                    'isFinish': item['is_finish'],
                    'isStarted': item['is_started'],
                    'newest': item['newest_ep_index'],
                    'currentPts': item['data']['pts'],
                    'currentPlay': item['data']['play'],
                    'squareCover': item['square_cover'],
                    'currentWatch': item['data']['watch'],
                    'currentReview': item['data']['review'],
                    'currentDanmaku': item['data']['danmaku']
                },
                '$addToSet': {
                    'data': item['data']
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)
class SiteInfoPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['site_info']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.insert_one({
                    'region_count': item['region_count'],
                    'all_count': item['all_count'],
                    'web_online': item['web_online'],
                    'play_online': item['play_online'],
                    'datetime':datetime.datetime.now()
            })
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

class AuthorPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['author']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'mid': item['mid']
            }, {
                '$set': {
                    'name': item['name'],
                    'face': item['face'],
                    'official': item['official'],
                    'level': item['level'],
                    'sex': item['sex'],
                    'focus':True,
                    'c_fans':item['c_fans'],
                    'c_attention':item['c_attention'] ,
                    'c_archive':item['c_archive'] ,
                    'c_article':item['c_article'] ,
                    'c_archive_view':item['c_archive_view'],
                    'c_article_view':item['c_article_view'], 
                },
                '$push': {
                    'data': {
                        '$each':[item['data']],
                        '$position':0
                    }
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)
        
class OnlinePipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['video_online']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            
            self.coll.update_one({
                'title': item['title']
            }, {
                '$set': {
                    'title': item['title'],
                    'author': item['author'],
                    'channel': item['channel'],
                    'subChannel': item['subChannel'],
                },
                '$addToSet': {
                    'data': item['data']
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)


class TagPipeLine(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['tag']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            
            self.coll.update_one({
                'tag_id': item['tag_id']
            }, {
                '$set': {
                    'tag_name': item['tag_name'],
                    'ctime': item['ctime'],
                },
                '$addToSet': {
                    'use': item['use'],
                    'atten': item['atten'],
                    'datetime': datetime.datetime.now()
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)
class VideoAddPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['video']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            for each_aid in item['aid']:
                self.coll.update_one({
                    'aid': each_aid
                }, {
                    '$set': {
                        'aid': each_aid,
                        'focus': True
                    },
                }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

class AuthorChannelPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['author']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'mid': item['mid']
            }, {
                '$set': {
                    'channels': item['channels']
                },
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

class BiliMonthlyRankPipeline(object):
    def __init__(self):
        # 链接mongoDB
        self.client = MongoClient(settings['MINGO_HOST'], 27017)
        # 数据库登录需要帐号密码
        self.client.admin.authenticate(settings['MINGO_USER'],
                                       settings['MONGO_PSW'])
        self.db = self.client['biliob']  # 获得数据库的句柄
        self.coll = self.db['monthly_rank']  # 获得collection的句柄

    def process_item(self, item, spider):
        try:
            self.coll.update_one({
                'aid': item['aid']
            }, {
                '$addToSet': {
                    'pts': item['pts'],
                    'datetime': datetime.datetime.now()
                },
                '$set':{
                    'title': item['title'],
                    'author': item['author'],
                    'aid': item['aid'],
                    'mid': item['mid'],
                    'channel': item['channel'],
                    'currentPts':item['pts']
                }
            }, True)
            return item
        except Exception as error:
            # 出现错误时打印错误日志
            logging.error(error)

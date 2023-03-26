from textrank4zh import TextRank4Keyword, TextRank4Sentence
import jieba
import logging

# 取消jieba 的日志输出
jieba.setLogLevel(logging.ERROR)


# """提取关键词"""
def get_key_words(text, num=5):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=text, window=5, lower=True)
    key_words = tr4w.get_keywords(num)
    return [item.word for item in key_words]  # 命名 小行星 周先生 天文台 国际


# """提取摘要"""
def get_summary(text, num=3):
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=text, lower=True, source="all_filters")
    return [item.sentence for item in tr4s.get_key_sentences(num)]

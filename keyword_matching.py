import pandas as pd
from elasticsearch import Elasticsearch, helpers

# 连接到Elasticsearch
es = Elasticsearch()

# 导入课程描述数据
courses_df = pd.read_excel('course_info_clean.csv')
keywords_df = pd.read_excel('keyword_list.xlsx')

# 删除现有索引（如果存在）
if es.indices.exists(index='courses_index'):
    es.indices.delete(index='courses_index')

# 创建新的索引
es.indices.create(index='courses_index')

# 将课程描述导入Elasticsearch
actions = [
    {
        "_index": "courses_index",
        "_id": i,
        "_source": {
            "description": description
        },
    }
    for i, description in enumerate(courses_df['description'])
]

helpers.bulk(es, actions)


def search_keywords(keywords, index='courses_index'):
    results = []
    for keyword in keywords:
        # 定义搜索查询
        search_query = {
            "query": {
                "match": {
                    "description": keyword
                }
            }
        }
        response = es.search(index=index, body=search_query)
        for hit in response['hits']['hits']:
            results.append({
                "keyword": keyword,
                "matched_description": hit['_source']['description']
            })
    return results

# 获取关键词列表
keywords = keywords_df['keyword'].tolist()

# 搜索关键词并打印结果
matched_results = search_keywords(keywords)

# 将结果保存到新的Excel文件中
matched_results_df = pd.DataFrame(matched_results)
matched_results_df.to_excel('matched_results.xlsx', index=False)
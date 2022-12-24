import json
import boto3
import numpy as np
import pandas as pd
from opensearchpy import OpenSearch, RequestsHttpConnection

s3 = boto3.client('s3')
csv_data = s3.get_object(Bucket='cloud-final-images', Key='truncated_rec.csv')
recommend_csv = pd.read_csv(csv_data['Body'], dtype=str)

def fetch_data(username):
    region_name = 'us-east-1'
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table('ifashion-likes')
    response = table.get_item(
        Key={
            'email': username
        }
    )
    if 'Item' in response:
        return response['Item']['likes']
    else:
        return []
        
def format(liked_list):
    new_list = []
    for item in liked_list:
        if len(item) == 10:
            new_list.append(item[1:])
        else:
            new_list.append(item)
    print(new_list)
    return new_list

def get_recommend(input_list, recommend_table):
    LL = len(recommend_table)
    idx_start = np.random.randint(LL)
    rec = recommend_table[idx_start]
    intersec = [k for k in input_list if k in rec]
    s = len(intersec)
    for i in recommend_table:
        intersec_tmp = [k for k in input_list if k in i]
        s_tmp = len(intersec_tmp) 
        if s_tmp>s:
            rec = i
            s = s_tmp
    return rec, s 
    
def es_search(es_host, es_http_auth, index, rec):
    es_client = OpenSearch(
        hosts=[{'host': es_host, 'port': 443}],
        use_ssl=True,
        http_auth=es_http_auth,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    pictures = []
    for pic in rec:
        if len(pic) != 10:
            pic = '0' + pic
        result = es_client.search(index=index, body={"query": {"match": {"_id": pic}}})
        if 'hits' in result:
            for item in result['hits']['hits']:
                article_id = item['_id']
                if len(article_id) != 10:
                    article_id = '0' + article_id
                file_num = article_id[:3]
                jpg_id = article_id + '.jpg'
                path = 'https://cloud-final-images.s3.amazonaws.com/images/' + file_num + '/' + jpg_id
                pic_name = item['_source']['product_group_name'] + '-' + item['_source']['product_type_name'] 
                pic_dic = {
                    'id' : article_id,
                    'listPicUrl' : path,
                    'name' : pic_name,
                    'isLiked' : False
                }
                pictures.append(pic_dic)
    return pictures
        
def lambda_handler(event, context):
    global csv_data, recommend_csv
    username = event['queryStringParameters']['username']
    print(username)
    if username == 'null':
        rec = ['677930023', '919365008', '893059004', '923037003', '896169002', '715624052', '714790020', '924243002', '923037001', '931769003', '852584001']
    else:
        liked_list = fetch_data(username)
        liked_list = format(liked_list)
        recommend_table = recommend_csv.values.tolist()
        rec, s = get_recommend(liked_list, recommend_table)
        print(rec)
        print(s)
    es_host = 'search-opensearch-ifashion-domain-n4svedl66we46bvxmltfu5rbwe.us-east-1.es.amazonaws.com'
    es_http_auth = (,)
    pictures = es_search(es_host, es_http_auth, "articles", rec)
    print(pictures)
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(pictures)
    }
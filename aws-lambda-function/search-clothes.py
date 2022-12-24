import json
import boto3
from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection
    
def map_name(queryStringParameters):
    index_group_name = None
    garment_group_name = None
    q_list = queryStringParameters.lower().split(' ')
    category1 = {
        'men': 'Menswear',
        'man': 'Menswear',
        'menswear': 'Menswear',
        'woman': 'Ladieswear',
        'women': 'Ladieswear',
        'womenswear': 'Ladieswear',
        'lady': 'Ladieswear',
        'ladies': 'Ladieswear',
        'ladieswear': 'Ladieswear',
        'baby': 'Baby/Children',
        'babies': 'Baby/Children',
        'child': 'Baby/Children',
        'children': 'Baby/Children',
        'kid': 'Baby/Children',
        'kids': 'Baby/Children',
        'boy': 'Baby/Children',
        'boys': 'Baby/Children',
        'girl': 'Baby/Children',
        'girls': 'Baby/Children'
    }
    category2 = {
        'accessory' : 'Accessories',
        'accessories' : 'Accessories',
        'socks': 'Socks and Tights',
        'blouses': 'Blouses',
        'shorts': 'Shorts',
        'shoes': 'Shoes',
        'knitwear': 'Knitwear',
        'dresses': 'Dresses',
        'skirts': 'Dresses',
        'trousers': 'Trousers',
        'jersy': 'Jersey Fancy',
        'shirts': 'Shirts'
        
    }
    if len(q_list) == 1:
        if q_list[0] in category1.keys():
            index_group_name = category1[q_list[0]]
        elif q_list[0] in category2.keys():
            garment_group_name = category2[q_list[0]]
        
    else:
        if q_list[0] in category1.keys():
            index_group_name = category1[q_list[0]]
        elif q_list[0] in category2.keys():
            garment_group_name = category2[q_list[0]]
            
        if q_list[1] in category1.keys():
            index_group_name = category1[q_list[1]]
        elif q_list[1] in category2.keys():
            garment_group_name = category2[q_list[1]]
    print(index_group_name, garment_group_name)
    return index_group_name, garment_group_name

def es_search(es_host, es_http_auth, index, index_group_name, garment_group_name):
    es_client = OpenSearch(
        hosts=[{'host': es_host, 'port': 443}],
        use_ssl=True,
        http_auth=es_http_auth,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    paths = []
    ids = []
    
    if index_group_name is None and garment_group_name is None:
        result = []
    elif index_group_name is not None and garment_group_name is not None:
        result = es_client.search(index=index, size = 50, 
        body={
            "query": {
                "bool": {
                    "must": [
                        {   
                            "match": {
                                "index_group_name": index_group_name,
                            }
                            
                        },
                        {
                            "match": {
                                "garment_group_name": garment_group_name
                            }
                        }
                    ]
                }
            }
        })
    elif garment_group_name is None:
        result = es_client.search(index=index, size = 50, body={"query": {"match": {"index_group_name": index_group_name}}})
    elif index_group_name is None:
        result = es_client.search(index=index, size = 50, body={"query": {"match": {"garment_group_name": garment_group_name}}})
        
    pictures = []
    if 'hits' in result:
        for item in result['hits']['hits']:
            article_id = item['_id']
            if len(article_id) == 10:
                file_num = article_id[:3]
                jpg_id = article_id + '.jpg'
            else:
                print(article_id)
                file_num = '0' + article_id[:2]
                jpg_id = '0' + article_id + '.jpg'
            path = 'https://cloud-final-images.s3.amazonaws.com/images/' + file_num + '/' + jpg_id
            pic_name = item['_source']['product_group_name'] + '-' + item['_source']['product_type_name'] 
            pic = {
                'id' : article_id,
                'listPicUrl' : path,
                'name' : pic_name,
                'isLiked' : False
            }
            pictures.append(pic)
    return pictures

def lambda_handler(event, context):
    queryStringParameters = event['queryStringParameters']['q']
    
    index_group_name, garment_group_name = map_name(queryStringParameters)
    
    sen = 'category1 = ' + str(index_group_name) + ', category2 = ' + str(garment_group_name)
    print(sen)
    es_host = 'search-opensearch-ifashion-domain-n4svedl66we46bvxmltfu5rbwe.us-east-1.es.amazonaws.com'
    es_http_auth = (,)
    pictures = es_search(es_host, es_http_auth, "articles", index_group_name, garment_group_name)
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(pictures)
    }
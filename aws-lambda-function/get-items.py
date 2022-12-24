import json
import boto3
from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection

def map_name(category1, category2):
    index_group_name = '' 
    garment_group_name = ''
    if category1 == '1': # women
        index_group_name = 'Ladieswear'
        if category2 == '1':
            garment_group_name = 'Accessories'
        elif category2 == '2':
            garment_group_name = 'Blouses'
        elif category2 == '3':
            garment_group_name = 'Dresses Ladies'
        elif category2 == '4':
            garment_group_name = 'Jersey Fancy'
        elif category2 == '5':
            garment_group_name = 'Knitwear'
        elif category2 == '6':
            garment_group_name = 'Shorts'
        elif category2 == '7':
            garment_group_name = 'Shoes'
        elif category2 == '8':
            garment_group_name = 'Trousers'
        elif category2 == '9':
            garment_group_name = 'Socks and Tights'
        else:
            garment_group_name = None
            
    elif category1 == '2': # men
        index_group_name = 'Menswear'
        if category2 == '1':
            garment_group_name = 'Accessories'
        elif category2 == '2':
            garment_group_name = 'Jersey Fancy'
        elif category2 == '3':
            garment_group_name = 'Knitwear'
        elif category2 == '4':
            garment_group_name = 'Shirts'
        elif category2 == '5':
            garment_group_name = 'Shorts'
        elif category2 == '6':
            garment_group_name = 'Shoes'
        elif category2 == '7':
            garment_group_name = 'Trousers'
        elif category2 == '8':
            garment_group_name = 'Socks and Tights'
        else:
            garment_group_name = None
            
    elif category1 == '3': # Kids
        index_group_name = 'Baby/Children'
        if category2 == '1':
            garment_group_name = 'Accessories'
        elif category2 == '2':
            garment_group_name = 'Dresses/Skirts girls'
        elif category2 == '3':
            garment_group_name = 'Jersey Fancy'
        elif category2 == '4':
            garment_group_name = 'Knitwear'
        elif category2 == '5':
            garment_group_name = 'Shirts'
        elif category2 == '6':
            garment_group_name = 'Shorts'
        elif category2 == '7':
            garment_group_name = 'Shoes'
        elif category2 == '8':
            garment_group_name = 'Trousers'
        elif category2 == '9':
            garment_group_name = 'Socks and Tights'
        else:
            garment_group_name = None
    
    return index_group_name, garment_group_name

def es_search(es_host, es_http_auth, index, index_group_name, garment_group_name):
    es_client = OpenSearch(
        hosts=[{'host': es_host, 'port': 443}],
        use_ssl=True,
        http_auth=es_http_auth,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    
    if garment_group_name == None:
        result = es_client.search(index=index, size = 50, body={"query": {"match": {"index_group_name": index_group_name}}})
    else:
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
        }
        )
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
    category1 = event['pathParameters']['category1']
    category2 = event['pathParameters']['category2']
    index_group_name, garment_group_name = map_name(category1, category2)
    
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
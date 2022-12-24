import json
import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection

def es_search(es_host, es_http_auth, index, request_body):
    print(type(request_body))
    print(request_body)
    request_body = json.loads(request_body)
    
    sex = request_body["sex"]
    if sex == 'male':
        index_group_name = 'Menswear'
    elif sex == 'female':
        index_group_name = 'Ladieswear'
    else:
        index_group_name = 'Baby/Children'
    colors = request_body['colors']
    patterns = request_body['patterns']
    textures = request_body['textures']
    
    es_client = OpenSearch(
        hosts=[{'host': es_host, 'port': 443}],
        use_ssl=True,
        http_auth=es_http_auth,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    pictures = []
    
    if len(colors) >= 1 and len(patterns) >= 1 and len(textures) >= 1:
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
                                "perceived_colour_master_name": colors[0]
                            }
                        }
                    ],
                    "should": [
                        {
                            "match": {
                                "graphical_appearance_name": patterns[0]
                            }
                        },
                        {
                            "match": {
                                "graphical_appearance_name": textures[0]
                            }
                        }
                    ]
                }
            }
        })
        if 'hits' in result:
            for item in result['hits']['hits']:
                article_id = item['_id']
                if len(article_id) != 10:
                    article_id = '0' + article_id
                file_num = article_id[:3]
                jpg_id = article_id + '.jpg'
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
    print(event)
    request_body = event['body']
    es_host = 'search-opensearch-ifashion-domain-n4svedl66we46bvxmltfu5rbwe.us-east-1.es.amazonaws.com'
    es_http_auth = (,)
    pictures = es_search(es_host, es_http_auth, "articles", request_body)
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

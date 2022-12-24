import json
import boto3
from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection

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
        
def gen_pictures(items):
    pictures = []
    for article_id in items:
        if len(article_id) != 10:
            article_id = '0' + article_id
        file_num = article_id[:3]
        jpg_id = article_id + '.jpg'
        path = 'https://cloud-final-images.s3.amazonaws.com/images/' + file_num + '/' + jpg_id
        pic = {
                'id' : article_id,
                'listPicUrl' : path,
                'name' : '',
                'isLiked' : True
            }
        pictures.append(pic)
    return pictures
    
def es_search(es_host, es_http_auth, index, pictures):
    es_client = OpenSearch(
        hosts=[{'host': es_host, 'port': 443}],
        use_ssl=True,
        http_auth=es_http_auth,
        verify_certs=True,
        connection_class=RequestsHttpConnection
    )
    for pic in pictures:
        result = es_client.search(index=index, body={"query": {"match": {"_id": pic['id']}}})
        if 'hits' in result:
            item = result['hits']['hits'][0]
            pic_name = item['_source']['product_group_name'] + '-' + item['_source']['product_type_name'] 
            pic['name'] = pic_name
            print(pic)
    print(pic)
    return pictures
    
        
def lambda_handler(event, context):
    username = event['queryStringParameters']['username']
    fav_items = fetch_data(username)
    if len(fav_items) == 0:
        pictures = []
    else:
        pictures = gen_pictures(fav_items)
        es_host = 'search-opensearch-ifashion-domain-n4svedl66we46bvxmltfu5rbwe.us-east-1.es.amazonaws.com'
        es_http_auth = (,)
        pictures = es_search(es_host, es_http_auth, "articles", pictures)
    
    # TODO implement
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
        },
        'body': json.dumps(pictures)
    }

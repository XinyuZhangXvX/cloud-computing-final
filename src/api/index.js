/**
 * 导出所有的接口请求函数
 */
import req from './req'

const baseApi = "https://dbgqcxez61.execute-api.us-east-1.amazonaws.com/ifashion-api/"
 // get category items
 export const getCate=(catId)=>{
    console.log(baseApi+ catId +'/0')
    return req.get(baseApi+ catId +'/0');
 }

 // get subcategory items
 export const getSubCate=(catId, subCateId)=>{
    console.log(baseApi+ catId +'/' + subCateId)
    return req.get(baseApi+ catId +'/' + subCateId);
 }

// search items
export const getSearchResults=(keyword)=>{
   console.log(baseApi + 'search?q='+ keyword)
   return req.get(baseApi  + 'search?q='+ keyword);
}

// get favorite
export const getFavorite=(username)=>{
   console.log(baseApi+ 'myfavorite?username='+ username)
   return req.get(baseApi + 'myfavorite?username='+ username);
}

// post method to like an item
export const likeItem=(id, username)=>{
   // return req.post('/foo/like');
   // var params = {
   //    id: id.toString(),
   //    username: username
   // }
   console.log(baseApi + "like?id="+id + "&username="+username)
   req.post(baseApi + "like?id="+id + "&username="+username);
}

// post method to like an item
export const postQuestionnaire=(username, params)=>{
   
   console.log(baseApi + "questionnaire?id="+id + "&username="+username)
   req.post(baseApi +"questionnaire", params);
}
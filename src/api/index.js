/**
 * 导出所有的接口请求函数
 */
import req from './req'

 // get category items
 export const getCate=(catId)=>{
    console.log('/foo/'+ catId +'/0')
    return req.get('/foo/'+ catId +'/0');
 }

 // get subcategory items
 export const getSubCate=(catId, subCateId)=>{
    console.log('/foo/'+ catId +'/' + subCateId)
    return req.get('/foo/'+ catId +'/' + subCateId);
 }

// search items
export const getSearchResults=(keyword)=>{
   console.log('/foo/search?q='+ keyword)
   return req.get('/foo/search?q='+ keyword);
}

// get favorite
export const getFavorite=(username)=>{
   console.log('/foo/myfavorite?username='+ username)
   return req.get('/foo/myfavorite?username='+ username);
}

// post method to like an item
export const likeItem=(id, username)=>{
   
   // return req.post('/foo/like');
   // var params = {
   //    id: id.toString(),
   //    username: username
   // }
   console.log("/foo/like?id="+id + "&username="+username)
   req.post("/foo/like?id="+id + "&username="+username);
}
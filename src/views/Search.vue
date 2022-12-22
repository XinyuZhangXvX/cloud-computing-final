<template>
  <div class="search-result w">
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>Search Result</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div >
      <MyPanel title="Results" subTitle="There are the results">
        <ul class="goods-list">
          <li class="item" v-for="item in goods" :key="item.id">
            <img :src="item.listPicUrl" />
            <div class="title ellipsis-2">{{item.name}}</div>
            <a style="float: right;">
              <i class="fa-solid fa-heart favorite-right" v-if="map.get(item.id)" @click="toggleLike(item)"></i>
              <i class="fa-regular fa-heart favorite-right" v-else @click="toggleLike(item)"></i>
            </a>
          </li>
        </ul>
      </MyPanel>
    </div>
  </div>
  
</template>

<script>
import MyPanel from "@/components/MyPanel.vue";
import HomeVueSkeleton from '@/components/Skeleton/HomeVueSkeleton.vue'
import { defaultRecommend } from '@/utils/constants';
import { useRoute } from "vue-router";
import { useStore } from "vuex";
import { getSearchResults } from "@/api";
import { likeItem } from "@/api";
import { ref, computed } from "vue";
// import { getSearch } from "@/api";

export default {
  data(){
    return{
      map: new Map()
    }
  },
  components: {
    MyPanel,
    HomeVueSkeleton
  },
  methods:{
    toggleLike(e){
    // const cur = this
    if(e.isLiked === false){
        // TODO -> send axios request to like a item
        console.log(this)

        e.isLiked = true
        // this.map[e.id] = true
        this.map.set(e.id, true)
        // this.goods[e.id-1].isLiked = true
        console.log("like item")
        console.log(this)
        likeItem(e.id, this.username);
    }else{
        // TODO -> send axios request to unlike a item
        e.isLiked = false
        // this.map[e.id] = false
        this.map.set(e.id, false)
        // this.goods[e.id-1].isLiked = false
        console.log("unlike item")
      }
    }
  },
  setup(props) {
    // 鼠标进入显示
    const show = item => {
      item.open = true;
    };
    // 鼠标离开，点击二级菜单后隐藏
    const hide = item => {
      item.open = false;
    };
    const route = useRoute();
    const store = useStore();
    const goods = ref([]);
    const getResultList = async (keyword) => {
      try {
        const res = await getSearchResults(keyword);
        console.log(res);
        // if(status == 200)
        goods.value=res.slice(0,20);
        
      } catch (error) {
        console.log(error);
      }
    };
    getResultList(route.params.keyword);
    // console.log(typeof(goods)) // object
    // if(goods.length > 8) goods = goods.slice(0,8)
    console.log(goods)
    const username = computed(function() {
      return store.getters.email;
    });
    // const goods = defaultRecommend;
    return { show, hide, goods, username };
  }
};
</script>

<style lang="less" scoped>
.search-result{
  clear:left;
  padding: 10px 30px;
  .breadcrumb{
    padding: 10px 0;
  }
  .goods-list {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-bottom: 40px;
    .item {
      // display: list-item;
      // float:left; 
      // display: block;
      // white-space: nowrap;
      width: 265px;
      height: 365px;
      background-color: #f5f5f5;
      img {
        width: 265px;
        height: 265px;
      }
      // .hoverShadow();
      .title {
        font-size: 17px;
        text-align: center;
        padding: 15px 25px;
      }
      .price {
        text-align: center;
        font-size: 15px;
        color: @priceColor;
        del {
          color: #666;
        }
      }
    }
  }
}


</style>
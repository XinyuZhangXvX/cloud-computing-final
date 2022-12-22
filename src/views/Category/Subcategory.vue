

<template>
  <div class="category w">
    <!-- 1、面包屑 -->
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>{{category.name}}</el-breadcrumb-item>
        <el-breadcrumb-item>{{subcategory.name}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 2、轮播图 -->
    <!-- <AppBanner :list="banner" /> -->

    <!-- 3、分类展示 -->
    <!-- <div class="sub-list">
      <h3>全部分类</h3>
      <ul>
        <li v-for="item in category.subCateList" :key="item.id">
          <a href="##">
            <img :src="item.bannerUrl" alt />
            <div class="name">{{item.name}}</div>
          </a>
        </li>
      </ul>
    </div> -->

    <div >
      <MyPanel title="Results" subTitle="There are the results">
        <ul class="goods-list">
          <li class="item" v-for="item in goods" :key="item.id">
            <router-link to="/">
              <img :src="item.listPicUrl" />
              <div class="title ellipsis-2">{{item.name}}</div>
              <a style="float: right;">
                <i class="fa-solid fa-heart favorite-right" v-if="map.get(item.id)" @click="toggleLike(item)"></i>
                <i class="fa-regular fa-heart favorite-right" v-else @click="toggleLike(item)"></i>
              </a>
            </router-link>
          </li>
        </ul>
      </MyPanel>
    </div>
  </div>
</template>

<script>
import MyPanel from "@/components/MyPanel.vue";
import HomeVueSkeleton from '@/components/Skeleton/HomeVueSkeleton.vue'
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { getSubCate } from "@/api";
import {topCategory} from '@/utils/constants'
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

    // 获取仓库对象
    const store = useStore();
    // 获取路由导航对象
    const route = useRoute();
    // 查找跟路由中 id 相等的分类
    const category = computed(() => {
      let cate = {};
      const item = topCategory.find(item => {
        return item.id == route.params.id;
      });
      if (item) cate = item;
      return cate;
    });

    console.log(category)
    
    const subcategory = computed(() => {
      let cate = {};
      let subcat = {};
      const item = topCategory.find(item => {
        return item.id == route.params.id;
      });
      if (item) {
        cate = item;
        const sub = cate.subCateGroupList.find(item =>{
          return item.id == route.params.subid;
        });
        if(sub) subcat = sub;
        return sub;
      }
      return sub;
    });

    const goods = ref([]);
    const getSubCateList = async (catId, subCatId) => {
      try {
        const res = await getSubCate(catId, subCatId);
        console.log(res);
        // if(status == 200)
        goods.value=res;
        
      } catch (error) {
        console.log(error);
      }
    };
    getSubCateList(category.value.id, subcategory.value.id);
    console.log('goods is')
    console.log(goods)
    // const goods = defaultRecommend;

    return { category, subcategory, goods};
  }
};
</script>

<style lang="less" scoped>
.category {
  clear:left;
  padding: 15px 40px;
  .breadcrumb {
    padding: 20px 0;
  }
  .sub-list {
    margin-top: 20px;
    h3 {
      font-size: 32px;
      text-align: center;
      font-weight: normal;
      line-height: 100px;
    }
    ul {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      li {
        width: 140px;
        height: 160px;
        text-align: center;
        img {
          width: 100px;
          height: 100px;
          margin: 5px 0;
        }
        &:hover {
          .name {
            color: @xtxColor;
          }
        }
      }
    }
  }
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
</style>
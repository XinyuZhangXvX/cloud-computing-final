<template>
  <div class="search-result w">
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>My Favorite</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div >
      <MyPanel title="Favorites" subTitle="There are your favorite items">
        <ul class="goods-list">
          <li class="item" v-for="item in goods" :key="item.id">
            <router-link to="/">
              <img :src="item.listPicUrl" />
              <div class="title ellipsis-2">{{item.name}}</div>
              
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
import { defaultRecommend } from '@/utils/constants';
import { useStore } from "vuex";
import { computed } from "vue";
import { ref } from "vue";
import { getFavorite } from "@/api";
// import { getSearch } from "@/api";

export default {
  data(){
    return{
      map: [true, true, true, true,true, true, true, true],
      username: null  
    }
  },
  components: {
    MyPanel,
    HomeVueSkeleton
  },
  methods:{
  },
  setup(props) {
    // 鼠标进入显示
    const store = useStore();
    const goods = ref([]);
    const show = item => {
      item.open = true;
    };
    // 鼠标离开，点击二级菜单后隐藏
    const hide = item => {
      item.open = false;
    };
    const username = computed(function() {
      return store.getters.email;
    });
    console.log("Username is: "+username.value)
    const getFavoriteList = async (name) => {
      try {
        const res = await getFavorite(name);
        console.log(res);
        // if(status == 200)
        goods.value=res;
        
      } catch (error) {
        console.log(error);
      }
    };
    getFavoriteList(username.value);
    
    return { show, hide, goods };
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
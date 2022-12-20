<template>
  <div class="home-hot">
    <MyPanel title="Women Hot" subTitle="Hot women items">
      <!-- 使用默认插槽 -->
      <template #right>
        <AppMore path="/" />
      </template>
      <ul class="goods-list">
        <li class="item" v-for="item in goods" :key="item.id">
          <router-link to="/">
            <img :src="item.listPicUrl" />
            <div class="title ellipsis-2">{{item.name}}</div>
            <a style="float: right;">
              <i class="fa-solid fa-heart favorite-right" v-if="map[item.id]" @click="toggleLike(item)"></i>
              <i class="fa-regular fa-heart favorite-right" v-else @click="toggleLike(item)"></i>
            </a>
          </router-link>
        </li>
      </ul>
    </MyPanel>
  </div>
</template>

<script>
import MyPanel from "@/components/MyPanel.vue";
import HomeVueSkeleton from '@/components/Skeleton/HomeVueSkeleton.vue'
import { ref } from "vue";
import { getHot } from "@/api";
import { defaultWomen } from '@/utils/constants';
export default {
  data(){
    return{
      map: [false, false, false, false,false, false, false, false,],
      goods: defaultWomen
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
          this.map[e.id] = true
          // this.goods[e.id-1].isLiked = true
          console.log("like item")
          console.log(this)
      }else{
          // TODO -> send axios request to unlike a item
          e.isLiked = false
          this.map[e.id] = false
          // this.goods[e.id-1].isLiked = false
          console.log("unlike item")
      }
      }
  },
  setup(props) {
    const goods = ref([]);
    const getHotList = async () => {
      try {
        const res = await getHot();
        console.log(res);
        // if (res.msg == "操作成功") {
        goods.value=res.slice(0,8);
        // }
      } catch (error) {
        console.log(error);
      }
    };
    getHotList();
    console.log(goods)
    // const goods = defaultRecommend;
    return { goods };
  }
};
</script>

<style lang="less" scoped>
.home-hot {
	// clear:left;
  .goods-list {
    
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-bottom: 40px;
    .item {
      // display: list-item;
      float:left; 
      display: block;
      white-space: nowrap;
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
  .goods-list-old {
    display: flex;
    justify-content: space-between;
    margin-bottom: 40px;
    .item {
      width: 265px;
      height: 365px;
      background-color: #f5f5f5;
      img {
        width: 265px;
        height: 265px;
      }
      .hoverShadow();
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
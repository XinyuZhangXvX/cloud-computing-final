

<template>
  <div class="home-new">
    <MyPanel title="Recommend" subTitle="These items you might like: ">
      <!-- 使用右侧插槽 -->
      <template #right>
        <AppMore path="/" />
      </template>
      <!-- 使用默认插槽 -->
      <ul v-if="goods.length" class="goods-list">
        <li class="item" v-for="item in goods" :key="item.id">
          <img :src="item.listPicUrl" />
          <div class="title ellipsis">{{item.name}}</div>
          
          <a style="float: right;">
            <!-- <i class="fa-regular fa-heart favorite-right" v-if="!isLiked"></i> -->
            <!-- <i class="fa-solid fa-heart favorite-right" v-if="isLiked"></i> -->
            <!-- <i :class="item.isLiked===true? 'fa-solid fa-heart favorite-right': 'fa-regular fa-heart favorite-right'" @click="toggleLike(item)"></i> -->
            <i class="fa-solid fa-heart favorite-right" v-if="map.get(item.id)" @click="toggleLike(item)"></i>
            <i class="fa-regular fa-heart favorite-right" v-else @click="toggleLike(item)"></i>
          </a>
        </li>
      </ul>
      <!-- 骨架屏 -->
      <HomeVueSkeleton v-else/>

      <!-- <div v-else class="goods-list">
        <el-skeleton v-for="i in 4" :key="i" style="width: 265px">
          <template #template>
            <el-skeleton-item variant="image" style="width: 240px; height: 240px" />
            <div style="padding: 14px">
              <el-skeleton-item variant="p" style="width: 50%" />
              <div
                style="
            display: flex;
            align-items: center;
            justify-items: space-between;
          "
              >
                <el-skeleton-item variant="text" style="margin-right: 16px" />
                <el-skeleton-item variant="text" style="width: 30%" />
              </div>
            </div>
          </template>
        </el-skeleton>
      </div> -->
    </MyPanel>
  </div>
</template>

<script>
import { ref } from "vue";
import MyPanel from "@/components/MyPanel.vue";
import HomeVueSkeleton from '@/components/Skeleton/HomeVueSkeleton.vue'
import { defaultRecommend } from '@/utils/constants';
import { useStore } from "vuex";
import { computed } from "vue";
import { likeItem, getRecommend } from "@/api";
export default {
  data(){
    return{
      map: new Map(),
      goods: []
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
        console.log(e)

        e.isLiked = true
        // this.map[e.id] = true
        this.map.set(e.id, true)
        // this.goods[e.id-1].isLiked = true
        console.log("like item")
        console.log(e.id)
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
    const goods = ref([]);
    // const goods = defaultRecommend;
    const store = useStore();
    // const likemap = new Map();
    // for (let i = 0; i < goods.length; i++) {
    //   likemap.set(goods[i].id, goods[i].isLiked);
    // }
    const username = computed(function() {
      return store.getters.email;
    });

    console.log(this)
    // setMap(this.map, likemap)
    const getRcmdList = async (username) => {
      try {
        const res = await getRecommend(username);
        console.log(res);
        if ((res.code = "200")) {
          goods.value = res;
        }
      } catch (error) {
        console.log(error);
      }
    };
    console.log(username)
    console.log(username.value)
    getRcmdList(username.value);
    return { goods, username};
  }
};

</script>

<style lang="less" scoped>
.home-new {
  clear:left;
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
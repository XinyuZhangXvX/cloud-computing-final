<template>
  <div class="home w">
    <!-- 轮播图 -->
    <!-- <HomeBanner/> -->

    <!-- Recommend -->
    <HomeRcmd />
    <!-- Women -->
    <HomeWomen />
    <!-- Men -->
    <HomeMen />
    <!-- Kids -->
    <HomeKids />

    <!-- 产品区块 -->
    <HomeProduct />
    
  </div>
</template>

<script>
import HomeBanner from './HomeBanner.vue'
import HomeRcmd from './HomeRcmd.vue'
import HomeWomen from './HomeWomen.vue'
import HomeMen from './HomeMen.vue'
import HomeKids from './HomeKids.vue'
import HomeProduct from './HomeProduct.vue'
export default {
    components:{
        HomeBanner,
        HomeRcmd,
        HomeWomen,
        HomeMen,
        HomeKids,
        HomeProduct
    }
};
</script>

<style lang="less" scoped>
</style>
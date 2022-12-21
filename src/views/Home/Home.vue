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

    
  </div>
</template>

<script>
import HomeRcmd from './HomeRcmd.vue'
import HomeWomen from './HomeWomen.vue'
import HomeMen from './HomeMen.vue'
import HomeKids from './HomeKids.vue'
export default {
    components:{
        HomeRcmd,
        HomeWomen,
        HomeMen,
        HomeKids,
    }
};
</script>

<style lang="less" scoped>
</style>
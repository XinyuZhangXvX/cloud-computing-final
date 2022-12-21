

<template>
  <div class="category w">
    <!-- 1、面包屑 -->
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>{{category.name}}</el-breadcrumb-item>
      </el-breadcrumb>
    </div>
    <!-- 2、轮播图 -->
    <!-- <AppBanner :list="banner" /> -->

    <!-- 3、分类展示 -->
    <div class="sub-list">
      <h3>All Categories</h3>
      <ul>
        <li v-for="item in category.subCateGroupList" :key="item.id">
          <a href="##">
            <!-- <img :src="item.bannerUrl" alt /> -->
            <div class="name">{{item.name}}</div>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { ref, computed } from "vue";
import { useStore } from "vuex";
import { useRoute } from "vue-router";
import { getBanner } from "@/api";
import {topCategory} from '@/utils/constants'
export default {
  setup(props) {
    // 轮播图
    const banner = ref([]);
    // getBanner()
    //   .then(res => {
    //     if (res.msg == "操作成功") {
    //       banner.value = res.result;
    //     }
    //   })
    //   .catch(err => {
    //     console.log(err);
    //   });

    // 获取仓库对象
    const store = useStore();
    // 获取路由导航对象
    const route = useRoute();
    // 查找跟路由中 id 相等的分类
    console.log(topCategory)
    const category = computed(() => {
      let cate = {};
      const item = topCategory.find(item => {
        return item.id == route.params.id;
      });
      if (item) cate = item;
      return cate;
    });
    console.log(category.value);
    return { banner, category };
  }
};
</script>

<style lang="less" scoped>
.category {
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
        height: 40px;
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
</style>
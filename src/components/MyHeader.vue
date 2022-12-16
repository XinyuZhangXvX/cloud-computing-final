<template>
  <div class="my-header w">
    <!-- 上面区域 -->
    <div class="header-top">
      <!-- logo -->
      <a class="logo" href="/"><img src='../assets/images/ifashion-logo.png' width="380"></a>
      
      <!-- <h1>
        <p>ifashion</p>
        <router-link to="/"></router-link>
        
      </h1> -->
      <!-- 搜索-->
      <div class="center">
        <div class="center-search">
          <input type="text" name id placeholder="women tops" v-model="keyword"/>
          
          <RouterLink class="link" :to="'/search/'+keyword"><button class="search-btn" @click="search">Search</button></RouterLink>
        </div>
        
      </div>
      <!-- 购物车 -->
      <div class="cart">
        <a href="##">
          Qustionnaire
        </a>
      </div>
    </div>

    <!-- 二级导航 -->
    <AppHeaderNav />
    <!-- Test -->
    <!-- <div>
      <RouterLink class="link" :to="'/search/test'" @click="hide(item)">Test Search</RouterLink>
    </div> -->
  </div>
</template>

<script>
import AppHeaderNav from "./AppHeaderNav.vue";
import { useStore } from "vuex";
export default {
  data(){
    return {
      keyword: ""
    }
  },
  components: {
    AppHeaderNav
  },
  methods:{
  	search(){
      console.log(this.keyword)
    }
  },
  setup(props) {
    const store = useStore();
    // 触发action
    store.dispatch('category/getAllCategory');
  }
};
</script>

<style lang="less" scoped>
.my-header {
  height: 120px;
  padding: 25px 0 0 0;
  background-color: #fff;
  .header-top {
    display: flex;
    .logo {
      width: 400px;
      height: 80px;
      // a {
      //   display: inline-block;
      //   height: 60px;
      //   width: 100%;
      // }
    }
    .center {
      flex: 1;
      .center-search {
        width: 540px;
        height: 50px;
        input {
          width: 440px;
          height: 50px;
          border: 1px solid @xtxColor;
          border-radius: 20px 0 0 20px;
          padding-left: 15px;
          box-sizing: border-box;
        }
        .search-btn {
          float: right;
          width: 100px;
          height: 50px;
          color: #fff;
          background-color: @xtxColor;
          border-radius: 0 20px 20px 0;
          border: 0;
          font-size: 16px;
          cursor: pointer;
        }
      }
      .center-navs {
        width: 540px;
        li {
          float: left;
          height: 32px;
          padding: 5px;
          a {
            padding: 0 5px;
            border-right: 1px solid #ccc;
            &:hover {
              color: @xtxColor;
            }
          }
        }
        li:last-child a {
          border-right: 0;
        }
      }
    }
    .cart {
      box-sizing: border-box;
      width: 150px;
      height: 50px;
      border-left: 20px;
      line-height: 45px;
      border-radius: 20px;
      border: 2px solid @xtxColor;
      font-size: 15px;
      text-align: center;

      &:hover {
        background-color: #f5f3ef;
      }
      a {
        color: @xtxColor;
      }
      i {
        // font-size: 16px;
        color: @xtxColor;
      }
      em {
        color: #fff;
        background-color: red;
        border-radius: 50%;
        padding: 5px;
        display: inline-block;
        width: 11px;
        height: 9px;
        line-height: 10px;
        font-size: 10px;
        // padding: 2px 5px;
      }
    }
  }
}
</style>
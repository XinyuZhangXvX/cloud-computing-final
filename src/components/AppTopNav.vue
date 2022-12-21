<template>
  <div class="app-top-nav">
    <div class="w">
      <ul>
        <template v-if="isAuthenticated">
          <li>
            <a href="javascript:;">Hi</a>
          </li>
          <li>
            <a href="javascript:;">Logout</a>
            <!-- <RouterLink class="link" :to="'/signin'">Logout</RouterLink> -->
          </li>
        </template>
        <li v-else>
          <!-- <a href="javascript:;">Login</a> -->
          <RouterLink class="link" :to="'/signin'">Login</RouterLink>
        </li>
        <li>
          <a href="javascript:;">My Favorite</a>
        </li>
        <li>
          <a href="javascript:;">Contact</a>
        </li>
        <li>
          <a href="javascript:;">Help</a>
        </li>
        <li>
          <a href="javascript:;">
            <i class="iconfont icon-phone"></i>
            APP
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { useStore } from "vuex";
import { computed } from "vue";
export default {
  setup(props) {
    const store = useStore();
    // console.log(store.state);
    // let userinfo = computed(() => {
    //   return {
    //     // token: 111,
    //     // username: "abc"
    //   }
    // });
    const isAuthenticated = computed(function() {
      return store.getters.isAuthenticated;
    });

    return { isAuthenticated };
  }
};
</script>

<style lang="less" scoped>
// @import url('../assets/styles/variables.less');
.app-top-nav {
  background-color: #35185A;
  ul {
    display: flex;
    height: 40px;
    line-height: 40px;
    justify-content: flex-end;
    li {
      a {
        font-size: 12px;
        padding: 0 15px;
        color: #ccc;
        border-left: 1px solid #ccc;

        &:hover {
          color: @xtxColor;
        }
      }
    }
    li:nth-child(1) {
      a {
        border-left: 0;
      }
    }
  }
}
</style>
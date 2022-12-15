<template>
  <div class="app-top-nav">
    <div class="w">
      <ul>
        <template v-if="userinfo.token">
          <li>
            <a href="javascript:;">Hi {{userinfo.username}}</a>
          </li>
          <li>
            <a href="javascript:;">Logout</a>
          </li>
        </template>
        <li v-else>
          <a href="javascript:;">Login</a>
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
    let userinfo = computed(() => {
      return store.state.user.userinfo;
    });

    return { userinfo };
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
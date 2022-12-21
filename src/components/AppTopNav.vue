<template>
  <div class="app-top-nav">
    <div class="w">
      <ul>
        <template v-if="isAuthenticated">
          <li>
            <a href="javascript:;">Hi</a>
          </li>
          <li>
            <RouterLink class="link" :to="'/'" @click.prevent="logout">Logout</RouterLink>
          </li>
        </template>
        <li v-else>
          <!-- <a href="javascript:;">Login</a> -->
          <RouterLink class="link" :to="'/signin'">Login</RouterLink>
        </li>
        <li>
          <RouterLink class="link" :to="'/favorite'">
            My Favorite
          </RouterLink>
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
import { useRouter } from "vue-router";

export default {
  setup(props) {
    const store = useStore();
    const router = useRouter();
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

    async function logout() {
      store.dispatch("logout");

      router.push({
        name: "SignIn",
        params: { message: "You have logged out" },
      });
    }

    return { logout, isAuthenticated };
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
<template>
  <div class="search-result w" v-if="!isSubmitted">
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>Questionnaire</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div >
      <MyPanel title="Questionnaire" subTitle="Please fill in the following questions">
        <ul class="question-list">
          <li>
            <h5> Question 1: </h5>
            <p> Please what kind of clothes you want to look for:</p>
            <form action="">
              <input type="radio" name="sex" value="female" v-model="sexChecked">Female<br/>
              <input type="radio" name="sex" value="male" v-model="sexChecked">Male<br/>
              <input type="radio" name="sex" value="kids" v-model="sexChecked">Kids
            </form>
          </li>
          <li>
            <h5> Question 2: </h5>
            <p> Please choose all the colors you like below:</p>
            <form class="color-form">
                <input type="checkbox" name="color" v-model="checkedColors" value="Beige">Beige<span class="color-display" style="background-color: beige; color: beige;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Black">Black<span class="color-display" style="background-color: black; color: black;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Blue">Blue<span class="color-display" style="background-color: blue; color: blue;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Bluish Green">Bluish Green<span class="color-display" style="background-color: #008080; color: #008080;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Brown">Brown<span class="color-display" style="background-color: #8B4513 ; color: #8B4513 ;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Green">Green<span class="color-display" style="background-color: green; color: green;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Grey">Grey<span class="color-display" style="background-color: gray; color: gray;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Khaki green">Khaki green<span class="color-display" style="background-color: #8A865D; color: #8A865D;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Lilac Purple">Lilac Purple<span class="color-display" style="background-color: #c8a2c8; color: #c8a2c8;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Mole">Mole<span class="color-display" style="background-color: #392d2b; color: #392d2b;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Orange">Orange<span class="color-display" style="background-color: orange; color: orange;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Pink">Pink<span class="color-display" style="background-color: pink; color: pink;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Red">Red<span class="color-display" style="background-color: red; color: red;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Turquoise">Turquoise<span class="color-display" style="background-color: turquoise; color: turquoise;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="White">White<span class="color-display" style="background-color: white; color: white;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Yellow">Yellow<span class="color-display" style="background-color: yellow; color: yellow;">......</span><br/>
                <input type="checkbox" name="color" v-model="checkedColors" value="Yellowish Green">Yellowish Green<span class="color-display" style="background-color: #9ACD32; color: #9ACD32;">......</span><br/>
                
            </form>
          </li>

          <li>
            <h5> Question 3: </h5>
            <p> Please choose the patterns you like:</p>
            <form action="">
              <!-- <input type="checkbox" name="pattern" :value="item.name">Female<br/> -->
              <ul class="pattern-list">
                <li class="item" v-for="item in patterns" :key="item.id">
                  <img :src="item.listPicUrl"/>
                  <div class="title ellipsis-2">
                    <input type="checkbox" name="pattern" :value="item.name" v-model="checkedPatterns">{{item.name}}<br/>
                  </div>
                </li>
              </ul>
            </form>
          </li>

          <li>
            <h5> Question 4: </h5>
            <p> Please choose the textures you like:</p>
            <form action="">
              <ul class="texture-list">
                <li class="item" v-for="item in textures" :key="item.id">
                  <img :src="item.listPicUrl"/>
                  <div class="title ellipsis-2">
                    <input type="checkbox" name="texture" :value="item.name" v-model="checkedTextures">{{item.name}}<br/>
                  </div>
                </li>
              </ul>
              
            </form>
          </li>
          <li>
            <button class="search-btn" @click="submit">Submit</button>
          </li>
        </ul>
        <!-- <p>选择的sex: {{ sexChecked }}</p>
        <p>选择的pattern: {{ checkedPatterns }}</p>
        <p>选择的textures: {{ checkedTextures }}</p>
        <p>选择的colors: {{ checkedColors }}</p> -->
        
      </MyPanel>
    </div>
  </div>
  

  <div class="search-result w" v-if="isSubmitted">
    <div class="breadcrumb">
      <el-breadcrumb separator="/">
        <el-breadcrumb-item to="/">Home</el-breadcrumb-item>
        <el-breadcrumb-item>Recommend</el-breadcrumb-item>
      </el-breadcrumb>
    </div>

    <div >
      <MyPanel title="Recommendations" subTitle="These items you might like">
        <ul class="goods-list">
          <li class="item" v-for="item in goods" :key="item.id">
            <img :src="item.listPicUrl" />
            <div class="title ellipsis-2">{{item.name}}</div>
            <a style="float: right;">
              <i class="fa-solid fa-heart favorite-right" v-if="map.get(item.id)" @click="toggleLike(item)"></i>
              <i class="fa-regular fa-heart favorite-right" v-else @click="toggleLike(item)"></i>
            </a>
          </li>
        </ul>
      </MyPanel>
    </div>
  </div>
  

</template>

<script>
import MyPanel from "@/components/MyPanel.vue";
import HomeVueSkeleton from '@/components/Skeleton/HomeVueSkeleton.vue'
import { patternSamples, textureSamples } from '@/utils/constants';
import { defaultRecommend } from '@/utils/constants';
import { postQuestionnaire } from "@/api";
import { likeItem } from "@/api";
import { useStore } from "vuex";
import { ref, computed } from "vue";
// import { getSearch } from "@/api";

export default {
  data(){
    return{
      map: new Map(),
      sexChecked: "female",
      checkedTextures: [],
      checkedPatterns: [],
      checkedColors: [],
      isSubmitted: false,
      goods: defaultRecommend
    }
  },
  components: {
    MyPanel,
    HomeVueSkeleton
  },
  methods:{
    submit(){
      console.log("Choose sex: " + this.sexChecked);
      console.log("Choose colors: " + this.checkedColors);
      console.log("Choose patterns: " + this.checkedPatterns);
      console.log("Choose textures: " + this.checkedTextures);
      // const goods = ref([]);
      var params = {
        sex: this.sexChecked,
        colors: this.checkedColors,
        patterns: this.checkedPatterns,
        textures: this.checkedTextures
      }
      const getRcmdList = async (params) => {
        try {
          var res = await postQuestionnaire(params);
          console.log(res);
          // if(status == 200)
          this.goods=res;
          // this.goods.push(res)
          return res;
          
        } catch (error) {
          console.log(error);
        }
      };
      var res = getRcmdList(params);
      this.isSubmitted = true
      // console.log(res)
      console.log(this.goods)

    },
    toggleLike(e){
    // const cur = this
    if(e.isLiked === false){
        // TODO -> send axios request to like a item
        console.log(this)

        e.isLiked = true
        // this.map[e.id] = true
        this.map.set(e.id, true)
        // this.goods[e.id-1].isLiked = true
        console.log("like item")
        console.log(this)
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
    const patterns = patternSamples;
    const textures = textureSamples;
    const store = useStore();
    const username = computed(function() {
      return store.getters.email;
    });
    return { patterns, textures, username };
  }
}
</script>

<style lang="less" scoped>
.search-result{
  clear:left;
  padding: 10px 30px;
  .breadcrumb{
    padding: 10px 0;
  }
  .question-list {
    // display: flex;
    // flex-wrap: wrap;
    // justify-content: space-between;
    // margin-bottom: 40px;
    li{
        padding: 15px 25px;
        input{
          margin: 10px;
        }
      }
    .color-form{
      .color-display {
        margin: 15px;
        height: 40px;
        width: 40px;
        border: 1px solid #919191;
        border-radius: 20px 20px 20px 20px;
        box-sizing: border-box;
      }
    }
      
    .pattern-list {
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
        // background-color: #f5f5f5;
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
      }
    }
    .texture-list {
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
        // background-color: #f5f5f5;
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
      }
    }
    .search-btn {
      width: 100px;
      height: 50px;
      color: #fff;
      background-color: @xtxColor;
      border-radius: 20px 20px 20px 20px;
      border: 0;
      font-size: 16px;
      cursor: pointer;
    }
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
    }
  }
  
}



</style>
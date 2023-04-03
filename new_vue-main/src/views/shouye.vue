<template>
  <div>
    <a-row :gutter="24">
      <a-col :span="leftwidth">
        <a-card style="height: 650px;" class="second-line mb-24">
          <template #title>
            <h6>实时热点推特</h6>
            <p>点击可查看详细信息</p>
          </template>
          <a-carousel autoplay dot-position="right" :autoplay-speed=10>
            <a-row :gutter="24">
              <div v-infinite-scroll="handleInfiniteOnLoad" class="demo-infinite-container"
                :infinite-scroll-disabled="busy" :infinite-scroll-distance="10">
                <a-list :data-source="data">
                  <a-list-item v-on:click="clickTweet(item)" slot="renderItem" slot-scope="item">
                    <a-list-item-meta :description="item.create_time">
                      <a slot="title">{{ item.user_name }}</a>
                      <a-avatar slot="avatar" :src="url" />
                    </a-list-item-meta>
                    {{ item.tweet_text }}
                  </a-list-item>

                  <div v-if="loading && !busy" class="demo-loading-container">
                    <a-spin />
                  </div>
                </a-list>
              </div>
            </a-row>
          </a-carousel>
        </a-card>
      </a-col>
      <a-col :span="rightwidth">
        <a-card v-if="!this.image" style="height: 650px;" class="second-line mb-24">
          <template #title>
            <h6>推特详细信息</h6>
            <p>推特正文及谣言判定结果</p>
          </template>
          <a-row style="height: 100px; margin-left:20px; margin-top: 20px;" :gutter="24">
            <a-col :span="4">
              <a-avatar :src="url" />
            </a-col>
            <a-col :span="20">
              <span style="margin-left: -65px; position: relative; top: 0px;"> <b style="font-size: 20px;"> {{
                this.tweet_info.user_name }} </b> </span>
            </a-col>
          </a-row>
          <a-row style="height: 100px; margin-left:25px; margin-top: -50px;">
            <a-col :span="3">
              <a-icon style="font-size: 25px; color:#82C5EA" type="user-add" /></a-col>
            <a-col :span="6">
              <span style="font-family: SimSun; font-size: 16px; position: relative; right: 45px;">粉丝数:{{
                this.tweet_info.user_followers_count }}</span>
            </a-col>
            <a-col :span="3">
              <a-icon style="font-size: 25px; color:#82C5EA" type="usergroup-delete" />
            </a-col>
            <a-col :span="6">
              <span style="font-family: SimSun; font-size: 16px; position: relative; right: 45px;">好友数:{{
                this.tweet_info.user_friends_count }}</span>
            </a-col>
            <a-col :span="12"></a-col>
          </a-row>
          <a-row>
            <a-col :span="20">
              <span style="font-family: SimSun; font-size: 16px; position: relative; right: -30px; bottom: 50px;">
                {{ this.tweet_info.tweet_text }}
              </span>
            </a-col>
          </a-row>
          <a-row v-if="rumor_image" :gutter="24">
            <a-col :span="7"></a-col>
            <a-col :span="12">
              <el-image style="width: 260px; height: 260px; margin-top: -40px;" :src="this.tweet_info.images_url"
                fit="contain"></el-image>
            </a-col>
          </a-row>
          <a-row style="height: 100px; margin-left:25px; margin-top: -50px;">
            <a-col :span="3">
              <a-icon style="font-size: 25px; color:#82C5EA" type="share-alt" /></a-col>
            <a-col :span="3">
              <span style="font-family: SimSun; font-size: 16px; position: relative; right: 45px;">转发:{{
                this.tweet_info.retweet_count }}</span>
            </a-col>
            <a-col :span="12"></a-col>
          </a-row>

          <a-row>
            <a-col :span="10">

            </a-col>
            <a-col>
              <a-button type="primary" icon="search" :loading="iconLoading" @click="clickButton">
                真实性分析
              </a-button>
            </a-col>

          </a-row><a-icon type="" />

        </a-card>
        <el-image v-if="this.image" style="margin-left:-100px; margin-top:-100px; width: 700px; height: 700px"
          :src="rumor" fit="contain"></el-image>
      </a-col>
    </a-row>


    <!-- 接下来是模型调用和判定结果部分 -->

    <a-row v-if="this.showAnaylize" :gutter="24">
      <a-card style="height: 500px;" class="second-line mb-24">
        <template #title>
          <h6>谣言判定结果</h6>
          <p>可信度分析</p>
        </template>
        <a-row style="height: 30px"></a-row>
        <a-row style="height:50px">
          <a-col :span="1"></a-col>
          <a-col :span="7">
            <h6>谣言判定结果:</h6>
          </a-col>
          <a-col :span="1"></a-col>
          <a-col :span="7">
            <h6>威胁程度分析：</h6>
          </a-col>

        </a-row>
        <a-row style="height:100px">
          <a-col :span="10">
            <chart />
          </a-col>
          <a-col :span="1"></a-col>
          <a-col :span="11">
            <radar />
          </a-col>
        </a-row>

      </a-card>
    </a-row>

  </div>
</template>

<script>
// import tweets from "../components/rumor_killer_com/tweets.vue";
import rumor_killer from "../assets/img/rumor_killer.png";
import tweetURL from "../assets/img/tweet.png"
import infiniteScroll from "vue-infinite-scroll";
import chart from "../components/rumor_killer_com/rumor_bar.vue"
import pie from "../components/rumor_killer_com/rumor_pie.vue"
import radar from "../components/rumor_killer_com/rumor_radar.vue"

export default {
  components: {
    // tweets,
    chart,
    pie,
    radar
  },
  directives: { infiniteScroll },
  data() {
    return {
      chartData: [10, 20, 30, 40],
      showAnaylize: false,
      data: [],
      image: true,
      rumor: rumor_killer,
      data: [],
      url: tweetURL,
      loading: false,
      busy: false,
      leftwidth: 12,
      rightwidth: 12,
      tweet_info: {},
      rumor_image: false,
      iconLoading: false,
    };
  },
  beforeMount() {
    this.fetchData();
  },
  methods: {
    async fetchData(callback) {
      await this.axios
        .post("http://localhost:5000/tweets/getTrendingTweets")
        .then(response => {
          // this.data = data
          console.log(response);
          for (var i = 0; i < 10; i++) {
            this.data.push(response.data[i]);
          }
        })
        .catch(error => {
          console.log(error);
        });
    },

    clickTweet(item) {
      this.image = false;
      this.leftwidth = 10;
      this.rightwidth = 14;
      this.tweet_info = item;
      if (this.tweet_info.images_url == "") {
        this.rumor_image = false;
      } else {
        this.rumor_image = true;
        this.tweet_info.images_url = this.tweet_info.images_url.split(",")[0];
      }

    },

    handleInfiniteOnLoad() {
      const data = this.data;
      this.loading = true;
      if (data.length > 500) {
        this.$message.warning("没有更多了~");
        this.busy = true;
        this.loading = false;
        return;
      }
      this.fetchData((res) => {
        this.loading = false;
      });
    },


    async clickButton() {
      this.iconLoading = true;

      await this.axios
        .post("http://localhost:5000/tweets/getTrendingTweets")
        .then(response => {
          // this.data = data
          console.log(response);
          for (var i = 0; i < 10; i++) {
            this.data.push(response.data[i]);
          }
        })
        .catch(error => {
          console.log(error);
        });

      setTimeout(() => {
        this.iconLoading = false;
        this.showAnaylize = true; 
      }, 2500);

      const ctx = document.getElementById('myChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['非谣言', '谣言'],
          datasets: [{
            label: 'My Dataset',
            data: this.chartData,
            backgroundColor: ['#add8e6', '#1e90ff'],
          }]
        }
      });
    }

  },
};
</script>

<style scoped lang="scss">
.second-line {
  height: 278px;
}

.demo-infinite-container {
  /* border: 1px solid #e8e8e8; */
  /* border-radius: 4px; */
  overflow: auto;
  padding: 8px 24px;
  height: 550px;
}

.demo-loading-container {
  position: absolute;
  bottom: 40px;
  width: 100%;
  text-align: center;
}
</style>

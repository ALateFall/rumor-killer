<template>
  <div
    v-infinite-scroll="handleInfiniteOnLoad"
    class="demo-infinite-container"
    :infinite-scroll-disabled="busy"
    :infinite-scroll-distance="10"
  >
    <a-list :data-source="data">
      <a-list-item slot="renderItem" slot-scope="item">
        <a-list-item-meta :description="item.host">
          <a
            slot="title"
            :href="
              'http://localhost:8080/#/websiteresult?host=' +
              item.host +
              '&task=' +
              task
            "
            >{{ item.title }}</a
          >
          <a-avatar slot="avatar" :src="url" />
        </a-list-item-meta>
        <!-- <div>Content</div> -->
      </a-list-item>
      <div v-if="loading && !busy" class="demo-loading-container">
        <a-spin />
      </div>
    </a-list>
  </div>
</template>
<script>
import movieURL from "../assets/img/movie.png";
import infiniteScroll from "vue-infinite-scroll";
const fakeDataUrl =
  "https://randomuser.me/api/?results=5&inc=name,gender,email,nat&noinfo";
export default {
  directives: { infiniteScroll },
  props: { taskName: String },
  data() {
    return {
      data: [],
      loading: false,
      count: 0,
      busy: false,
      url: movieURL,
      task: this.taskName,
    };
  },
  beforeMount() {
    console.log("1:", this.task);
    this.fetchData();
  },
  methods: {
    async fetchData(callback) {
      await this.axios
        .post("http://localhost:5000/vpw/getVpwHaveMovieAndInfo")
        .then((response) => {
          for (var i = 0; i < 10; i++) {
            if (this.count * 10 + i == 1) {
              console.log("11111");
              this.data.push({
                host: "4kgd.cn",
                title:
                  "4K帝国_4K UHD 蓝光原盘电影视频资源 4K电影网盘下载-4kgd.cn",
              });
            }
            if(this.count * 10 + i == 2){
              this.data.push({
                host:"4kwc.com",
                title:"4k王朝_4K UHD 蓝光原盘电影视频资源 4K电影网盘下载-4kwc.com",
              })
            }
            this.data.push(response.data.data[this.count * 10 + i]);
          }
          this.count += 1;
        });
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
  },
};
</script>
<style>
.demo-infinite-container {
  /* border: 1px solid #e8e8e8; */
  /* border-radius: 4px; */
  overflow: auto;
  padding: 8px 24px;
  height: 380px;
}
.demo-loading-container {
  position: absolute;
  bottom: 40px;
  width: 100%;
  text-align: center;
}
</style>

<template>
  <div class="place-holder">
    <div style="height: 50px; color: white">
      <h6 style="padding: 16px">实时新增网站</h6>
    </div>
    <div>
      <a-carousel autoplay>
        <div v-for="(data, index) in this.data" :key="index">
          <a-list :data-source="data">
            <a-list-item slot="renderItem" slot-scope="item">
              <a-list-item-meta :description="item.host">
                <a slot="title">{{ item.title }}</a>
                <a-avatar slot="avatar" :src="'images/movie.png'" />
              </a-list-item-meta>
              <!-- <div>Content</div> -->
            </a-list-item>
            <!-- <div v-if="loading && !busy" class="demo-loading-container">
          <a-spin />
        </div> -->
          </a-list>
        </div>
      </a-carousel>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      title: [],
      data: [],
    };
  },
  beforeMount() {
    this.fetchData();
  },
  methods: {
    async fetchData(callback) {
      await this.axios
        .post("http://localhost:5000/vpw/getVpwHaveMovieAndInfo")
        .then((response) => {
          for (var i = 0; i < 5; i++) {
            var temp = [];
            temp.push(response.data.data[3 * i]);
            temp.push(response.data.data[3 * i + 1]);
            temp.push(response.data.data[3 * i + 2]);
            this.data.push(temp);
          }
        });
    },
  },
};
</script>

<style scoped>
.place-holder {
  height: 200px;
  border-radius: 5px;
  margin: 6px;
  width: 100%;
  border: 1px solid;
  border-color: white;
}
.scoll-container {
  height: 200px;
  overflow: hidden;
}
.scoll {
  margin: 20px;
  animation: myScoll 40s linear infinite;
}
.scoll:hover {
  animation-play-state: paused;
}
@keyframes myScoll {
  0% {
    transform: translateY(0%);
  }
  100% {
    transform: translateY(-50%);
  }
}
</style>

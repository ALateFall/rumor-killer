<template>
  <div>
    <a-row class="mb-24">
      <a-col :span="24">
        <a-card style="height: 70px; padding: 16px">
          <div
            style="font-weight: bold; font-size: 15px; display: inline-block"
          >
            当前任务：
          </div>
          <div style="display: inline-block">
            <a-cascader
              v-if="this.flag"
              :options="this.selectData"
              style="width: 250px"
              :default-value="[this.task, this.host]"
              @change="onChange"
            />
          </div>
          <div style="float: right; margin-top: 8px">
            <div
              style="
                font-weight: bold;
                font-size: 15px;
                display: inline-block;
                margin-right: 4px;
              "
            >
              显示所有信息
            </div>
            <a-switch default-checked />
          </div>
        </a-card>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col :span="10">
        <div v-if="this.websiteFlag == 0" style="text-align: center">
          <a-card
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
            style="height: 305px"
          >
            <div style="height: 140px"></div>
            <a-spin />
          </a-card>
        </div>
        <div v-if="this.websiteFlag">
          <a-card
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
            style="height: 320px"
          >
            <template #title>
              <h6>侵权网站信息概述</h6>
              <!-- <p>今日爬虫运行数量 <span class="text-danger">-1</span></p> -->
            </template>
            <a-descriptions :column="1" bordered>
              <a-descriptions-item label="网站标题"
                >{{ this.websiteData.title }}
              </a-descriptions-item>
              <a-descriptions-item label="Domain">
                {{ this.websiteData.domain }}
              </a-descriptions-item>
              <a-descriptions-item label="IP地址">
                <a-tag color="orange"> {{ this.websiteData.ip }} </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="地理位置">
                <a-tag color="blue"> {{ this.websiteData.location }} </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="探测时间">
                <a-tag color="green"> {{ this.websiteData.detectTime }} </a-tag>
              </a-descriptions-item>
            </a-descriptions>
          </a-card>
        </div>
        <a-card
          style="height: 320px"
          :bordered="false"
          class="dashboard-bar-line header-solid mb-24"
        >
          <template #title>
            <h6>网页词云展示</h6>
          </template>
          <el-image
            :src="this.cloud"
            :preview-src-list="[this.cloud]"
          ></el-image>
        </a-card>
      </a-col>
      <a-col :span="14">
        <a-card style="height: 664px">
          <neo-vis-test :site="this.neoflag"></neo-vis-test>
        </a-card>
      </a-col>
    </a-row>
    <a-row :gutter="24" class="mb-24">
      <a-col :span="12">
        <div v-if="this.imageFlag == 0" style="text-align: center">
          <a-card
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
            style="height: 680px"
          >
            <div style="height: 320px"></div>
            <a-spin />
          </a-card>
        </div>
        <div v-if="this.imageFlag">
          <a-card
            style="height: 680px"
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
          >
            <template #title>
              <h6>网页取证</h6>
              <p>已添加盲水印</p>
            </template>
            <el-image
              :src="this.image"
              :preview-src-list="[this.image]"
            ></el-image>
          </a-card>
        </div>
      </a-col>
      <a-col :span="12">
        <div v-if="this.infoFlag == 0">
          <a-card
            style="height: 680px; text-align: center"
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
          >
            <div style="height: 320px"></div>
            <a-spin></a-spin>
          </a-card>
        </div>
        <div v-if="this.infoFlag">
          <a-card
            style="height: 680px"
            :bordered="false"
            class="dashboard-bar-line header-solid mb-24"
          >
            <template #title>
              <h6>溯源信息</h6>
              <p>侵权网站溯源信息展示</p>
            </template>
            <a-descriptions :column="1" bordered>
              <a-descriptions-item label="服务器软件"
                ><div v-html="this.websiteData.app"></div>
              </a-descriptions-item>
              <a-descriptions-item label="网站描述">
                {{ this.websiteData.desccription }}
              </a-descriptions-item>
              <a-descriptions-item label="运营人员邮箱">
                <a-tag color="orange"> {{ this.websiteData.email }} </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="运营人员姓名">
                {{ this.websiteData.registrant }}
              </a-descriptions-item>
              <a-descriptions-item label="运营公司名称">
                {{ this.websiteData.registrar }}
              </a-descriptions-item>
              <a-descriptions-item label="友情链接">
                <a-tag color="blue"> {{ this.websiteData.friend_link }} </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="关键词">
                {{ this.websiteData.keywords }}
              </a-descriptions-item>
              <a-descriptions-item label="服务器">
                <a-tag color="green"> {{ this.websiteData.server }} </a-tag>
              </a-descriptions-item>
              <a-descriptions-item label="侵权电影">
                <div class="container">
                  <div :class="this.isScoll">
                    <!-- <div class="scoll"> -->
                    <div v-for="movie in this.movies1" :key="movie">
                      <div>{{ movie }}</div>
                    </div>
                  </div>
                </div>
              </a-descriptions-item>
            </a-descriptions>
          </a-card>
        </div>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import NeoVisTest from "../components/NeoVisTest.vue";
export default {
  components: {
    NeoVisTest,
  },
  data() {
    return {
      selectData: [],
      websiteData: [],
      task: "",
      host: "",
      flag: false,
      websiteFlag: false,
      imageFlag: false,
      infoFlag: false,
      movies1: [],
      movies2: [],
      isScoll: true,
      neoflag: 1,
    };
  },

  beforeMount() {
    this.getSelectData();
    this.getWebsiteData();
    this.getImage();
    this.getMovies1();
    this.getMovies2();

    setInterval(() => {
      this.isScoll = "scoll";
      setTimeout(() => {
        var t = this.movies1.shift();
        this.movies1.push(t);
        this.isScoll = "";
      }, 850);
    }, 1700);
  },

  methods: {
    onChange(value) {
      this.task = value[0];
      this.host = value[1];
      this.getWebsiteData();
      this.getImage();
      this.changeNeo();
    },
    changeNeo() {
      if (this.neoflag == 1) {
        this.neoflag = 2;
      } else if (this.neoflag == 2) {
        this.neoflag = 1;
      }
    },
    ifMovieNotInArray(movie, array) {
      for (var i = 0; i < array.length; i++) {
        if (array[i].toString().search(movie) != -1) {
          return false;
        }
      }
      return true;
    },

    getMovies1() {
      this.movies1 = [""];
      // console.log("here", this.movies1);
      this.axios
        .post("http://localhost:5000/movie/getMovieInPage", {
          start: 0,
          count: 200,
          site: "zywlyy.cn",
        })
        .then((response) => {
          var pattern = "《(.*?)》";
          // console.log("r", response);
          for (var i = 0; i < response.data.data.length; i++) {
            var result = response.data.data[i].name.match(pattern);
            // console.log("result:", result);
            if (result != null) {
              if (
                this.ifMovieNotInArray(result[1].split(" ")[0], this.movies1)
              ) {
                this.movies1.push(result[1].split(" ")[0]);
              }
            }
          }
        });
    },

    getMovies2() {},

    getImage() {
      this.imageFlag = false;
      var image = "";
      if (typeof this.host == "undefined") {
        image = "4kgd.cn";
      } else {
        image = this.host;
      }
      this.image =
        "http://localhost:5000/apiRequestSender/query/getScreenshot?domain=" +
        image;
      this.imageFlag = true;
      this.cloud =
        "http://localhost:5000/apiRequestSender/query/getWordCloud?domain=" +
        image;
    },

    getSelectData() {
      this.task = this.$route.query.task;
      this.host = this.$route.query.host;
      // console.log(refererCode);
      var temp = [
        {
          value: "00ysw.com",
          label: "00ysw.com",
        },
        {
          value: "4kgd.cn",
          label: "4kgd.cn",
        },
        {
          value: "1080p.site",
          label: "1080p.site",
        },
        {
          value: "4kwc.com",
          label: "4kwc.com",
        },
        {
          value: "115fhd.com",
          label: "115fhd.com",
        },
        {
          value: "154.92.22.154",
          label: "154.92.22.154",
        },
        {
          value: "185.149.23.238",
          label: "185.149.23.238",
        },
        {
          value: "2046ys.com",
          label: "2046ys.com",
        },
        {
          value: "258.tv",
          label: "258.tv",
        },
      ];
      this.axios
        .post("http://localhost:5000/apiRequestSender/query/getTimerRemain", {
          a: 1,
        })
        .then((response) => {
          for (var i = 0; i < response.data.data.length; i++) {
            var json = {
              value: response.data.data[i].name,
              label: response.data.data[i].name,
              children: temp,
            };
            this.selectData.push(json);
          }
          if (typeof this.task == "undefined") {
            this.task = this.selectData[0].value;
          }
          if (typeof this.host == "undefined") {
            this.host = "4kgd.cn";
          }
          this.flag = true;
        });
    },

    getWebsiteData() {
      var site = "";
      if (typeof this.host == "undefined") {
        site = "4kgd.cn";
      } else {
        site = this.host;
      }
      this.websiteFlag = false;
      this.axios
        .post("http://localhost:5000/apiRequestSender/query/trackQuery", {
          param: site,
        })
        .then((response) => {
          this.websiteData = response.data.data[0];
          this.websiteFlag = true;
          this.infoFlag = true;
          var year = new Date().getFullYear();
          var month = new Date().getMonth() + 1;
          var day = new Date().getDate() - 2;
          var time = year + "年" + month + "月" + day + "日";
          this.websiteData["detectTime"] = time;
          // console.log(time);
          // console.log(this.websiteData.title);
          // console.log(this.websiteData);
        });
    },
  },
};
</script>

<style>
th {
  width: 140px;
}
.container {
  height: 60px;
  overflow: hidden;
}

.scoll {
  animation: myScoll 20s linear infinite;
}

@keyframes myScoll {
  0% {
    transform: translateY(0%);
  }
  100% {
    transform: translateY(-50%);
  }
}

#particles-js {
  width: 100%;
  height: 100%;
  position: fixed;
}
</style>

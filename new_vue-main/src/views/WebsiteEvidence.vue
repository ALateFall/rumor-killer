<template>
  <div>
    <a-card style="min-height: 1000px; padding: 16px">
      <div style="text-align: center; margin-top: 150px">
        <img
          src="http://localhost:8080/images/PiracySpy.png"
          style="width: 600px"
          alt=""
        />
      </div>

      <div style="text-align: center; margin-top: 20px">
        <a-input-search
          placeholder="输入待查询的网站URL"
          style="width: 800px; margin-bottom: 30px"
          @search="onSearch"
        />
      </div>
      <a-row v-if="this.statusFlag" style="margin-top: 20px">
        <a-col :span="7"></a-col>
        <a-col :span="10">
          <a-row :gutter="20">
            <a-col :span="4">
              <div style="font-family: Open Sans; font-weight: bold">
                检测状态：
              </div></a-col
            >
            <a-col :span="11"
              ><a-progress :percent="this.process" :status="this.status"
            /></a-col>
            <a-col :span="2"><a-spin v-if="this.spin" size="small" /></a-col>
            <a-col :span="7">
              <span style="font-weight: bold">{{ this.words }}</span>
            </a-col>
          </a-row>
        </a-col>
        <a-col :span="7"></a-col>
      </a-row>
      <div v-if="this.isWebsite" style="text-align: center">
        <span style="font-weight: bold"
          >您想检测的网站已在我们的数据库中，已为您探测网站最新信息。右边为网站截图取证，已添加带有时间戳的盲水印。</span
        >
      </div>

      <div v-if="this.notWebsite" style="text-align: center">
        <span style="font-weight: bold">检测完成！</span>
        <br />
        <span style="font-weight: bold"
          >您想检测的网站不是侵权网站，无法查看信息。</span
        >
      </div>

      <a-row :gutter="24" v-if="this.table" style="margin-top: 20px">
        <a-col :span="12">
          <a-descriptions :column="1" bordered>
            <a-descriptions-item label="网站标题">
              {{ this.data.title }}
            </a-descriptions-item>
            <a-descriptions-item label="Domain">
              {{ this.data.domain }} </a-descriptions-item
            ><a-descriptions-item label="IP地址">
              <a-tag color="orange"> {{ this.data.ip }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="地理位置">
              <a-tag color="blue"> {{ this.data.location }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="探测时间">
              {{ this.data["detect_time"] }}
            </a-descriptions-item>
            <a-descriptions-item label="运营人员姓名">
              <a-tag color="red"> {{ this.data.registrant }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="运营公司名称">
              {{ this.data.registrar }}
            </a-descriptions-item>
            <a-descriptions-item label="运营人员邮箱">
              <a-tag color="green"> {{ this.data.email }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="聚类ID">
              <a-tag color="cyan"> {{ this.data.cluster }} </a-tag>
            </a-descriptions-item>
            <a-descriptions-item label="是否是侵权电影网站">
              {{ this.data.isin }}
            </a-descriptions-item>
          </a-descriptions>
        </a-col>
        <a-col :span="12">
          <el-image
            v-show="this.table"
            :src="this.image"
            :preview-src-list="[this.image]"
          ></el-image>
        </a-col>
      </a-row>
    </a-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      process: 0,
      status: "active",
      statusFlag: false,
      spin: true,
      table: false,
      image: "",
      isWebsite: false,
      notWebsite: false,
      words: "",
    };
  },
  methods: {
    onSearch(value) {
      this.isWebsite = false;
      this.notWebsite = false;
      this.image =
        "http://localhost:5000/apiRequestSender/query/getScreenshot?domain=" +
        value;
      this.axios
        .post("http://localhost:5000/apiRequestSender/query/trackQuery", {
          param: value,
        })
        .then((response) => {
          this.data = response.data.data[0];
          let year = new Date().getFullYear();
          let month = new Date().getMonth();
          let day = new Date().getDate();
          this.data["detect_time"] = year + "年" + month + "月" + day + "日";
          this.data["isin"] = "是";
          this.data["cluster"] = 313;
        });
      this.change(value);
    },

    change(value) {
      this.table = false;
      this.spin = true;
      this.process = 0;
      this.status = "active";
      this.statusFlag = true;
      this.timer1 = setInterval(() => {
        this.process += 1;
        this.words = "分析网页结构...";
        if (this.process >= 33) {
          clearInterval(this.timer1);
        }
      }, 50);
      this.timer2 = setInterval(() => {
        if (this.process >= 33) {
          this.process += 1;
          this.words = "提取网页文本信息...";
        }
        if (this.process >= 43) {
          clearInterval(this.timer2);
        }
      }, 200);
      this.timer3 = setInterval(() => {
        if (this.process >= 43) {
          this.words = "图像识别中...";
          this.process += 1;
        }
        if (this.process >= 62) {
          clearInterval(this.timer3);
        }
      }, 50);
      this.timer4 = setInterval(() => {
        if (this.process >= 62) {
          this.words = "溯源中...";
          this.process += 1;
        }
        if (this.process >= 97) {
          clearInterval(this.timer4);
        }
      }, 100);
      this.timer5 = setInterval(() => {
        if (this.process >= 97) {
          this.words = "获取结果...";
          this.process += 1;
        }
        if (this.process >= 100) {
          this.words = "";
          this.status = "success";
          this.spin = false;
          clearInterval(this.timer5);
          setTimeout(() => {
            this.statusFlag = false;
            setTimeout(() => {
              console.log(value);
              if (value == "5dz.cn") {
                this.isWebsite = true;
                this.table = true;
              } else {
                this.notWebsite = true;
              }
            }, 1000);
          }, 1000);
        }
      }, 500);
    },
  },
};
</script>

<style>
</style>
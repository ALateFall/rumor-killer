<template>
  <div>
    <a-row class="mb-24">
      <a-col :span="24">
        <a-card
          class="card-table dashboard-bar-line header-solid"
          style="height: 70px; padding: 16px"
        >
          <div style="display: inline-block">
            <a-button type="primary" style="font-size: 13px">
              <a-icon type="cloud-download" style="font-size: 13px" />
              导出本页信息</a-button
            >
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
      <a-col :span="16">
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="height: 500px"
        >
          <NeoForAll @func="changeById"></NeoForAll>
        </a-card>
      </a-col>
      <a-col :span="8">
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="height: 500px"
        >
          <div
            class="timeline"
            style="
              max-height: 480px;
              max-weight: 350px;
              overflow-x: hidden;
              overflow-y: scroll;
              margin-top: 10px;
              matgin-buttom: 10px;
            "
          >
            <a-timeline mode="alternate" v-show="this.classChoice">
              <a-timeline-item color="green">聚类1838</a-timeline-item>
              <a-timeline-item color="green">
                新增网站:{{ this.class1838[0].url }}<br />{{
                  this.class1838[0].date
                }}
              </a-timeline-item>
              <a-timeline-item>
                新增网站:{{ this.class1838[1].url }}<br />{{
                  this.class1838[1].date
                }}
              </a-timeline-item>
              <a-timeline-item color="red">
                新增可疑组织人员:<br />{{ this.class1838[5].name }}
              </a-timeline-item>
              <a-timeline-item
                >新增网站:{{ this.class1838[2].url }}<br />{{
                  this.class1838[2].date
                }}
              </a-timeline-item>
              <a-timeline-item
                >新增网站:新增网站:{{ this.class1838[3].url }}<br />{{
                  this.class1838[3].date
                }}
              </a-timeline-item>
              <a-timeline-item>
                <a-icon
                  slot="dot"
                  type="clock-circle-o"
                  style="font-size: 16px"
                />
                组织常用服务:{{ this.class1838[5].pro }}<br />2022-04-01
              </a-timeline-item>
              <a-timeline-item
                >新增网站:新增网站:{{ this.class1838[4].url }}<br />{{
                  this.class1838[4].date
                }}
              </a-timeline-item>
            </a-timeline>
            
            <a-timeline mode="alternate" v-show="this.classChoice2">
              <a-timeline-item color="green">聚类870</a-timeline-item>
              <a-timeline-item color="green">
                新增网站:{{ this.class870[0].url }}<br />{{
                  this.class1838[0].date
                }} 

              </a-timeline-item>
              <a-timeline-item>
                <a-icon

                新增网站:{{ this.class870[1].url }}<br />{{
                  this.class1838[1].date
                }}
              </a-timeline-item>
              <!-- <a-timeline-item color="red">
                新增可疑组织人员:<br />{{ this.class870[5].name }}
              </a-timeline-item> -->
              <a-timeline-item
                >新增网站:{{ this.class870[2].url }}<br />{{
                  this.class870[2].date
                }}
              </a-timeline-item>
              <a-timeline-item
                >新增网站:{{ this.class870[3].url }}<br />{{
                  this.class870[3].date
                }}
              </a-timeline-item>
              <a-timeline-item>
                <a-icon
                  slot="dot"
                  type="clock-circle-o"
                  style="font-size: 16px"
                />
                组织常用服务:{{ this.class1838[5].pro }}<br />2022-04-01
              </a-timeline-item>
              <a-timeline-item
                >新增网站:新增网站:{{ this.class1838[4].url }}<br />{{
                  this.class1838[4].date
                }}
              </a-timeline-item>
            </a-timeline>
          </div>
        </a-card>
      </a-col>
    </a-row>
    <a-row :gutter="24">
      <a-col :span="12">
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="height: 400px"
          v-if="this.chartLeftFlag"
        >
          <template #title>
            <h6>该类别中侵权网站增长情况图</h6>
            <p>过去十周增长情况</p>
            <!-- <p>已发现网站数量 <span class="text-success">+0.8%</span></p> -->
          </template>
          <template #extra>
            <a-badge
              color="primary"
              class="badge-dot-primary"
              text="当周增长数量"
            />
            <a-badge
              color="primary"
              class="badge-dot-secondary"
              text="该类别中总数量"
            />
          </template>
          <ChartLeft :data1="this.data1" :data_all="this.data_all"></ChartLeft>
        </a-card>
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="height: 400px; text-align: center"
          v-if="this.chartLeftFlag == 0"
        >
          <div style="height: 180px"></div>
          <a-spin></a-spin>
        </a-card>
      </a-col>
      <a-col :span="12">
        <a-card
          class="mb-24 card-table dashboard-bar-line header-solid"
          style="height: 400px"
        >
          <template #title>
            <h6>各类别网站活跃时间与规模气泡图</h6>
            <p>大气泡说明含有侵权电影资源越多</p>
            <!-- <p>已发现网站数量 <span class="text-success">+0.8%</span></p> -->
          </template>
          <ChartRight></ChartRight>
        </a-card>
      </a-col>
    </a-row>
  </div>
</template>

<script>
import ChartLeft from "../components/TraceChartLeft.vue";
import ChartRight from "../components/TraceChartRight.vue";
import NeoForAll from "../components/NeoForAll.vue";
import * as NeoVis from "neovis.js";
export default {
  components: { ChartLeft, ChartRight, NeoForAll },
  data() {
    return {
      data1: [],
      data_all: [],
      chartLeftFlag: false,
      clusterId: null,
      classChoice: true,
      classChoice2: false,
      class1838: [
        { url: "yy6090.org", date: "2022-05-12" },
        { url: "zzhyqh.cn", date: "2022-05-01" },
        { url: "zyrbbs.org", date: "2022-04-13" },
        { url: "wuweiscape.com", date: "2022-04-01" },
        { url: "xjbylxx.org", date: "2022-04-01" },
        { name: "LiChen", pro: "Nginx" },
      ],
      class870: [
        { url: "116986.com", date: "2022-05-01" },
        { url: "661652.com", date: "2022-04-22" },
        { url: "jhdutwz.cn", date: "2022-04-13" },
        { url: "0p679.cn", date: "2022-04-12" },
        { url: "knymani.cn", date: "2022-04-09" },
        { name: "暂无", pro: "IIS" },
      ],
    };
  },

  mounted() {
    // setInterval(() => {
    var random = Math.floor(Math.random() * 100 + 10);
    //   this.onChangeLabel(random);
    // }, 2000);
    this.onChangeLabel(random);
  },

  methods: {
    changeById(data) {
      // console.log("infater",data)
      this.clusterId = data;
      var random = Math.floor(Math.random() * 100 + 10);
      this.onChangeLabel(random);
      if (this.classChoice) {
        this.classChoice = false;
        this.classChoice2 = true;
      } else if (!this.classChoice) {
        this.classChoice = true;
        this.classChoice2 = false;
      }
    },
    onChangeLabel(max) {
      //   Math.floor(Math.random() * 10 + 1)
      this.chartLeftFlag = false;
      setTimeout(() => {
        this.chartLeftFlag = true;
      }, 1000);
      this.data1 = [];
      this.data_all = [];
      var temp = 0;
      var change = 0;
      for (var i = 0; i < 10; i++) {
        temp = (max * 0.7) / 10;
        if (i % 2 == 0) {
          change = Math.floor(Math.random() * (temp * 0.8) + temp * 0.1);
          temp -= change;
        } else {
          temp += change;
        }
        this.data1.push(temp);
        if (i == 0) {
          this.data_all.push(temp + max * 0.3);
        } else {
          this.data_all.push(this.data_all[this.data_all.length - 1] + temp);
        }
      }
      //   console.log("data1:", this.data1);
      //   console.log("data_all:", this.data_all);
    },
  },
};
</script>

<style></style>

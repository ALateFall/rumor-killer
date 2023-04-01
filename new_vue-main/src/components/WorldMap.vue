<template>
  <div id="con">
    <div class="map-holder" id="map"></div>
  </div>
</template>

<script>
export default {
  name: "Map",
  data() {
    return {
      data: [],
      mapData: {},
      chinaData: {},
      nameMap: {},
      chart: null,
      lowData: [],
      middleData: [],
      highData: [],
      extraData: [],
      timeId: null,
    };
  },
  mounted() {
    this.$nextTick(() => {
      this.getState();
    });
  },
  unmounted() {
    this.$echarts.dispose;
    this.clearInterval(this.timeId);
  },
  beforeDestroy(){
    this.chart.clear();
  },
  methods: {
   async getState() {
      this.mapData = await this.axios.get(
        "http://localhost:8080/map/world.json"
      );
      this.nameMap = await this.axios.get(
        "http://localhost:8080/map/mapChinaName.json"
      );
      this.chinaData = await this.axios.get(
        "http://localhost:8080/map/USA_geo.json"
      );
      this.initChart();
      this.update();
    },

    //初始化表格
    initChart() {
      this.$echarts.registerMap("world", this.mapData.data);
      this.$echarts.registerMap("china", this.chinaData.data);
      this.chart = this.$echarts.init(document.getElementById("map"));
      this.getdata();
      let options = {
        title: {
          text: "▎ 地区分布",
          left: 20,
          top: 20,
          textStyle: {
            color: "#fff",
          },
        },

        geo: {
          map: "world",
          top: "5%",
          bottom: "5%",
          roam: true,
          label: {
            show: false,
          },
          // center:[50.46, 32.92],
          scaleLimit: {
            min: 0.85,
            max: 5,
          },
          nameMap: this.nameMap.data,
          itemStyle: {
            areaColor: "rgb(49,114,191,0.9)",
            borderColor: "#fff",
          },
        },
        legend: {
          left: "5%",
          bottom: "5%",
          orient: "vertical",
        },
      };
      this.chart.setOption(options);
      window.onresize = function () {
        //自适应大小
        this.chart.resize();
      };
      this.chart.on("click", async (arg) => {
        if (arg.name == "美国") {
          this.chart.setOption({
            geo: {
              map: "china",
              zoom: 1.6,
              center: [-100.445882, 39.7837304],
            },
          });
        }
      });
      let flag = 0;
      this.chart.getZr().on("click", async (arg) => {
        if (!arg.target) {
          if (flag == 0) {
            this.chart.setOption({
              geo: {
                map: "world",
                zoom: 1.0,
                center: [10.46, 13.92],
              },
            });
          }
        }
      });
    },

    update() {
      this.getdata().then(() => {
        console.log("hello");
        let dataOption = {
          series: [
            {
              type: "effectScatter",
              rippleEffect: {
                scale: 1,
                brushType: "stroke",
              },
              symbolSize: 6,
              itemStyle: {
                color: "#388E3C",
              },
              name: "低威胁",
              nameStyle: {
                color: "#fff",
              },
              legend: {
                show: false,
              },
              label: {
                show: true,
                color: "#fff",
                offset: [20, 20],
                formatter: "{b}",
              },
              data: this.lowData,
              coordinateSystem: "geo",
            },
            {
              type: "effectScatter",
              rippleEffect: {
                scale: 2,
                brushType: "stroke",
              },
              symbolSize: 6,
              itemStyle: {
                color: "#FFEB3B",
              },
              name: "中威胁",
              nameStyle: {
                color: "#fff",
              },
              legend: {
                show: false,
              },
              label: {
                show: true,
                color: "#fff",
                offset: [20, 20],
                formatter: "{b}",
              },
              data: this.middleData,
              coordinateSystem: "geo",
            },
            {
              type: "effectScatter",
              rippleEffect: {
                scale: 3,
                brushType: "stroke",
              },
              itemStyle: {
                color: "#FF5722",
              },
              name: "高威胁",
              nameStyle: {
                color: "#fff",
              },
              legend: {
                show: false,
              },
              label: {
                show: true,
                color: "#fff",
                offset: [20, 20],
                formatter: "{b}",
              },
              data: this.highData,
              coordinateSystem: "geo",
            },
            {
              type: "effectScatter",
              rippleEffect: {
                scale: 7,
                brushType: "stroke",
              },
              symbolSize: 11,

              itemStyle: {
                color: "#D32F2F",
              },
              name: "超高威胁",
              nameStyle: {
                color: "#fff",
              },
              legend: {
                show: false,
              },
              label: {
                show: true,
                color: "#fff",
                offset: [20, 20],
                formatter: "{b}",
              },
              data: this.extraData,
              coordinateSystem: "geo",
            },
          ],
        };
        this.chart.setOption(dataOption);
      });
    },

    async getdata() {
      await this.axios
        .post("http://localhost:5000/vpw/getLocAndStatus")
        .then((response) => {
          console.log(response);
          //低
          this.datas = response.data.data[0].map((item) => {
            return item;
          });
          // console.log("ts",datas)
          for (var i in this.datas) {
            this.lowData.push({ value: this.datas[i].loc });
          }
          //中
          this.datas = response.data.data[1].map((item) => {
            return item;
          });
          for (var i in this.datas) {
            this.middleData.push({ value: this.datas[i].loc });
          }
          //高
          this.datas = response.data.data[2].map((item) => {
            return item;
          });
          for (var i in this.datas) {
            this.highData.push({ value: this.datas[i].loc });
          }
          //极高
          this.datas = response.data.data[3].map((item) => {
            return item;
          });
          for (var i in this.datas) {
            this.extraData.push({ value: this.datas[i].loc });
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    startInterval() {
      if (this.timeId) {
        this.clearInterval(this.timeId);
      }
      this.timeId = setInterval(() => {
        this.update();
      }, 5000);
    },
  },
};
</script>

<style scoped lang="css">
.map-holder {
  height: 456px;
  /* background-image:url('../assets/img/img.jpg');
  background-size: 100% 100%; */
  border-radius: 5px;
  margin: 6px;
  width: 100%;
  border: 1px solid;
  border-color: white;
}
</style>

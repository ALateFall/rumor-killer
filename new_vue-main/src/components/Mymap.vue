<template>
  <div id="mymap"></div>
</template>

<script>
import "echarts-gl";
import mapURL from "../assets/img/earth2.jpg";
import backURL from "../assets/img/light.png";
export default {
  mounted() {
    this.getData().then(() => {
      this.initChart();
    });
  },
  beforeDestroy() {
    this.chart.clear();
  },
  data() {
    return {
      data: [],
      data1: [],
      data2: [],
      data3: [],
      data4: [],
      chart:null,
    };
  },
  methods: {
    async getData() {
      var _this = this;
      await this.axios
        .post("http://localhost:5000/vpw/getLocAndStatus")
        .then((response) => {
          console.log("123", response.data.data);

          for (var key in response.data.data[0]) {
            _this.data1.push(response.data.data[0][key].loc);
            _this.data1[key].push(100);
          }
          for (var key in response.data.data[1]) {
            _this.data2.push(response.data.data[1][key].loc);
            _this.data2[key].push(100);
          }
          for (var key in response.data.data[2]) {
            _this.data3.push(response.data.data[2][key].loc);
            _this.data3[key].push(100);
          }
          for (var key in response.data.data[3]) {
            _this.data4.push(response.data.data[3][key].loc);
            _this.data4[key].push(100);
          }

          _this.data = _this.data.concat(_this.data2);
          _this.data = _this.data.concat(_this.data3);
          _this.data = _this.data.concat(_this.data4);
          _this.data = _this.data.concat(_this.data1);

          console.log("all", _this.data);
        });
    },
    initChart() {
      this.chart = this.$echarts.init(document.getElementById("mymap"));
      var option = {
        backgroundColor: "rgb(0,0,0,0)",
        title: {
          text: "全球侵权情况态势感知",
        },
        legend:{
          show: true,
          left:"1%",
          top:"95%",
          orient: 'vertical',
        },
        globe: {
          // baseTexture:'https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples/data-gl/asset/earth.jpg',
          baseTexture: mapURL,
          environment: "none",
          globeRadius: 100,
          globeOuterRadius: 115,
          shading: "color",
          // environment: ROOT_PATH + '/data-gl/asset/starfield.jpg',
          atmosphere: {
            show: true,
          },
          viewControl: {
            autoRotate: true,
            autoRotateSpeed: 10,
            autoRotateAfterStill: 1,
            animation: true,
            animationDurationUpdate: 10000,
          },
        },
        series: [
          {
            type: "bar3D",
            coordinateSystem: "globe",
            stack: "1",
            name:"低风险",
            barSize: 1,
            bevelSmoothness: 0,
            minHeight: 0.1,
            maxHeight: 0.1,
            silent: true,
            label:{
              show: true,
            },
            itemStyle: {
              color: "green",
              opacity:0.2,
            },
            data: this.data1 ,
          },
          {
            type: "bar3D",
            coordinateSystem: "globe",
            stack: "2",
            name:"中风险",
            barSize: 1.5,
            bevelSmoothness: 0,
            minHeight: 0.1,
            maxHeight: 0.5,
            silent: true,
            itemStyle: {
              color: "yellow",
              opacity:0.3,
            },
            data: this.data2,
          },
          {
            type: "bar3D",
            coordinateSystem: "globe",
            stack: "3",
            name:"中高风险",
            barSize: 1.5,
            bevelSmoothness: 0,
            minHeight: 0.1,
            maxHeight: 1,
            silent: true,
            itemStyle: {
              color: "orange",
              opacity:0.4,
            },
            data: this.data3,
          },
          {
            type: "bar3D",
            coordinateSystem: "globe",
            stack: "3",
            name:"高风险",
            barSize: 2,
            bevelSmoothness: 0,
            minHeight: 0.1,
            maxHeight: 1.0,
            silent: true,
            itemStyle: {
              color: "red",
              opacity:0.5,
            },
            data: this.data4,
          },
        ],
      };
      this.chart.setOption(option);
    },
  },
};
</script>

<style scoped>
#mymap {
  margin-top: 0px;
  min-height: 580px;
  margin-left: 20px;
}
</style>

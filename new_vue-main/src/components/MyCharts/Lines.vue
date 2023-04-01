<template>
  <div class="lines-holder" :id="this.myid"></div>
</template>

<script>
export default {
  mounted() {
    this.initChart();
  },
  data() {
    return {
      datas: [],
      deDatas: [],
    };
  },
  props:['myid'],
  methods: {
    initChart() {
      this.axios
        .post("http://localhost:5000/site/getSiteCount", {
          siteType: "undetected",
        })
        .then((response) => {
          var data1 = response.data.data;
          this.datas.push(parseInt(data1 * 0.4));
          this.datas.push(parseInt(data1 * 0.1));
          this.datas.push(parseInt(data1 * 0.2));
          this.datas.push(parseInt(data1 * 0.41));
          this.datas.push(parseInt(data1 * 0.15));
          this.datas.push(parseInt(data1 * 0.5));
          console.log("1", this.datas);
        });

      this.axios
        .post("http://localhost:5000/site/getSiteCount", {
          siteType: "detected",
        })
        .then((response) => {
          var data2 = response.data.data;
          this.deDatas.push(parseInt(data2 * 0.12));
          this.deDatas.push(parseInt(data2 * 0.17));
          this.deDatas.push(parseInt(data2 * 0.31));
          this.deDatas.push(parseInt(data2 * 0.1));
          this.deDatas.push(parseInt(data2 * 0.19));
          this.deDatas.push(parseInt(data2 * 0.13));
          console.log(this.deDatas);
          let chart = this.$echarts.init(
            document.getElementById(this.myid)
          );
          chart.setOption({
            //标题配置
            title: {
              text: "▎侵权网页数量",
              left: 10,
              top: 10,
              textStyle: {
                color: "rgb(154,154,154)",
              },
            },
            //展示图的展示位置
            grid: {
              top: "20%",
              left: "3%",
              right: "6%",
              bottom: "3%",
              containLabel: true, // 距离是包含坐标轴上的文字
            },
            //图例的展示，通过name与series里对应
            legend: {
              show: true,
              right: 10,
              top: 10,
              textStyle: {
                color: "rgb(154,154,154)",
              },
            },
            yAxis: {
              type: "value",
              show: true,
              axisLine: {
                lineStyle: {
                  color: "rgb(154,154,154)",
                  width: 1, //这里是为了突出显示加上的
                },
              },
            },
            xAxis: {
              type: "category",
              data: ["十二月", "一月", "二月", "三月", "四月", "五月"],
              boundaryGap: false,
              axisLine: {
                lineStyle: {
                  color: "rgb(154,154,154)",
                  width: 1, //这里是为了突出显示加上的
                },
              },
            },
            //鼠标在图上时的具体信息展示
            tooltip: {
              trigger: "axis",
              axisPointer: {
                type: "line",
                z: 0,
                lineStyle: {
                  color:"rgb(154,154,154)",
                },
              },
            },
            series: [
              {
                name: "未侵权",
                type: "line",
                stack: "1",
                areaStyle: {},
                label: {
                  show: true,
                  position: "right",
                  textStyle: {
                    color: "rgb(154,154,154)",
                  },
                },
                data: this.deDatas,
                itemStyle: {
                  // 指明颜色渐变的方向
                  // 指明不同百分比之下颜色的值
                  color: new this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
                    // 百分之0状态之下的颜色值
                    {
                      offset: 0,
                    //   color: "rgba(11, 168, 44, 1)",
                    color:"#B7CDD6",
                    //   color: "rgba(0, 0, 0, 0)",

                    },
                    // 百分之100状态之下的颜色值
                    {
                      offset: 1,
                    //   color: "rgba(11, 168, 44, 1)",
                      color: "rgba(0, 0, 0, 0)",

                    },
                  ]),
                },
              },
              {
                name: "侵权",
                type: "line",
                stack: "0",
                areaStyle: {},
                label: {
                  show: true,
                  position: "right",
                  textStyle: {
                    color: "rgb(154,154,154)",
                  },
                },
                data: this.datas,
                itemStyle: {
                  // 指明颜色渐变的方向
                  // 指明不同百分比之下颜色的值
                  color: new this.$echarts.graphic.LinearGradient(0, 0, 1, 0, [
                    // 百分之0状态之下的颜色值
                    {
                      offset: 0,
                      color: "rgba(254, 33, 30, 1)",
                    },
                    // 百分之100状态之下的颜色值
                    {
                      offset: 1,
                      color: "rgba(254, 33, 30, 1)",
                    },
                  ]),
                },
              },
            ],
          });
        })
        .catch(function (error) {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.lines-holder {
  height: 230px;
  margin: 0px;
  padding: 0px;
  width: 100%;
  /* border: 1px solid; */
  border-radius: 12px;
  box-shadow: 1;
  // background-image: linear-gradient(to right, #00369E, #005CFD, #A18DFF ) ;

  /* border-color: black; */
}
</style>

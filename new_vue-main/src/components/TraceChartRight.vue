<template>
  <div>
    <!-- Bubble chart -->
    <canvas
      ref="chart"
      class="chart-bubble"
      :style="{ height: height + 'px' }"
    ></canvas>
    <!-- / Bubble chart -->
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  props: [],
  data() {
    return {
      height: 300,
    };
  },
  mounted() {
    let ctx = this.$refs.chart.getContext("2d");

    this.chart = new Chart(ctx, {
      type: "bubble",
      data: {
        // labels: [
        //   "第一周",
        //   "第二周",
        //   "第三周",
        //   "第四周",
        //   "第五周",
        //   "第六周",
        //   "第七周",
        // ],
        datasets: [
          {
            label: "Dataset 1",
            data: [
              {
                x: 0,
                y: 0,
                r: 10,
              },
              {
                x: 1,
                y: 30,
                r: 20,
              },
              {
                x: 2,
                y: 35,
                r: 10,
              },
              {
                x: 3,
                y: 22,
                r: 10,
              },
              {
                x: 4,
                y: 49,
                r: 15,
              },
              {
                x: 5,
                y: 43,
                r: 5,
              },
              {
                x: 6,
                y: 9,
                r: 5,
              },
            ],
            backgroundColor: "#B37FEB",
          },
          {
            label: "Dataset 1",
            data: [
              {
                x: 0,
                y: 23,
                r: 18,
              },
              {
                x: 0,
                y: 36,
                r: 12,
              },
              {
                x: 3,
                y: 28,
                r: 5,
              },
              {
                x: 5,
                y: 12,
                r: 13,
              },
              {
                x: 6,
                y: 33,
                r: 3,
              },
              {
                x: 6,
                y: 9,
                r: 13,
              },
              {
                x: 6,
                y: 39,
                r: 2,
              },
            ],
            backgroundColor: "#B37FEB",
          },
        ],
      },
      options: {
        layout: {
          padding: {
            top: 30,
            right: 15,
            left: 10,
            bottom: 5,
          },
        },
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: false,
          },
        },
        tooltips: {
          enabled: true,
          mode: "index",
          intersect: false,
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: false,
              borderDash: [5, 5],
            },
            ticks: {
              display: true,
              padding: 10,
              color: "#b2b9bf",
              font: {
                size: 11,
                family: "Open Sans",
                style: "normal",
                lineHeight: 2,
              },
            },
          },
          x: {
            grid: {
              drawBorder: false,
              display: true,
              drawOnChartArea: true,
              drawTicks: true,
              borderDash: [5, 5],
            },
            ticks: {
              display: true,
              color: "#b2b9bf",
              padding: 10,
              font: {
                size: 11,
                family: "Open Sans",
                style: "normal",
                lineHeight: 2,
              },
              callback: function (value, index, values) {
                var week = "";
                switch (value) {
                  case 0: {
                    week = "一";
                    break;
                  }
                  case 1: {
                    week = "二";
                    break;
                  }
                  case 2: {
                    week = "三";
                    break;
                  }
                  case 3: {
                    week = "四";
                    break;
                  }
                  case 4: {
                    week = "五";
                    break;
                  }
                  case 5: {
                    week = "六";
                    break;
                  }
                  case 6: {
                    week = "七";
                    break;
                  }
                  default: {
                    return "";
                  }
                }
                return "第" + week + "周";
              },
            },
          },
        },
      },
    });
  },
  // Right before the component is destroyed,
  // also destroy the chart.
  beforeDestroy: function () {
    this.chart.destroy();
  },
};
</script>

<style lang="scss" scoped>
</style>
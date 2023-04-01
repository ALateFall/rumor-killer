<template>
  <div>
    <!-- Line chart -->
    <canvas
      ref="chart"
      class="chart-line"
      :style="{ height: height + 'px' }"
    ></canvas>
    <!-- / Line chart -->
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  props: ["data", "height"],
  data() {
    return {
      chart: null,
    };
  },
  mounted() {
    let ctx = this.$refs.chart.getContext("2d");

    this.chart = new Chart(ctx, {
      type: "line",
      data: this.data,
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
          A: {
            title: {
              display: true,
              text: "侵权网站数量",
            },
            grid: {
              display: true,
              color: "rgba(0, 0, 0, .2)",
              zeroLineColor: "#000000",
              borderDash: [6],
              borderDashOffset: [6],
            },
            ticks: {
              suggestedMin: 22000,
              suggestedMax: 24000,
              display: true,
              color: "#8C8C8C",
              font: {
                size: 14,
                lineHeight: 1.8,
                weight: "600",
                family: "Open Sans",
              },
            },
            type: "linear",
            position: "left",
          },
          B: {
            title: {
              display: true,
              text: "侵权电影数量",
            },
            grid: {
              display: true,
              color: "rgba(0, 0, 0, .2)",
              zeroLineColor: "#000000",
              borderDash: [6],
              borderDashOffset: [6],
            },
            ticks: {
              suggestedMin: 2200000,
              suggestedMax: 2400000,
              display: true,
              color: "#8C8C8C",
              font: {
                size: 14,
                lineHeight: 1.8,
                weight: "600",
                family: "Open Sans",
              },
            },
            type: "linear",
            position: "right",
          },
          x: {
            grid: {
              display: false,
            },
            ticks: {
              display: true,
              color: "#8C8C8C",
              font: {
                size: 14,
                lineHeight: 1.5,
                weight: "600",
                family: "Open Sans",
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
<template>
  <div>
    <!-- Mixed chart -->
    <canvas
      ref="chart"
      class="chart-mixed"
      :style="{ height: height + 'px' }"
    ></canvas>
    <!-- / Mixed chart -->
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  props: [],
  data() {
    return {
      height: 220,
    };
  },
  mounted() {
    let ctx = this.$refs.chart.getContext("2d");

    this.chart = new Chart(ctx, {
      data: {
        labels: ["一月", "二月", "三月", "四月", "五月", "六月"],
        datasets: [
          {
            type: "bar",
            label: "获取任务",
            weight: 10,
            tension: 0.4,
            borderWidth: 0,
            pointBackgroundColor: "#1890FF",
            borderColor: "#1890FF",
            backgroundColor: "#1890FF",
            borderRadius: 10,
            borderSkipped: false,
            data: [24, 15, 21, 34, 18, 12],
            maxBarThickness: 20,
          },
          {
            type: "bar",
            label: "分析任务",
            weight: 10,
            tension: 0.4,
            borderWidth: 0,
            pointBackgroundColor: "#B37FEB",
            borderColor: "#B37FEB",
            backgroundColor: "#B37FEB",
            borderRadius: 10,
            borderSkipped: false,
            data: [9, 30, 32, 36, 21, 9],
            maxBarThickness: 20,

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

<style lang="scss" scoped></style>

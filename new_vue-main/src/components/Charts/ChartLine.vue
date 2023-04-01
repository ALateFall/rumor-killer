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
  props: [
    // 'data'
    "height",
  ],
  data() {
    return {
      chart: null,
    };
  },
  mounted() {
    let ctx = this.$refs.chart.getContext("2d");
    var gradientStroke1 = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke1.addColorStop(1, "rgba(24, 144, 255, .3)");
    gradientStroke1.addColorStop(0.2, "rgba(24, 144, 255, 0)");
    gradientStroke1.addColorStop(0, "rgba(24, 144, 255, 0)"); // Primary color

    var gradientStroke2 = ctx.createLinearGradient(0, 230, 0, 50);

    gradientStroke2.addColorStop(1, "rgba(179,127,235,0.3)");
    gradientStroke2.addColorStop(0.2, "rgba(179,127,235,0)");
    gradientStroke2.addColorStop(0, "rgba(179,127,235,0)"); // Dark color
    this.chart = new Chart(ctx, {
      type: "line",
      data: {
        labels: ["一月", "二月", "三月", "四月", "五月", "六月"],
        datasets: [
          {
            label: "侵权网站",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#1890FF",
            borderWidth: 3,
            backgroundColor: gradientStroke1,
            fill: true,
            data: [25718, 21821, 29471, 40281, 26182, 29391],
            maxBarThickness: 6,
          },
          {
            label: "未侵权网站",
            tension: 0.4,
            borderWidth: 0,
            pointRadius: 0,
            borderColor: "#B37FEB",
            borderWidth: 3,
            backgroundColor: gradientStroke2,
            fill: true,
            data: [40291, 39123, 49172, 50192, 40412, 32182],
            maxBarThickness: 6,
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
              display: true,
              color: "rgba(0, 0, 0, .2)",
              zeroLineColor: "#000000",
              borderDash: [6],
              borderDashOffset: [6],
            },
            ticks: {
              suggestedMin: 0,
              suggestedMax: 1000,
              display: true,
              color: "#8C8C8C",
              font: {
                size: 14,
                lineHeight: 1.8,
                weight: "600",
                family: "Open Sans",
              },
            },
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

<style lang="scss" scoped></style>

<template>
  <div>
    <!-- Pie chart -->

    <canvas
      ref="chart"
      class="chart-pie"
      :style="{ height: height + 'px' }"
    ></canvas>
    <!-- / Pie chart -->
  </div>
</template>

<script>
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

export default {
  props: [],
  data() {
    return {
      height: 200,
    };
  },
  mounted() {
    let ctx = this.$refs.chart.getContext("2d");

    this.chart = new Chart(ctx, {
      type: "pie",
      data: {
        labels: ["深度分析任务", "浅度分析任务"],
        datasets: [
          {
            label: "Projects",
            weight: 9,
            cutout: 0,
            tension: 0.9,
            pointRadius: 2,
            borderWidth: 2,
            backgroundColor: ["rgb(179,127,235)", "rgb(24,144,255)", ],
            data: [12, 9],
            fill: false,
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            display: true,
			position:"right",
          },
        },
        interaction: {
          intersect: false,
          mode: "index",
        },
        scales: {
          y: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false,
            },
          },
          x: {
            grid: {
              drawBorder: false,
              display: false,
              drawOnChartArea: false,
              drawTicks: false,
            },
            ticks: {
              display: false,
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
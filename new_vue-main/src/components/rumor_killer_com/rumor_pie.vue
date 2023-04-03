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
        height: 300,
      };
    },
    mounted() {
      let ctx = this.$refs.chart.getContext("2d");
  
      this.chart = new Chart(ctx, {
        type: "pie",
        data: {
          labels: ["非谣言", "谣言"],
          datasets: [
            {
              label: "Projects",
              weight: 9,
              cutout: 0,
              tension: 0.9,
              pointRadius: 2,
              borderWidth: 2,
              backgroundColor: [
                "rgb(255,173,96)",
                "rgb(150,206,180)",
                //   "#141414",
                //   "#1890FF",
              ],
              data: [545, 376],
              fill: false,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              // display: false,
              position: "top",
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
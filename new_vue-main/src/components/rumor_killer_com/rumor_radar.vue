<template>
  <div>
    <canvas id="myChart" :height="this.height"></canvas>
  </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default ({
  props: [
  ],
  data() {
    return {
      height: 400,
    };
  },
  mounted() {
    var ctx = document.getElementById('myChart').getContext('2d');
    var myChart = new Chart(ctx, {
      type: 'radar',
      data: {
        labels: [
          '争议性',
          '影响性',
          '可信性',
        ],
        datasets: [{
          label: 'My First Dataset',
          data: [65, 59, 60],
          fill: true,
          backgroundColor: 'rgba(255, 99, 132, 0.2)',
          borderColor: 'rgb(255, 99, 132)',
          pointBackgroundColor: 'rgb(255, 99, 132)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgb(255, 99, 132)'
        }]
      },
      options: {
        elements: {
          line: {
            borderWidth: 3
          }
        },
        scales: {
          r: {
            angleLines: {
              display: false
            },
            suggestedMin: 50,
            suggestedMax: 80
          }
        },
        responsive: true,
        maintainAspectRatio: false
      },
    });
  },
  // Right before the component is destroyed,
  // also destroy the chart.
  beforeDestroy: function () {
    this.chart.destroy();
  },
})

</script>

<style lang="scss" scoped></style>
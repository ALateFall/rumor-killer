<template>
    <div>
        <!-- Bar chart 2 -->
        <canvas ref="chart" class="chart-bar-2" :style="{ 'height': height + 'px'}"></canvas>
        <!-- / Bar chart 2 -->
    </div>
</template>

<script>
import { Chart, registerables } from 'chart.js';
Chart.register(...registerables);

export default ({
    props: [
        'detection'
    ],
    data() {
        return {
            height: 300,
        };
    },
    mounted() {
        let ctx = this.$refs.chart.getContext("2d");

        this.chart = new Chart(ctx, {
            type: "bar",
            data: {
                labels: ['非谣言', '谣言'],
                datasets: [{
                    label: "任务数量",
                    weight: 5,
                    borderWidth: 0,
                    borderRadius: 4,
                    backgroundColor: '#B37FEB',
                    data: [this.detection[0], this.detection[1]],
                    fill: false,
                    maxBarThickness: 35
                }],
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
                            borderDash: [5, 5]
                        },
                        ticks: {
                            display: true,
                            padding: 10,
                            color: '#b2b9bf',
                            font: {
                                size: 11,
                                family: "Open Sans",
                                style: 'normal',
                                lineHeight: 2
                            },
                        },
                    },
                    x: {
                        grid: {
                            drawBorder: false,
                            display: true,
                            drawOnChartArea: true,
                            drawTicks: true,
                            borderDash: [5, 5]
                        },
                        ticks: {
                            display: true,
                            color: '#b2b9bf',
                            padding: 10,
                            font: {
                                size: 11,
                                family: "Open Sans",
                                style: 'normal',
                                lineHeight: 2
                            },
                        },
                    },
                },
            }
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
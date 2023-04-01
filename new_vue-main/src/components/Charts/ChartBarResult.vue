<template>
	<div>
		<!-- Bar chart 2 -->
		<canvas ref="chart" class="chart-bar-2" :style="{'height': height + 'px'}"></canvas>
		<!-- / Bar chart 2 -->
	</div>
</template>

<script>
	import { Chart, registerables } from 'chart.js';
	Chart.register(...registerables);

	export default ({
		props: [
			"data",
		],
		data(){
			return {
				height: 200,
			} ;
		},
		mounted () { 
    		let ctx = this.$refs.chart.getContext("2d");
			// console.log("prop:", this.data);
			this.chart = new Chart(ctx, {
				type: "bar",
				data: {
					labels: ['Apache', 'CloudFlare', 'IIS', 'Microsoft ASP.NET', 'Nginx', 'PHP', 'Windows Server'],
					datasets: [{
						label: "服务器软件",
						weight: 5,
						borderWidth: 0,
						borderRadius: 4,
						// backgroundColor: '#B37FEB',
						backgroundColor: "#1890FF",
						data: this.data,
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
			this.chart.destroy() ;
		},
	})

</script>

<style lang="scss" scoped>
</style>
<template>

	<!-- Line Chart card -->
	<a-card :bordered="false" class="dashboard-bar-line header-solid">
		<template #title>
			<h6>侵权网站数量变化</h6>			
			<p>本月新增<span style="color:rgb(179,127,235)">-20%</span></p>	
			<p>本月新增<span style="color:rgb(24,144,255)">+12%</span></p>
		</template>
		<template #extra>
			<a-badge color="primary" class="badge-dot-primary" text="侵权" />
			<a-badge color="primary" class="badge-dot-secondary" text="未侵权" />
		</template>
		<chart-line :height="200" :data="lineChartData"></chart-line>
	</a-card>
	<!-- / Line Chart card -->

</template>

<script>

	// Bar chart for "Active Users" card.
	import ChartLine from '../Charts/ChartLine' ;

	export default ({
		components: {
			ChartLine,
		},
		data() {
			return {

				// Data for line chart.
				lineChartData: {
					labels: ["一月", "二月", "三月", "四月", "五月", "六月"],
					datasets: [{
						label: "侵权网站",
						tension: 0.4,
						borderWidth: 0,
						pointRadius: 0,
						borderColor: "#1890FF",
						borderWidth: 3,
						data: [25718, 21821, 29471, 40281, 26182, 29391],
						maxBarThickness: 6

					},
					{
						label: "未侵权网站",
						tension: 0.4,
						borderWidth: 0,
						pointRadius: 0,
						borderColor: "#B37FEB",
						borderWidth: 3,
						data: [40291, 39123, 49172, 62192, 40412, 32182],
						maxBarThickness: 6

					}],
				},
			}
		},
	})

</script>
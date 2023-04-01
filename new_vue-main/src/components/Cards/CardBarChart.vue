<template>

	<!-- Active Users Card -->
	<a-card :bordered="false" class="dashboard-bar-chart">
		<chart-bar :height="200" :data="barChartData"></chart-bar>
	</a-card>
	<!-- Active Users Card -->

</template>

<script>

	// Bar chart for "Active Users" card.
	import ChartBar from '../Charts/ChartBar' ;

	export default ({
		components: {
			ChartBar,
		},
		data() {
			return {
				// Data for bar chart.
				barChartData: {
					labels: ["一月", "二月", "三月", "四月", "五月", "六月"],
					datasets: [{
						label: "侵权次数",
						backgroundColor: '#fff',
						borderWidth: 0,
						borderSkipped: false,
						borderRadius: 6,
						data: [83274, 66529, 91274, 125923, 78212, 87597],
						maxBarThickness: 20,
					}, ],
				},
			}
		},
	})

</script>
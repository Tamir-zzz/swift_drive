$(function () {
	var d1, d2, d3, data, chartOptions;
	d1 = [[0,12],[21,38],[13,29],[82,14],[52,43],[32,59],[92,48],[68,31],[32,24],[30,67],[10,45],[37,5],[18,41],[31,70]];
	d2 = [[23,40],[46,16],[20,42],[33,41],[51,39],[11,28],[32,36],[38,40],[99,22],[41,30],[21,18]];
	d3 = [[3,23],[4,36],[29,62],[13,55],[11,42],[6,37],[27,16],[3,45],[79,52],[39,90],[11,68]];
	data = [{ 
		label: "Likes", 
		data: d1,
	}, {
		label: "Shares",
		data: d2,
	}, {
		label: "Comments",
		data: d3,
	}];
	chartOptions = {
		xaxis: {	
		},
		yaxis: {
		},
		series: {
			lines: {
				show: false, 
				fill: false,
				lineWidth: 4,
			},
			points: {
				show: true,
				radius: 3,
				fill: true,
				lineWidth: 6,
			}
		},
		grid:{
      hoverable: true,
      clickable: true,
      borderWidth: 1,
      tickColor: '#E5E5E5',
      borderColor: '#E5E5E5',
    },
		legend: {
			show: true
		},
		tooltip: true,
		tooltipOpts: {
			content: '%s: %y'
		},
		shadowSize: 0,
		colors: ['#E84234', '#4286F7', '#F9BB06', '#32AB52'],
	};
	var holder = $('#scatter-chart');
	if (holder.length) {
		$.plot(holder, data, chartOptions );
	}
});
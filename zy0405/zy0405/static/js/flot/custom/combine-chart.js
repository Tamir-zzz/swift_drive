$(function () {    
		var data1 = [
			[1354586000000, 153], [1364587000000, 658], [1374588000000, 198],
			[1384589000000, 663], [1394590000000, 801], [1404591000000, 1080],
			[1414592000000, 353], [1424593000000, 749], [1434594000000, 523],
			[1444595000000, 258], [1454596000000, 688], [1464597000000, 364]
		];
 
		var data2 = [
			[1354586000000, 53], [1364587000000, 65], [1374588000000, 98],
			[1384589000000, 83], [1394590000000, 980], [1404591000000, 808],
			[1414592000000, 720], [1424593000000, 674], [1434594000000, 23],
			[1444595000000, 79], [1454596000000, 88], [1464597000000, 36]
		];
 
		var data = [{
			label: "Sales",
			data: data1,
			bars: {
				show: true,
				lineWidth: 0,
				barWidth: 30 * 60 * 60 * 1000 * 80,
				fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
			}
		},{
			label: "Expenses",
			data: data2,
			lines: {
				show: true,
				lineWidth: 2,
				fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
			},
			points:{
				show:true,
				radius: 4,
				fill: true,
				fillColor: "#FFFFFF",
				lineWidth: 2
			}
		}];
 
		var options = {
			series: {
			shadowSize: 0,
			bars: {
				lineWidth: 2,
				fillColor: { colors: [ { opacity: 1 }, { opacity: 1 } ] }
			}
		},
		grid: {
			hoverable: true,
			clickable: false,
			borderWidth: 1,
			tickColor: '#E5E5E5',
			borderColor: '#E5E5E5',
		},
		legend:{   
			show: true,
			position: 'nw',
			noColumns: 0,
		},
		tooltip: true,
		tooltipOpts: {
			content: '%x: %y'
		},

		xaxis: {mode: "time", ticks:6, tickDecimals: 0},
		yaxis: {ticks:6, tickDecimals: 0},

		colors: ['#4286F7', '#E84234', '#F9BB06', '#32AB52'],
	};
 
	var plot = $.plot($("#combineChart"), data, options);  
});
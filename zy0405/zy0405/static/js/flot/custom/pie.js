var $border_color = "#eee";
var $grid_color = "#eee";
var $default_black = "#666";

$(function () {

	var data, chartOptions;
	
	data = [
		{ label: "HTML", data: Math.floor (Math.random() * 100 + 190) }, 
		{ label: "CSS", data: Math.floor (Math.random() * 100 + 220) }, 
		{ label: "PHP", data: Math.floor (Math.random() * 100 + 370) }, 
		{ label: "jQuery", data: Math.floor (Math.random() * 100 + 120) },
		{ label: "RUBY", data: Math.floor (Math.random() * 100 + 430) }
	];

	chartOptions = {		
		series: {
			pie: {
				show: true,  
				innerRadius: 0, 
				stroke: {
					width: 0
				}
			}
		},
		grid:{
      hoverable: true,
      clickable: false,
      borderWidth: 0,
      tickColor: '#E5E5E5',
      borderColor: '#E5E5E5',
    },
		legend: {
			position: 'nw'
		},
		shadowSize: 0,
		tooltip: true,
		
		tooltipOpts: {
			content: '%s: %y'
		},
		colors: ['#E84234', '#4286F7', '#F9BB06', '#32AB52'],
	};

  var holder = $('#pie-chart');

  if (holder.length) {
      $.plot(holder, data, chartOptions );
  }
			
});
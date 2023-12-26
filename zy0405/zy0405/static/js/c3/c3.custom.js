// C3 Chart 1
var chart1 = c3.generate({
	bindto: '#audienceOverview',
	padding: {
		left: 40,
	},
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 105, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 67, 69, 72, 71, 75, 80, 65, 71],
			// ['data1', 1, 1, 2, 3, 5, 20, 50, 80, 90, 110, 110, 100, 50, 50, 120, 150],
			// ['data2', 50, 50, 80, 110, 110, 90, 80, 50, 20, 15, 10, 10, 5, 30, 40, 110],
		],
		types: {
			data1: 'area-spline',
			data2: 'area-spline'
		},
		names: {
			data1: 'Visitors',
			data2: 'Clicks'
		},
		colors: {
			data1: '#4286F7',
			data2: '#E84234'
		},
	}
});

// C3 Chart 2
var chart2 = c3.generate({
	bindto: '#mobileDesktop',
	padding: {
		left: 30,
	},
	data: {
		columns: [
			['Mobile', 30, 200, 200, 400, 250],
			['Desktop', 130, 100, 100, 200, 50],
		],
		type: 'bar',
		colors: {
			Desktop: '#E84234',
			Mobile: '#4286F7'
		},
	},
	legend: {
		show: false,
	},
	axis: {
		y: {
			tick: {
				count: 3,
			}
		}
	}
});

// C3 Chart 3
var chart3 = c3.generate({
	bindto: '#customerRating',
	data: {
		columns: [
			['Customers', 10, 20, 50, 40, 50, 100],
		],
		types: {
			Customers: 'area',
		},
		colors: {
			Customers: '#FBACAF',
		},
	},
	legend: {
		show: false,
	},
	axis: {
		y: {
		  show: false,
		},
		x: {
		  show: false,
		},
	},
});

// C3 Chart 4
var chart4 = c3.generate({
	bindto: '#lineGraph',
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 105, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 67, 69, 72, 71, 75, 80, 65, 71],
		],
		names: {
			data1: 'Likes',
			data2: 'Clicks'
		},
		colors: {
			data1: '#E84234',
			data2: '#4286F7'
		},
	}
});

// C3 Chart 5
var chart5 = c3.generate({
	bindto: '#splineGraph',
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 105, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 67, 69, 72, 71, 75, 80, 65, 71],
		],
		types: {
			data1: 'spline',
			data2: 'area-spline'
		},
		names: {
			data1: 'Likes',
			data2: 'Clicks'
		},
		colors: {
			data1: '#E84234',
			data2: '#32AB52'
		},
	}
});

// C3 Chart 6
var chart6 = c3.generate({
	bindto: '#areaSplineGraph',
	data: {
		columns: [
			['data1', 24, 49, 52, 48, 62, 60, 62, 70, 80, 82, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 24, 27, 32, 40, 48, 46, 57, 64, 62, 59, 71, 75, 80, 65, 71, 89],
		],
		types: {
			data1: 'area-spline',
			data2: 'area-spline'
		},
		names: {
			data1: 'Male',
			data2: 'Female'
		},
		colors: {
			data1: '#E84234',
			data2: '#4286F7'
		},
	}
});

// C3 Chart 7
var chart7 = c3.generate({
	bindto: '#stepGraph',
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 78, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 44, 59, 73, 77, 89, 82, 81, 85, 90, 95, 71],
		],
		types: {
			data1: 'step',
			data2: 'area-step'
		},
		names: {
			data1: 'Twitter',
			data2: 'LinkedIn'
		},
		colors: {
			data1: '#E84234',
			data2: '#4286F7'
		},
	}
});

// C3 Chart 8
var chart8 = c3.generate({
	bindto: '#barAreaGraph',
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 105, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 67, 69, 72, 71, 75, 80, 65, 71],
		],
		types: {
			data1: 'bar',
			data2: 'area'
		},
		names: {
			data1: 'Twitter',
			data2: 'LinkedIn'
		},
		colors: {
			data1: '#32AB52',
			data2: '#F9BB06'
		},
	}
});

// C3 Chart 9
var chart9 = c3.generate({
	bindto: '#barGraph',
	data: {
		columns: [
			['data1', 24, 28, 31, 49, 57, 59, 52, 48, 55, 58, 62, 60, 62, 58, 55, 61, 70, 80, 77, 78, 82, 98, 99, 105, 102, 95, 92, 100, 103, 117, 121, 126],
			['data2', 15, 16, 19, 24, 27, 32, 38, 36, 32, 36, 40, 48, 41, 44, 46, 53, 58, 62, 65, 61, 64, 62, 59, 63, 67, 69, 72, 71, 75, 80, 65, 71],
		],
		type: 'bar',
		names: {
			data1: 'Twitter',
			data2: 'LinkedIn'
		},
		colors: {
			data1: '#F9BB06',
			data2: '#32AB52'
		},
	}
});

// C3 Chart 10
var chart10 = c3.generate({
	bindto: '#stackedBarGraph',
	data: {
	columns: [
		['data1', 30, 90, 200, 400, 550, 250, 330, 120, 480, 560, 220, 300, 240, 470, 190,550, 250, 330, 120],
		['data2', 130, 100, 200, 200, 450, 150, 190, 220, 350, 180, 330, 550, 280, 180, 200, 450, 150, 190, 220],
		['data3', 230, 200, 200, 300, 250, 250, 320, 180, 410, 270, 180, 210, 270, 420, 330, 180, 410, 270, 180]
	],
	type: 'bar',
	names: {
		data1: 'Twitter',
		data2: 'LinkedIn',
		data3: 'Facebook',
	},
	colors: {
		data1: '#55ACEE',
		data2: '#007BB5',
		data3: '#3B5998',
	},
	groups: [
		['data1', 'data2', 'data3' ]
	]
	},
	grid: {
		x: {
			show: true
		},
		y: {
			show: true
		}
	}
});

// C3 Chart 11
var chart11 = c3.generate({
	bindto: '#scatterPlot',
	data: {
		xs: {
			Male: 'male_x',
			Female: 'female_x',
		},
		columns: [
			["male_x", 3.5, 3.0, 3.2, 3.1, 3.6, 3.9, 3.4, 3.4, 2.9, 3.1, 3.7, 3.4, 3.0, 3.0, 4.0, 4.4, 3.9, 3.5, 3.8, 3.8, 3.4, 3.7, 3.6, 3.3, 3.4, 3.0, 3.4, 3.5, 3.4, 3.2, 3.1, 3.4, 4.1, 4.2, 3.1, 3.2, 3.5, 3.6, 3.0, 3.4, 3.5, 2.3, 3.2, 3.5, 3.8, 3.0, 3.8, 3.2, 3.7, 3.3],
			["female_x", 3.2, 3.2, 3.1, 2.3, 2.8, 2.8, 3.3, 2.4, 2.9, 2.7, 2.0, 3.0, 2.2, 2.9, 2.9, 3.1, 3.0, 2.7, 2.2, 2.5, 3.2, 2.8, 2.5, 2.8, 2.9, 3.0, 2.8, 3.0, 2.9, 2.6, 2.4, 2.4, 2.7, 2.7, 3.0, 3.4, 3.1, 2.3, 3.0, 2.5, 2.6, 3.0, 2.6, 2.3, 2.7, 3.0, 2.9, 2.9, 2.5, 2.8],
			["Male", 0.2, 0.2, 0.2, 0.2, 0.2, 0.4, 0.3, 0.2, 0.2, 0.1, 0.2, 0.2, 0.1, 0.1, 0.2, 0.4, 0.4, 0.3, 0.3, 0.3, 0.2, 0.4, 0.2, 0.5, 0.2, 0.2, 0.4, 0.2, 0.2, 0.2, 0.2, 0.4, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.2, 0.2, 0.3, 0.3, 0.2, 0.6, 0.4, 0.3, 0.2, 0.2, 0.2, 0.2],
			["Female", 1.4, 1.5, 1.5, 1.3, 1.5, 1.3, 1.6, 1.0, 1.3, 1.4, 1.0, 1.5, 1.0, 1.4, 1.3, 1.4, 1.5, 1.0, 1.5, 1.1, 1.8, 1.3, 1.5, 1.2, 1.3, 1.4, 1.4, 1.7, 1.5, 1.0, 1.1, 1.0, 1.2, 1.6, 1.5, 1.6, 1.5, 1.3, 1.3, 1.3, 1.2, 1.4, 1.2, 1.0, 1.3, 1.2, 1.3, 1.3, 1.1, 1.3],
		],
		type: 'scatter',
		colors: {
			Male: '#E84234',
			Female: '#4286F7',
		},
	},
	axis: {
		x: {
			label: 'Male Visitors',
			tick: {
				fit: false
			}
		},
		y: {
			label: 'Female Visitors'
		}
	}
});

// C3 Chart 12
var chart12 = c3.generate({
	bindto: '#pieChart',
	data: {
		// iris data from R
		columns: [
			['Likes', 70],
			['Shares', 120],
		],
		type : 'pie',
		colors: {
			Likes: '#F9BB06',
			Shares: '#32AB52',
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	}
});

// C3 Chart 13
var chart13 = c3.generate({
	bindto: '#donutChart',
	data: {
		columns: [
			['Likes', 50],
			['Shares', 190],
			['Clicks', 110],
		],
		type : 'donut',
		colors: {
			Likes: '#F9BB06',
			Shares: '#32AB52',
			Clicks: '#4286F7',
		},
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	},
	donut: {
		title: "Clicks"
	},
});


// Widgets Page
// C3 Chart 14
var chart14 = c3.generate({
	bindto: '#advertising',
	data: {
		columns: [
			['Telivision', 30],
			['Press', 60],
			['Internet', 40],
			['Friends', 40],
			['Other', 10],
		],
		type : 'donut',
		colors: {
			Telivision: '#E84234',
			Press: '#F9BB06',
			Internet: '#32AB52',
			Friends: '#4286F7',
			Other: '#96ceb4',
		},
		
		onclick: function (d, i) { console.log("onclick", d, i); },
		onmouseover: function (d, i) { console.log("onmouseover", d, i); },
		onmouseout: function (d, i) { console.log("onmouseout", d, i); }
	},
	donut: {
		title: "Clicks",
		width: 17,
		label: {
			show: false,
		}
	},
});

// C3 Chart 15
var chart15 = c3.generate({
	bindto: '#maleVsFemale',
	data: {
		x: 'x',
		columns: [
			['x', '15', '25', '35', '45', '55'],
			['Male', 30, 200, 200, 400, 250, 120, 60],
			['Female', 130, 100, 100, 200, 50, 90, 180],
		],
		type: 'bar',
		colors: {
			Female: '#E84234',
			Male: '#4286F7'
		},
	},
	legend: {
		show: false,
	},
	axis: {
		y: {
			show: false,
			tick: {
				count: 3,
			}
		},
	},
});

// C3 Chart 16
var chart16 = c3.generate({
	bindto: '#serverRequests',
	padding: {
		top: 10,
		left: 40,
	},
	data: {
		columns: [
			['data1', 18, 22, 90, 33, 19, 21, 28, 21, 19, 43, 23, 34, 55, 43, 33, 77, 33, 87, 46, 39, 51, 32, 66, 99, 32, 54, 33, 24, 54, 22, 37, 76, 67, 89, 34, 12, 77, 99, 59, 66, 28, 77, 39, 60,  66, 99, 32, 54, 33, 24, 54, 22, 37, 76, 67, 89, 34, 12, 77, 99, 59, 66, 28, 77, 39, 60],
		],
		types: {
			data1: 'area',
		},
		names: {
			data1: 'Requests',
		},
		colors: {
			data1: '#4286F7',
		},
	},
	axis: {
		y: {
			tick: {
				count: 3,
			}
		}
	}
});

// Chart 17
var chart2 = c3.generate({
	bindto: '#sales',
	padding: {
		left: 30,
		top: 3,
	},
	data: {
		columns: [
			['Sales', 30, 200, 200, 400, 250, 70, 120, 90, 180, 330, 210],
		],
		type: 'bar',
		colors: {
			Sales: '#E84234',
		},
	},
	legend: {
		show: false,
	},
	tooltip: {
		show: false,
	},	
	axis: {
		y: {
			tick: {
				count: 2,
			}
		},
	}
});

// Chart 18
var chart2 = c3.generate({
	bindto: '#expenses',
	padding: {
		left: 30,
		top: 3,
		right: 5,
	},
	data: {
		columns: [
			['Expenses', 90, 120, 210, 290, 350, 100, 240, 90, 110, 190, 210],
		],
		type: 'bar',
		colors: {
			Expenses: '#32AB52',
		},
	},
	legend: {
		show: false,
	},
	tooltip: {
		show: false,
	},
	axis: {
		y: {
			tick: {
				count: 2,
			}
		},
	}
});

// Chart 19
var chart2 = c3.generate({
	bindto: '#profits',
	padding: {
		left: 30,
		top: 3,
		right: 5,
	},
	data: {
		columns: [
			['Profits', 220, 140, 100, 290, 380, 240, 80, 110, 180, 210, 310],
		],
		type: 'bar',
		colors: {
			Profits: '#4286F7',
		},
	},
	legend: {
		show: false,
	},
	tooltip: {
		show: false,
	},
	axis: {
		y: {
			tick: {
				count: 2,
			}
		},
	}
});
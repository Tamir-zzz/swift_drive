// Cal Heatmap 1
var weekStart = new Date();
weekStart.setDate(weekStart.getDate() - weekStart.getDay());
var ranges = d3.range(+weekStart/1000, +weekStart/1000 + 3600*24*8, 3600*20);

var max = 50;
var min = 10;

var marcData = {};

// Creating random data
ranges.map(function(element, index, array) {
  marcData[element] = Math.floor(Math.random() * (max - min) + min);
});

var cal = new CalHeatMap();
cal.init({
  itemSelector: "#cal-heatmap",
  domain: "week",
  data: marcData,
  colLimit: 7,
  cellSize: 16,
  range: 1,
  // legend: [5, 30, 40, 50],
  displayLegend: false,
  // legendHorizontalPosition: "center",
  tooltip: true,
});


// // Cal Heatmap 2
// var weekStart = new Date();
// weekStart.setDate(weekStart.getDate() - weekStart.getDay());
// var ranges = d3.range(+weekStart/1000, +weekStart/1000 + 3600*24*8, 3600*24);

// var max = 20;
// var min = 10;

// var marcData = {};

// // Creating a random data set
// ranges.map(function(element, index, array) {
//   marcData[element] = Math.floor(Math.random() * (max - min) + min);
// });

// var cal = new CalHeatMap();
// cal.init({
//   itemSelector: "#sales-heatmap",
//   domain: "week",
//   data: marcData,
//   cellSize: 12,
//   colLimit: 7,
//   itemName: ["Sale"],
//   range: 1,
//   // legend: [50, 90, 120, 250, 300, 100],
//   displayLegend: false,
//   // legendHorizontalPosition: "center",
//   tooltip: true,
// });

// // Cal Heatmap 3
// var weekStart = new Date();
// weekStart.setDate(weekStart.getDate() - weekStart.getDay());
// var ranges = d3.range(+weekStart/1000, +weekStart/1000 + 3600*24*8, 3600*24);

// var max = 35;
// var min = 25;

// var marcData = {};

// // Creating a random data set
// ranges.map(function(element, index, array) {
//   marcData[element] = Math.floor(Math.random() * (max - min) + min);
// });

// var cal = new CalHeatMap();
// cal.init({
//   itemSelector: "#expenses-heatmap",
//   domain: "week",
//   data: marcData,
//   cellSize: 12,
//   colLimit: 7,
//   itemName: ["Expense"],
//   range: 1,
//   // legend: [50, 90, 120, 250, 300, 100],
//   displayLegend: false,
//   // legendHorizontalPosition: "center",
//   tooltip: true,
// });


// // Cal Heatmap 4
// var weekStart = new Date();
// weekStart.setDate(weekStart.getDate() - weekStart.getDay());
// var ranges = d3.range(+weekStart/1000, +weekStart/1000 + 3600*24*8, 3600*24);

// var max = 50;
// var min = 45;

// var marcData = {};

// // Creating a random data set
// ranges.map(function(element, index, array) {
//   marcData[element] = Math.floor(Math.random() * (max - min) + min);
// });

// var cal = new CalHeatMap();
// cal.init({
//   itemSelector: "#profits-heatmap",
//   domain: "week",
//   data: marcData,
//   cellSize: 12,
//   colLimit: 7,
//   itemName: ["Profit"],
//   range: 1,
//   // legend: [50, 90, 120, 250, 300, 100],
//   displayLegend: false,
//   // legendHorizontalPosition: "center",
//   tooltip: true,
// });
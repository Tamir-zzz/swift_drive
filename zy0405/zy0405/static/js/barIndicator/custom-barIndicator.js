$('#defaultBar').barIndicator();



// Bar Color
var opt = {foreColor:'#e84234'};$('#barColor').barIndicator(opt);

// Bar Height
var opt = { horBarHeight:27}; $('#barHeight').barIndicator(opt);

// Vertical Height
var opt = { style:'vertical'}; $('#barVertical').barIndicator(opt);
var opt = { style:'vertical', foreColor:'#e84234'}; $('#barVertical2').barIndicator(opt);
var opt = { style:'vertical', foreColor:'#32ab52'}; $('#barVertical3').barIndicator(opt);

// Bar Holder Color
var opt = {foreColor:'#F9BB06', backColor:'#4286f7'}; $('#barHolderColor').barIndicator(opt);

// label Positions
var opt = {horLabelPos:'topRight', foreColor:'#e84234'};$('#barLabelTopRight').barIndicator(opt);
var opt = {horLabelPos:'right', foreColor:'#4286f7'};$('#barLabelRight').barIndicator(opt);
var opt = {horLabelPos:'left', foreColor:'#32ab52'};$('#barLabelLeft').barIndicator(opt);
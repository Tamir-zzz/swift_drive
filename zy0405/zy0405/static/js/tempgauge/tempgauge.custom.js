$(function(){
	if(!(/^\?noconvert/gi).test(location.search)){
		$(".tempGauge0").tempGauge({width: 90, borderWidth: 4, borderColor: "#4286F7", fillColor: "#4286F7", showLabel: true});
		$(".tempGauge1").tempGauge({width: 70, borderWidth: 4, borderColor: "#E84234", fillColor: "#E84234", showLabel: true});
		$(".tempGauge2").tempGauge({width: 50, borderWidth: 4, borderColor: "#F9BB06", fillColor: "#F9BB06", showLabel: true});
		$(".tempGauge3").tempGauge({width: 40, borderWidth: 4, borderColor: "#32AB52", fillColor: "#32AB52", showLabel: true});	
	}
});
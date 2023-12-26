$( document ).ready(function() {
	$("#mac").circliful({
			animation: 1,
			animationStep: 5,
			foregroundBorderWidth: 21,
			backgroundBorderWidth: 21,
			percent: 78,
			fontColor: '#000000',
			foregroundColor: '#E84234',
			backgroundColor: '#E2E2E2',
			multiPercentage: 1,
			percentages: [10, 20, 30]
	});
	$("#windows").circliful({
			animation: 1,
			animationStep: 5,
			foregroundBorderWidth: 21,
			backgroundBorderWidth: 21,
			percent: 48,
			fontColor: '#000000',
			foregroundColor: '#F9BB06',
			backgroundColor: '#E2E2E2',
			multiPercentage: 1,
			percentages: [10, 20, 30]
	});
	$("#linux").circliful({
			animation: 1,
			animationStep: 5,
			foregroundBorderWidth: 21,
			backgroundBorderWidth: 21,
			percent: 88,
			fontColor: '#000000',
			foregroundColor: '#32AB52',
			backgroundColor: '#E2E2E2',
			multiPercentage: 1,
			percentages: [10, 20, 30]
	});
});
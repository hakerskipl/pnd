$(document).ready(function() {
	$('.btn-search').height(function() { 
		var h = _.max($('.btn-search').closest('div.search-container').find('.btn-search'), function(elem, index, list) { return $(elem).height(); });
		return $(h).height();
	});
	$('.btn-search').each(function(){
		var preHeight = $(this).height();
		var div = $(this).children('div');
		div.css('margin-top', (preHeight-div.height())/2);
	});
});
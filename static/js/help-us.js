$(document).ready(function(){
	var activeHelper = $('.active').first().parents('.row.helper');
	console.log(activeHelper);
	$('.row.helper').on('showtime', function(){
		var sib = $(this).siblings();
		sib.find('.content').addClass('hidden');
		sib.find('.active').removeClass('active');
		$(this).find('.content').removeClass('hidden');
		$(this).find('.heads').addClass('active');
		// console.log($(this).find('.content'));
	});
	$('.row.helper').on('click', function(){
		$(this).trigger('showtime');
	});
});
$(document).ready(function(){
	var activeHelper = $('.active').first().parents('.row.helper');
	console.log(activeHelper);
	$('.row.helper').on('showtime', function(){
		var sib = $(this).siblings();
		sib.find('.content').addClass('hidden');
		sib.find('.active').removeClass('active');
		sib.find('.heads').removeClass('next');
		$(this).find('.content').removeClass('hidden');
		$(this).find('.heads').addClass('active').removeClass('next');
		$(this).next().find('.heads').addClass('next');
		// console.log($(this).find('.content'));
	});
	$('.row.helper').on('click', function(){
		$(this).trigger('showtime');
	});
});
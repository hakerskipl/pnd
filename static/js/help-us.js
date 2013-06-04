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
	$('#newsletter-singup').submit(function(event){
		event.preventDefault();
		// console.log( $(this).serializeArray() );
		$.ajax({
			url: $(this).attr('action'),
			type: 'POST',
			data: $(this).serialize(),
			dataType: 'json'
		}).done(function(data) {
			console.log(data);
			// Bład wysyłki
			if (data.answer == 0) {
				alert('0');
			}
			// Sukces
			else if (data.answer == 1) {
				var parent = $('.active').first().parents('.row.helper');
				parent.find('.heads').addClass('success');
				parent.find('.heads').removeClass('active');
				parent.find('.content').addClass('hidden');
				var sib = parent.siblings();
				sib.find('.content').addClass('hidden');
				sib.find('.next').addClass('active');
				sib.find('.next').removeClass('next');
				var newGuy = $('.active').first().parents('.row.helper');
				newGuy.find('.content').removeClass('hidden');
				newGuy.next().find('.heads').addClass('next');

				console.log(newGuy);
			}
			// Źle wypełniony formularz
			else {
				
			}
		});
		console.log(activeHelper);
	});
	
	// Like 
	FB.Event.subscribe('edge.create',
	    function(response) {
	        alert('You liked the URL: ' + response);
	    }
	);

	// Send
	FB.Event.subscribe('message.send',
	    function(response) {
	        alert('You send the URL: ' + response);
	    }
	);
});
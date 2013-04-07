$(document).ready(function() {
	$('div.radio-click').on('click', function() {
		$('div.radio-click').removeClass('checked').find('input[type="radio"]').attr('checked', false);
		$(this).addClass('checked').find('input[type="radio"]').attr('checked', true);
	});

	// Typeahead.js
	$('input.search').typeahead({
			name: 'places',
			remote: 'http://192.168.0.102:8000/pomysl/typeahead/%QUERY/'
		});
});
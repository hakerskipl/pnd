$(document).ready(function() {
	$('div.radio-click').on('click', function() {
		$('div.radio-click').removeClass('checked').find('input[type="radio"]').attr('checked', false);
		$(this).addClass('checked').find('input[type="radio"]').attr('checked', true);
	});

});
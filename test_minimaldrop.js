// Dropdowns.
	$('#nav > ul').dropotron({
		alignment: 'right',
		hideDelay: 350
	});

// Lightbox gallery.
$window.on('load', function() {

	$('#two').poptrox({
		caption: function($a) { return $a.next('h3').text(); },
		overlayColor: '#2c2c2c',
		overlayOpacity: 0.85,
		popupCloserText: '',
		popupLoaderText: '',
		selector: '.card',
		usePopupCaption: true,
		usePopupDefaultStyling: false,
		usePopupEasyClose: false,
		usePopupNav: true,
		windowMargin: (skel.breakpoint('small').active ? 0 : 50)
	});

});
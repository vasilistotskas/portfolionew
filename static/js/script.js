console.log('Its working')

var theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('light')
}else{
	setTheme(theme)
}

var themeDots = document.getElementsByClassName('theme-dot')


for (var i=0; themeDots.length > i; i++){
	themeDots[i].addEventListener('click', function(){
		var mode = this.dataset.mode
		console.log('Option clicked:', mode)
		setTheme(mode)
	})
}

function setTheme(mode){
	if(mode == 'light'){
		document.getElementById('theme-style').href = static + '/default.css'
	}

	if(mode == 'blue'){
		document.getElementById('theme-style').href = static + '/blue.css'
	}

	if(mode == 'green'){
		document.getElementById('theme-style').href = static + '/green.css'
	}

	if(mode == 'purple'){
		document.getElementById('theme-style').href = static + '/purple.css'
	}

	localStorage.setItem('theme', mode)
}

//slick slider


$('.logo-slider').slick({
    dots: true,
    arrows: false,
    infinite: true,
    speed: 500,
    fade: true,
    cssEase: 'linear',
    autoplay: true,
    speed: 1000,
    autoplayspeed:2000,
    nextArrow: '<div class="right"><i class="fa fa-angle-right"></i></div>',
    prevArrow: '<div class="left"><i class="fa fa-angle-left"></i></div>',
});

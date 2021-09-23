const menu = document.querySelector('#mobile-menu');
const menu_links = document.querySelector('.navbar-menu')

//Display Mobile Menu
const mobile_menu = () => {
    menu.classList.toggle('is-active')
    menu_links.classList.toggle('active')
}

menu.addEventListener('click', mobile_menu)


//Datetime picker
flatpickr("input[id=date]",{
    dateFormat: "d-m-Y",
})

flatpickr("input[id=time]",{
    enableTime: true,
    noCalendar: true,
    dataFormat: "H:i",
})

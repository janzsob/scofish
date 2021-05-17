const mainNavigation = document.querySelector(".main-navigation");
const overlay = mainNavigation.querySelector(".overlay"); 
const toggler = mainNavigation.querySelector(".navbar-toggler");

const openSideNav = () => mainNavigation.classList.add("active"); // add active class
const closeSideNav = () => mainNavigation.classList.remove("active");

toggler.addEventListener("click", openSideNav);
overlay.addEventListener("click", closeSideNav);

document.addEventListener("swiped-right", openSideNav);
document.addEventListener("swiped-left", closeSideNav);
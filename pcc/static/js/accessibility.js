// static/js/accessibility.js

document.addEventListener('DOMContentLoaded', function () {
    const toggleContrastLink = document.querySelector('.toggle-contrast-link');
    const increaseFontLink = document.querySelector('.increase-font');
    const decreaseFontLink = document.querySelector('.decrease-font');

    toggleContrastLink.addEventListener('click', function (event) {
        event.preventDefault();
        document.body.classList.toggle('high-contrast');
        document.querySelector('header').classList.toggle('high-contrast');
        document.querySelector('footer').classList.toggle('high-contrast');
        document.querySelector('.redirect').classList.toggle('high-contrast');
        document.querySelectorAll('.login a').forEach(item => {
            item.classList.toggle('high-contrast');
        });
        document.querySelector('.login .dropdown-content').classList.toggle('high-contrast');
        document.querySelectorAll('.login .dropdown-content a').forEach(item => {
            item.classList.toggle('high-contrast');
        });
        document.querySelector('.login .fa-caret-down').classList.toggle('high-contrast');
        document.querySelector('.login .fa-user').classList.toggle('high-contrast');
        document.querySelectorAll('.controls button').forEach(button => {
            button.classList.toggle('high-contrast');
        });
        document.querySelector('.footer-links').classList.toggle('high-contrast');
    });

    let fontSize = 16;
    const maxFontSize = 26;

    increaseFontLink.addEventListener('click', function (event) {
        event.preventDefault();
        if (fontSize < maxFontSize) {
            fontSize += 2;
            document.body.style.fontSize = fontSize + 'px';
        }
    });

    decreaseFontLink.addEventListener('click', function (event) {
        event.preventDefault();
        if (fontSize > 12) {
            fontSize -= 2;
            document.body.style.fontSize = fontSize + 'px';
        }
    });
});

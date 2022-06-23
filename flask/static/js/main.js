$('#menu')
.append('<a href="#menu" class="close"></a>')
.appendTo($body)
.panel({
    delay: 500,
    hideOnClick: true,
    hideOnSwipe: true,
    resetScroll: true,
    resetForms: true,
    side: 'right',
    target: $body,
    visibleClass: 'is-menu-visible'
});
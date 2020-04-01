// Add event handlers for Google Analytics

$(document).ready(function () {
    // Trigger article read event if article scrolled to the bottom and been on page for at least 60 seconds
    var start = new Date();
    setTimeout(function () {
        var finishedArticleWaypoint = new Waypoint({
            element: document.getElementById('finished-article'),
            handler: function (direction) {
                console.log("You finished reading the article!");
                var end = new Date();
                ga('send', 'event', 'article', 'read', this.element.getAttribute('article'), (end - start) / 1000);
                finishedArticleWaypoint.disable();
            },
            offset: 'bottom-in-view'
        });
    }, 60 * 1000);

    // Trigger code copied event when a user highlights some code and copies to the clipboard
    window.addEventListener("copy", function () {
        var parentElement = window.getSelection().getRangeAt(0).commonAncestorContainer;
        if (parentElement.localName === 'code') {
            ga('send', 'event', 'code', 'copied', parentElement.getAttribute('data-lang'));
        }
    });
});
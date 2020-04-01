$(document).ready(function () {
    // Add page anchor links to heading elements
    $('span[itemprop="articleBody"] h2, h3, h4, h5, h6').each(function () {
        $(this).append('<a class="heading-page-anchor" href="#' + $(this).attr('id') + '"><i class="fas fa-link"></i></a>');
    });
});
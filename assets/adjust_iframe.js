// Place this in your assets folder under adjust_iframe.js
window.addEventListener('load', function() {
    adjustIframeHeight();
});

function adjustIframeHeight() {
    const iframe = document.getElementById('graph-display');
    if (iframe) {
        iframe.onload = function() {
            var doc = iframe.contentDocument ? iframe.contentDocument : iframe.contentWindow.document;
            var height = Math.max(doc.documentElement.scrollHeight, doc.body.scrollHeight);
            iframe.style.height = `${height}px`; // Set iframe height based on content
        };
    }
}

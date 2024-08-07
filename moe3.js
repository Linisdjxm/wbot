(function($, mw) {
    $(function() {
        document.getElementById('mw-content-text').innerHTML = document.getElementById('mw-content-text').innerHTML.replace(' patroller-show','');
        // Create portlet link
        var portletLinkOnline = mw.util.addPortletLink(
                'p-cactions',
                '#',
                '检视页面最新版本');

        var api = new mw.Api();
        if(document.querySelector('.' + 'permissions-errors') != null)
        {
            var htextx = document.querySelector('.' + 'permissions-errors').innerText.match(/#[0-9]*/)[0].substring(1);
            var params = {
                action: 'parse',
                oldid: +htextx,
                format: 'json'
            };
            api.get(params).done(data => {
                document.getElementById('mw-content-text').innerHTML = data.parse.text['*'];
                console.log("Success");
            });
        }
        // Bind click handler
        $(portletLinkOnline).find('a').click(function(e) {
            e.preventDefault();
            var params = {
                action: 'parse',
                page: mw.config.get('wgPageName'),
                format: 'json'
            };
            api.get(params).done(data => {
                document.getElementById('mw-content-text').innerHTML = data.parse.text['*'];
                console.log("Success");
            });
        });
    });
})(jQuery, mw);

(function($, mw) {
    $(function() {
        // Create portlet link
        var portletLinkOnline = mw.util.addPortletLink(
                'p-cactions',
                '#',
                'FunctionA');

        var api = new mw.Api();

        // Bind click handler
        $(portletLinkOnline).find('a').click(function(e) {
            e.preventDefault();
            var params = {
                action: 'parse',
                page: mw.config.get('wgPageName'),
                format: 'json'
            };
            api.get(params).done(data => {
                console.log(data.parse.text['*']);
            });
        });
    });
})(jQuery, mw);

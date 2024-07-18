(function($, mw) {
    $(function() {
        // Create portlet link
        var portletLinkOnline = mw.util.addPortletLink(
                'p-cactions',
                '#',
                '申请删除');

        var api = new mw.Api();

        // Bind click handler
        $(portletLinkOnline).find('a').click(function(e) {
            e.preventDefault();
            var infoB = prompt("页面:","");
            var infoA = prompt("理由:","");
            if (infoA == "")
            {
                throw("NULL")
            }
            var params = {
                action: 'edit',
                title: '萌娘百科_talk:讨论版/操作申请',
                appendtext: '\n== 申请删除图片 ==\n* ' + infoB + '\n理由：' + infoA + '~~~~',
                format: 'json'
            };
            api.postWithToken( 'csrf', params ).done( function ( data ) {
                console.log( data );
            });
        });
    });
})(jQuery, mw);

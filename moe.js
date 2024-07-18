/*
This program is free software: you can redistribute it and/or modify 
it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with this program. 
If not, see <https://www.gnu.org/licenses/>. 
*/

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
                format: 'json',
                tags: 'Automation tool',
                summary: '使用Page-In Deletion提删'
            };
            api.postWithToken( 'csrf', params ).done( function ( data ) {
                console.log( data );
            });
        });
    });
})(jQuery, mw);

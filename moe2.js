function get(obj, attr, defret) {
    return obj.hasAttribute(attr) ? obj.getAttribute(attr) : defret;
}
(function ($, mw) {
    ids = []
    function loadIDs() {
        boxes = document.getElementsByTagName("input");
        for (i = 0; i < boxes.length; ++i) {
            if (get(boxes[i], "type") === "checkbox" && boxes[i].checked) {
                var idRe = /ids\[(\d+)\]/,
                    idArr = idRe.exec(get(boxes[i], "name", ""));
                if (idArr !== null)
                    ids.push(idArr[1]);
            }
        }
    }
    function FuncX() {
        loadIDs();
        if (ids.length != 2) {
            alert("Illegal Action!");
            return null;
        }
        $.ajax({
            url: mw.util.wikiScript('api'),
            dataType: 'json',
            type: 'GET',
            data: {
                action: 'compare',
                fromrev: +ids[0],
                torev: +ids[1],
                format: 'json'
            }
        }).done(function (data) {
            console.log("Get data.");
            var newWindow = window.open("https://zh.moegirl.org.cn/Special:%E7%A9%BA%E7%99%BD%E9%A1%B5%E9%9D%A2", '_blank')
            newWindow.onload = () => {
                console.log("Catch it.");
                newWindow.document.getElementById('mw-content-text').innerHTML = '<link rel="stylesheet" href="https://www.mediawiki.org/w/load.php?modules=mediawiki.legacy.shared|mediawiki.diff.styles&only=styles">\n<table class="diff">\n<colgroup>\n<col class="diff-marker">\n<col class="diff-content">\n<col class="diff-marker">\n<col class="diff-content">\n</colgroup>\n<tbody>' + data["compare"]["*"] + '</tbody>\n</table>\n';
            };
            //console.log(data["compare"]["*"]);
        }).fail(function (jqXHR, textStatus, errorThrown) {
            console.log('Error when comparing page!');
        });

    }
    var $showDiffx = $('<button />', {
        'name': 'showDiffx',
        'type': 'button',
        'class': 'historysubmit mw-history-diffx mw-ui-button',
        'title': "比较选中的版本",
        'text': "比较选中的版本"
    });
    $showDiffx.on('click', FuncX);
    $(".historysubmit.mw-history-compareselectedversions-button").after($showDiffx);
})(jQuery, mw);

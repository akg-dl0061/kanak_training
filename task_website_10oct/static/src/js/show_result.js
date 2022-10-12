odoo.define('task_website_10oct.show_result', function(require) {
    "use strict";


    require('web.dom_ready');
    var ajax = require('web.ajax');
    var size_tr = 0;
    var limit = 0;


    $('.btn').on('click', function(ev) {
        var button_id = ev.currentTarget.id;
        ajax.jsonRpc("/show-result", 'call', { 'button_id': button_id }).then(function(result) {
            if (result) {
                $('.show_result').empty();
                $('.show_result').append(result.data);
                console.log('size_tr', ('.show_result .table tbody tr').length);
                size_tr = $('.show_result .table tbody tr').length;
            }
            limit = 5;
            $(".table tr").slice(0, 5).show();
            if (limit > size_tr) {
                $('.load_more').hide();
            }
        });
        

    });

    $(document).on('click','.load_more',function(e){
        limit= (limit+5 <= size_tr) ? limit+5 : size_tr;
        $('.table tr:lt('+limit+')').show();
        if (limit == size_tr) {
            $('.load_more').hide();
        }
    });
});
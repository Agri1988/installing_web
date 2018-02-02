/**
 * Created by Ar on 02.02.2018.
 */
$(document).ready(function () {
    var show_btn = $('#show_summory_report');
    var table = $('#summory_report_table');
    show_btn.on('click', function (event) {
        event.preventDefault()
        if (table.css('display') == 'none'){
            table.css('display','')
        }
        else {table.css('display','none')}
    })
})
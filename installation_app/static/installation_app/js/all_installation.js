$(document).ready(function () {
    //filter for columns in table
    var table = $('#table').find('tbody').find('th');
    var rows_length = document.getElementById('table').rows.length;
    console.log(rows_length);
    function filter_data(index, sample) {

        var table = document.getElementById('table');
        for (var i = 2; i < rows_length; i++) {
            if ((table.rows[i].cells[index].innerText.toLowerCase()).indexOf(sample.toLowerCase()) == -1) {
                table.rows[i].setAttribute("style", "display:none")
            }
            else if (sample != '') {
                table.rows[i].setAttribute("style", "display:")
            }
            else {
                table.rows[i].setAttribute("style", "display:")
            }
        }
    }
    table.each(function (index) {
        var input = $(this).find('input');

        input.on('input keyup', function (e) {
            console.log(input.val());
            filter_data(index, String(input.val()))
        });
    });

    var search_date = $('#search_date');
    var search_date_button = $('#search_date_button');
    var url = $('#search_form').attr('action');
    search_date_button.on('click', function (event) {
        event.preventDefault();
        if (search_date.val()!=='') {
            console.log(url + search_date.val().substr(8, 2) + '/' + search_date.val().substr(5, 2) + '/' + search_date.val().substr(0, 4));
            document.location.href = url+search_date.val().substr(8,2)+'/'+search_date.val().substr(5,2)+'/'+search_date.val().substr(0,4)
        }
        // $.ajax({
        //         url:url+search_date.val().substr(8,2)+'/'+search_date.val().substr(5,2)+'/'+search_date.val().substr(0,4),
        //         type:'POST',
        //         data:{},
        //         cache:true,
        //         success:function (){
        //             console.log('OK')
        //         },
        //         error:function () {
        //             console.log('error')
        //         }
        //     });
    })
});
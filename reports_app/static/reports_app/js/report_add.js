$(document).ready(function () {
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    var url = $('form').attr('action');
    var btn = $('#btn_accept');
    btn.on('click', function (event) {
        var month = $('#month').val();
        var year = $('#year').val();
        var employee = $('#employee').val()
        if (employee){
            event.preventDefault();
            document.location.href = url+month+'/'+year+'/'+employee
        }
        else{
            event.preventDefault();
            document.location.href = url+month+'/'+year+'/'
        }
                // console.log('hej')
        // $.ajax({
        //     url:url+month+'/'+year+'/',
        //     type:'POST',
        //     data:{month:month, year:year, csrfmiddlewaretoken:csrf},
        //     cache:true,
        //     success:function (){
        //             console.log('OK')
        //         },
        //         error:function () {
        //             console.log('error')
        //         }
        // })
    });
    console.log(csrf, url)
});
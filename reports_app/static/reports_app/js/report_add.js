$(document).ready(function () {
    var csrf = $("[name='csrfmiddlewaretoken']").val();
    var url = $('#create_month_report_form').attr('action');
    var btn = $('#btn_accept');
    btn.on('click', function (event) {
        var month = $('#month').val();
        var year = $('#year').val();
        var employee = $('#employee').val();
        var more_detail = $('#more_detail').prop("checked");
        console.log(month, year, employee);
        if (employee){
            event.preventDefault();
            if (more_detail){
                document.location.href = url+month+'/'+year+'/'+employee+'/detail/not_accepted/'
            }
            else {document.location.href = url+month+'/'+year+'/'+employee+'/'}

        }
        else{
            event.preventDefault();
            if (more_detail){
                document.location.href = url+month+'/'+year+'/detail/not_accepted/'
            }
            else {document.location.href = url+month+'/'+year+'/'}

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
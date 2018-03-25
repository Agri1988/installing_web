$(document).ready(function () {
    var car_select_field = $('#id_car');
    car_select_field.on('change', function (event) {
        event.preventDefault();
        $.ajax({
            url:'/mileage_account/get_last_mileage/'+car_select_field.val()+'/',
            type:'POST',
            data:{'csrfmiddlewaretoken':csrf},
            cash:true,
            success:function (data){
                    console.log('OK', data);
                    $('#id_start_mileage').val(data['last_mileage'])
                },
                error:function () {
                    console.log('error')
                }
        })
    })
})
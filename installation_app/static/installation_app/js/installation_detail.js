$(document).ready(function () {
    var employee_3 = $('#id_employee_3').parent();
    employee_3.after(
        '<div class="form-group-row">' +
        '<label for="show_comments">Pokaż komentarz:</label>'+
        '<input type="checkbox" class="form-control" id="show_comments">' +
        '</div>');
    var show_comments_checkbox = $('#show_comments');
    var comments = $('#id_comment').parent();
    comments.prop('style','display:none');
    show_comments_checkbox.on('click', function () {
        if(show_comments_checkbox.prop('checked')){
            comments.prop('style','display:')
        }
        else {comments.prop('style','display:none')}
    })
    var address = $('#id_success')
    address.on('click', function () {
        if ($('#installation_id').val() == '0'){
            $('[name="submit"]').trigger('click')
        }
    })
    if ($('#installation_id').val() != '0'){
        location.hash = 'add_mileage_account'
    }
});
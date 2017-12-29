$(document).ready(function () {
    var form = document.querySelectorAll('form div :not(label) ' );
    form.forEach(function(item, i, arr){
    console.log(form[i].setAttribute('class','form-control'))
});
});

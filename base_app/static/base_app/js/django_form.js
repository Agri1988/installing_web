$(document).ready(function () {
    var form = document.querySelector('form');
    form.setAttribute('role',"form");
//    form.setAttribute('class',"form-inline")
    var form = document.querySelectorAll('form div :not(label) ' );
    form.forEach(function(item, i, arr){
    console.log(form[i].setAttribute('class','form-control'))
});
});

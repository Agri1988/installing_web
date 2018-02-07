function search_data (url) {
            var form = $('#installation_search_form');
            var input = form.find('input');
            var btn = form.find('button');
            var csrf = $(document).find("[name='csrfmiddlewaretoken']").val();
            btn.on('click', function (event) {
                event.preventDefault();
                console.log(input.val());
                $.ajax({
                    url:url,
                    type:'POST',
                    data:{csrfmiddlewaretoken:csrf, input:input.val()},
                    cache:true,
                    success:function (data){
                        console.log('OK');
                        $(document).find('body').find('*').remove();
                        $(document).find('body').append(data);
                        console.log(data)
                    },
                    error:function () {
                        console.log('error')
                    }
                });
            })
        }
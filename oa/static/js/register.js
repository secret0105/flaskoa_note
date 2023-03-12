function bindEmailCaptcha(){
    $(function (){
        $("#btn-capthca").click(function (event){

            var $this = $(this);
            //阻止默认事件
            event.preventDefault();
            
            var email = $("input[name='email']").val();
            // alert(email)
            
    
            $.ajax({
                url: "/auth/mail/captcha?email=" + email,
                type: "GET",
                
                success: function(result){
                    console.log(result)
                    // var code = result['code']
                    // if(code == 200){
                    //     alert("验证码已发送")
                    // }
                    //自己实践时，没有code 只有message
                    $this.off("click")
                    var count = 5
                    var timer = setInterval(function(){
                        $this.text(count)
                        count -= 1
                        if(count <= 0){
                            clearInterval(timer)
                            $this.text("获取验证码")
                            bindEmailCaptcha()
                        }
                    },1000)

                    if(result['message'] == 'success'){
                        alert('验证码已发送')
                        
                    }
                },
                fail: function(error){
                    console.log(error)
                },

                //这里complete方法没生效
                /*complete: function(jqXHR,textStatus){
                    $this.off("click")
                    var count = 5
                    var timer = setInterval(function(){
                        $this.text(count)
                        count -= 1
                        if(count <= 0){
                            clearInterval(timer)
                            $this.text("获取验证码")
                            bindEmailCaptcha()
                        }
                    })
                },*/
    
            })
        })
    });
}

$(function(){
    bindEmailCaptcha()
});
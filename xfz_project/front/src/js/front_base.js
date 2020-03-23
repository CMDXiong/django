// 用来处理导航条
function FrontBase() {

}

FrontBase.prototype.run = function(){
    var self = this;
    self.listenAuthBoxHover();
};

FrontBase.prototype.listenAuthBoxHover = function () {
    var authBox = $(".auth-box");
    var userMoreBox = $(".user-more-box");
    authBox.hover(function () {
        userMoreBox.show();
    },function () {
        userMoreBox.hide();
    })
};

//
// $(function () {
//    $('#btn').click(function () {
//        $(".mask-wrapper").show();
//    });
//
//    $(".close-btn").click(function () {
//        $(".mask-wrapper").hide();
//
//    });
// });
//
//
// $(function () {
//    $(".switch").click(function () {
//        var srcollWrapper = $(".scroll-wrapper");
//        var currentLeft = srcollWrapper.css('left');
//        currentLeft = parseInt(currentLeft);
//        if (currentLeft<0){
//           srcollWrapper.animate({"left": '0'});
//        }else{
//            srcollWrapper.animate({"left": '-400px'});
//
//        }
//    });
// });

// 用来处理登录和注册的
function Auth() {
    var self = this;
    self.maskWrapper = $('.mask-wrapper');
    self.scrollWrapper = $(".scroll-wrapper");

}

Auth.prototype.run = function () {
    var self = this;
    self.listenShowHideEvent();
    self.listenSwitchEvent();
    self.listenSigninEvent();
    self.listenImgCaptchaEvent();
};

Auth.prototype.showEvent = function(){
    var self = this;
    self.maskWrapper.show();
};

Auth.prototype.hideEvent = function(){
    var self = this;
    self.maskWrapper.hide();
};

Auth.prototype.listenShowHideEvent = function(){
    var self = this;
    var signinBtn = $(".signin-btn");
    var signupBtn = $(".signup-btn");
    var closeBtn = $(".close-btn");
    signinBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({"left":0});
    });
    signupBtn.click(function () {
        self.showEvent();
        self.scrollWrapper.css({"left":-400});
    });

    closeBtn.click(function () {
        self.hideEvent();
    });

};

Auth.prototype.listenSwitchEvent = function(){
    var self = this;
    var switcher = $(".switch");

    switcher.click(function () {
        var currentLeft = self.scrollWrapper.css('left');
        currentLeft = parseInt(currentLeft);
        if (currentLeft<0){
            self.scrollWrapper.animate({"left": '0'});
        }else{
            self.scrollWrapper.animate({"left": '-400px'});
       }
   });
};

Auth.prototype.listenImgCaptchaEvent = function(){
    var self = this;
    var imgCaptcha = $('.img-captcha');
    imgCaptcha.click(function () {
        imgCaptcha.attr("src", "/account/img_captcha/"+"?random="+Math.random());
    });
};

Auth.prototype.listenSigninEvent = function(){
    var self = this;
    var signinGroup = $(".signin-group");
    var telephoneInput = signinGroup.find("input[name='telephone']");
    var passwordInput = signinGroup.find("input[name='password']");
    var rememberInput = signinGroup.find("input[name='remember']");
    var submitBtn = signinGroup.find(".submit-btn");
    submitBtn.click(function () {
        var telephone = telephoneInput.val();
        var password = passwordInput.val();
        var remember = rememberInput.prop("checked");

        xfzajax.post({
            'url': '/account/login/',
            'data':{
                'telephone':telephone,
                'password': password,
                'remember': remember?1:0
            },
            'success': function (result) {
                if(result['code'] === 200){
                    self.hideEvent();
                    window.location.reload();
                }else{
                    var messageObject = result['message'];
                    if (typeof messageObject === 'string' || messageObject.constructor === String){
                        window.messageBox.show(messageObject);
                    } else{
                        for(var key in messageObject){
                            var messages = messageObject[key];
                            var message = messages[0];
                            window.messageBox.show(message);
                        }
                    }
                }

            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
};

$(function () {
    var auth  = new Auth();
    auth.run();
});


$(function () {
   var frontBase = new FrontBase();
   frontBase.run();
});

$(function () {
   if(template){
       template.defaults.imports.timeSince = function (dataValue) {
            var date = new Date(dataValue);
            var datats = date.getTime();
            var nowts = (new Date()).getTime();
            var timestamp = (nowts - datats)/1000;
            if(timestamp < 60){
                return '刚刚';
            }else if (timestamp >=60 && timestamp < 60*60){
                minutes = parseInt(timestamp/60)
                return minutes+'分钟前';
            }else if (timestamp >=60*60 && timestamp < 60*60*24){
                hours = parseInt(timestamp/60/60)
                return hours+'小时前';
            }else if (timestamp >=60*60*24 && timestamp < 60*60*24*30){
                days = parseInt(timestamp/60/60/24)
                return days+'天前';
            }else{
                var year = date.getFullYear();
                var month = date.getMonth();
                var day = date.getDay();
                var hour = date.getHours();
                var minute = date.getMinutes();
                return year+'/'+month+'/'+day+' '+hour+':'+minute;
            }

       };
   }
});
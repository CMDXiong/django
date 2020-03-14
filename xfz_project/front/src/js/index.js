

function Banner() {
    this.bannerGroup = $("#banner-group");
    this.listenBannerHover();
    this.index = 0;
}

Banner.prototype.listenBannerHover = function(){
    var self = this;
    this.bannerGroup.hover(function () {
       // 第一个函数是把鼠标移动到banner上会执行的函数
        clearInterval(self.timer);
    }, function () {
       // 第二个函数是把鼠标从banner上移走会执行的函数
        self.loop();
    });
};

Banner.prototype.loop = function(){
    var self = this;
    var bannerUI = $("#banner-ul");
    this.timer = setInterval(function () {
        if(self.index >=3){
            self.index = 0;
        }else {
            self.index++;
        }
        bannerUI.animate({"left":-798*self.index}, 500);

    }, 2000);

    // clearInterval(timer);
};


Banner.prototype.run = function () {
    this.loop();

};

// 保证在html加载完成后，再执行括号内的函数
$(function () {
   var banner = new Banner();
   banner.run();
});
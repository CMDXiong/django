

function Banner() {
    this.bannerGroup = $("#banner-group");
    this.index = 0;
    this.leftArrow = $(".left-arrow");
    this.rightArrow = $(".right-arrow");
    this.bannerUI = $("#banner-ul");
    this.liList = this.bannerUI.children('li');
    this.bannercount = this.liList.length;
    this.listenBannerHover();

}

Banner.prototype.listenBannerHover = function(){
    var self = this;
    this.bannerGroup.hover(function () {
       // 第一个函数是把鼠标移动到banner上会执行的函数
        clearInterval(self.timer);
        self.toggerArrow(true);
    }, function () {
       // 第二个函数是把鼠标从banner上移走会执行的函数
        self.loop();
        self.toggerArrow(false);
    });
};

Banner.prototype.toggerArrow = function(isShow){
    var self = this;
    if(isShow){
        self.leftArrow.show();
        self.rightArrow.show();
    }else{
        self.leftArrow.hide();
        self.rightArrow.hide();
    }

};

Banner.prototype.animate = function(){
    this.bannerUI.animate({"left":-798*this.index}, 500);

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
        self.animate();
    }, 2000);

    // clearInterval(timer);
};

Banner.prototype.listenArrowClick = function(){
    var self = this;
    self.leftArrow.click(function () {
        if (self.index === 0){
            self.index = self.bannercount-1;
        }else{
            self.index--;
        }

        self.animate();
    });
    self.rightArrow.click(function () {
        if (self.index === self.bannercount-1 ){
            self.index = 0;
        }else{
            self.index++;
        }

        self.animate();
    });
};


Banner.prototype.run = function () {
    console.log('running...');
    this.loop();
    this.listenArrowClick();

};

// 保证在html加载完成后，再执行括号内的函数
$(function () {
   var banner = new Banner();
   banner.run();
});
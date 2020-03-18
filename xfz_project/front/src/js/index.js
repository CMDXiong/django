

function Banner() {
    this.bannerWidth = 798;
    this.bannerGroup = $("#banner-group");
    this.index = 1;
    this.leftArrow = $(".left-arrow");
    this.rightArrow = $(".right-arrow");
    this.bannerUI = $("#banner-ul");
    this.liList = this.bannerUI.children('li');
    this.bannercount = this.liList.length;
    this.pageControl = $(".page-control");
}

Banner.prototype.initBanner = function(){
    var self = this;
    var firstBanner = self.liList.eq(0).clone();
    var lastBanner = self.liList.eq(self.bannercount-1).clone();
    self.bannerUI.prepend(lastBanner);
    self.bannerUI.append(firstBanner);
    self.bannerUI.css({'width':(self.bannercount+2)*self.bannerWidth, 'left': -self.bannerWidth});
};

Banner.prototype.initPageControl = function(){
    var self = this;
    for(var i=0; i<self.bannercount; i++) {
        var circle = $("<li></li>");
        self.pageControl.append(circle);
        if(i === 0){
            circle.addClass('active');
        }
    }

    // self.pageControl.css({'width': self.bannercount*(16+10)})
    self.pageControl.css({'width': self.bannercount*12+8*2+16*(self.bannercount-1)})
};

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
    var self = this;
    self.bannerUI.stop().animate({"left":-798*self.index}, 500);
    var index = self.index;
    if(index === 0){
        index = self.bannercount-1;
    }else if (index === self.bannercount+1){
        index = 0;
    }else{
        index = self.index - 1;
    }

    self.pageControl.children().eq(index).addClass('active').siblings().removeClass('active');

};

Banner.prototype.loop = function(){
    var self = this;
    var bannerUI = $("#banner-ul");
    this.timer = setInterval(function () {
        if(self.index >= self.bannercount+1){
            self.bannerUI.css({'left': -self.bannerWidth});
            self.index = 2;
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
            self.bannerUI.css({'left':-self.bannerWidth*self.bannercount});
            self.index = self.bannercount-1;
        }else{
            self.index--;
        }

        self.animate();
    });
    self.rightArrow.click(function () {
        if (self.index === self.bannercount+1 ){
            self.bannerUI.css({'left':-self.bannerWidth});
            self.index = 2;
        }else{
            self.index++;
        }

        self.animate();
    });
};

Banner.prototype.listenPageControl = function(){
    var self = this;
    self.pageControl.children('li').each(function (index, obj) {
        $(obj).click(function () {
            self.index = index+1;  // 与源代码不一致
            self.animate();

        });
    })
};



Banner.prototype.run = function () {

    console.log('running...');
    this.initBanner();
    this.initPageControl();

    this.loop();
    this.listenBannerHover();
    this.listenArrowClick();
    this.listenPageControl();

};

// 保证在html加载完成后，再执行括号内的函数
$(function () {
   var banner = new Banner();
   banner.run();
});
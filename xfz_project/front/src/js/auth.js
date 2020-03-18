
$(function () {
   $('#btn').click(function () {
       $(".mask-wrapper").show();
   });

   $(".close-btn").click(function () {
       $(".mask-wrapper").hide();

   });
});


$(function () {
   $(".switch").click(function () {
       var srcollWrapper = $(".scroll-wrapper");
       var currentLeft = srcollWrapper.css('left');
       currentLeft = parseInt(currentLeft);
       if (currentLeft<0){
          srcollWrapper.animate({"left": '0'});
       }else{
           srcollWrapper.animate({"left": '-400px'});

       }
   });
});
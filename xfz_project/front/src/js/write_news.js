function News() {

}


News.prototype.run = function () {
    var self = this;
    self.listenUploadFileEvent();

};

News.prototype.listenUploadFileEvent = function () {
    var uploadBtn = $("#thumbnail-btn");
    uploadBtn.change(function () {
        var file = uploadBtn[0].files[0];
        var formData = new FormData();
        formData.append('file', file);
        xfzajax.post({
            'url':'/cms/upload_file/',
            'data': formData,
            'processData':false,
            'contentType': false,
            'success': function (result) {
                if(result['code'] === 200){
                    var url = result['data']['url'];
                    console.log(url);
                    var thumbnailInput = $("#thumbnail-form")
                    thumbnailInput.val(url);
                }
            },
        });

    });
};

$(function () {
   var news = new News();
   news.run();
});
function News() {

}

News.prototype.initUEditor = function(){
    window.ue = UE.getEditor('editor', {
        'initialFrameHeight': 400,
        'serverUrl':'/ueditor/upload/'
    });

};


News.prototype.run = function () {
    var self = this;
    // self.listenUploadFileEvent();
    self.listenQiniuUploadFileEvent();
    self.initUEditor();
    self.listenSubmitEvent();

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

News.prototype.listenQiniuUploadFileEvent = function(){
    var self = this;
    var uploadBtn = $("#thumbnail-btn");
    uploadBtn.change(function () {
        var file  = this.files[0];
        xfzajax.get({
            'url': '/cms/qntoken/',
            'success': function (result) {
                if(result['code'] === 200){
                    var token = result['data']['token']
                    var key = (new Date()).getTime() + '.' + file.name.split('.')[1];
                    var putExtra = {
                        fname: key,
                        params:{},
                        mimeType:['image/png', 'image/jpeg', 'image/fig']
                    };
                    var config = {
                        useCdnDomain: true,
                        retryCount: 6,
                        region: qiniu.region.z0,

                    };

                    var observable = qiniu.upload(file, key, token, putExtra, config);
                    observable.subscribe({
                        'next': self.handleFileUploadProgress,
                        'error': self.handleFileUploadError,
                        'complete': self.handleFileUploadComplete
                    });
                }

            }
        })
    });
};

News.prototype.handleFileUploadProgress = function(response){
    var progressGroup = News.progressGroup;
    var progressBar = $(".progress-bar");
    progressBar.css({'width':'0'});
    progressBar.text('0%');
    var total = response.total;
    var percent = total.percent;
    var percentText = percent.toFixed(0)+'%';

    progressGroup.show();

    progressBar.css({'width':percentText});
    progressBar.text(percentText);
};

News.prototype.handleFileUploadError = function(error){
    console.log(error.message);
    var progressGroup = $("#progress-group");
    progressGroup.hide();
};

News.prototype.handleFileUploadComplete = function(response){
    var progressGroup = $("#progress-group");
    progressGroup.hide();
    var domain = 'http://q7jhogfwy.bkt.clouddn.com/';
    var filename = response.key;
    var url = domain + filename;
    var thumbnailInput = $("input[name='thumbnail']");
    thumbnailInput.val(url);
};

News.prototype.listenSubmitEvent = function(){
    var submitBtn = $("#submit-btn");
    submitBtn.click(function (event) {
        event.preventDefault();
        var btn = $(this);
        var pk = btn.attr('data-news-id');
        var title = $("input[name='title']").val();
        var category = $("select[name='category']").val();
        var desc = $("input[name='desc']").val();
        var thumbnail = $("input[name='thumbnail']").val();
        var content = window.ue.getContent();
        var url = '';
        if(pk){
            url = '/cms/edit_news/';
        }else {
            url = '/cms/write_news/';
        }


        xfzajax.post({
            'url': url,
            'data': {
                'title': title,
                'category': category,
                'desc': desc,
                'thumbnail': thumbnail,
                'content': content,
                'pk': pk
            },
            'success': function (result) {
                if (result['code'] === 200){
                    xfzalert.alertSuccess('恭喜！新闻发表成功', function () {
                        window.location.reload();
                    });
                }

            }
        });
    });


};

$(function () {
   var news = new News();
   news.run();
   News.progressGroup = $("#progress-group");
});
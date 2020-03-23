function NewsList(){
    var self = this;
}

NewsList.prototype.listenSubmitEvent = function () {
    var self = this;
    var submitBtn = $(".submit-btn");
    var textarea = $("textarea[name='comment']");
    submitBtn.click(function () {
        // data-news-id
        var content = textarea.val();
        console.log(content);
        var news_id = submitBtn.attr('data-news-id');
        xfzajax.post({
           'url': '/news/public_comment/',
           'data':{
               'content': content,
               'news_id': news_id
           },
            'success': function (result) {
                if(result['code'] === 200){
                    var comment = result['data'];
                    var tpl = template('comment-item',{'comment':comment});
                    var commentListGroup = $(".comment-list");
                    commentListGroup.prepend(tpl);
                    window.messageBox.showSuccess("评论成功");
                    textarea.val("");
                }
            }

        });
    });
};

NewsList.prototype.run = function () {
    var self = this;
    self.listenSubmitEvent();
};

$(function () {
    var newList = new NewsList();
    newList.run();
});
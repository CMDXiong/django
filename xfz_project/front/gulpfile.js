
var gulp = require("gulp");
var cssnano = require("gulp-cssnano");
var rename = require("gulp-rename");
var uglify = require("gulp-uglify");
var concat = require("gulp-concat");
var sass = require("gulp-sass");
var bs = require("browser-sync").create();
// var imagemin = require("gulp-imagemin");
// var cache = require("gulp-cache");

// 放所有的路径
var path = {
	'html':'./templates/**/',
    'css':'./src/css/',
    'js':'./src/js/',
    'images':'./src/images/',

    'css_dist':'./dist/css/',
    'js_dist':'./dist/js/',
    'images_dist':'./dist/images/'
};

// 处理html文件的任务
gulp.task("html", function(){
	gulp.src(path.html + '*.html')
	    .pipe(bs.stream())
});

// 定义一个css任务
// gulp.task("css", function(){
// 	gulp.src(path.css + '*.css')
//         .pipe(cssnano())
// 	    .pipe(rename({"suffix":".min"}))
// 	    .pipe(gulp.dest(path.css_dist))
// 	    .pipe(bs.stream())
// });

gulp.task("css", function(){
	gulp.src(path.css + '*.scss')
		.pipe(sass().on("error", sass.logError))
        .pipe(cssnano())
	    .pipe(rename({"suffix":".min"}))
	    .pipe(gulp.dest(path.css_dist))
	    .pipe(bs.stream())
});

// 定义一个js任务
gulp.task("js", function(){
	gulp.src(path.js + '*.js')
        .pipe(uglify())
	    .pipe(rename({"suffix":".min"}))
	    .pipe(gulp.dest(path.js_dist))
	    .pipe(bs.stream())
});

// 定义一个处理图片的任务
// gulp.task("images", function(){
// 	gulp.src(path.images + '*.*')
//         .pipe(cache(imagemin()))
// 	    .pipe(gulp.dest(path.images_dist))
// 	    .pipe(bs.stream())
// });

// 定义监听文件修改的任务
gulp.task("watch",function(){
	gulp.watch(path.html + "*.html", ['html']);
	gulp.watch(path.css + "*.scss",['css']);
	gulp.watch(path.js + '*.js', ['js']);
	// gulp.watch(path.images + '*.*', ['images']);
});

// 初始化browser-sycn任务
gulp.task("bs", function(){
	bs.init({
		'server':{
			'baseDir':'./'
		}
	});
});

// 创建一个默认的任务
gulp.task("default", ['bs', 'watch']);
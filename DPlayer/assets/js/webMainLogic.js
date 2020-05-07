function getQueryVariable(variable) {                                            //获取参数(function from https://www.runoob.com )
    var query = window.location.search.substring(1);
    var vars = query.split("&");
    for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
            return pair[1];
        }
    }
    return (false);
}

function getVariable(variable)                                                 //返回变量字符串
{
    if (getQueryVariable(variable))                                              //检查url中变量是否存在，存在即返回值，否则执行else
    {
        return getQueryVariable(variable);
    }
    else {
        if (variable == "vidtype") {                                                //vidtype未指定时返回“自动”
            var vidtype = "auto";
            return vidtype;
        }
        else if (variable == "vidurl") {                                            //vidurl的值未指定时返回的链接（默认播放）
            var defaultVidUrl = 'https://consumer.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/p40-pro-plus/images/intro/tvc/video-e-plus.webm';
            return defaultVidUrl;
        }
        else if (variable == "picurl" && getQueryVariable("vidurl") == false)    //picurl的值未指定时返回的链接（默认展示图）
        {
            var defaultPicUrl = 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/p40-pro-plus/images/design/design-intro-e-plus.jpg';
            return defaultPicUrl;
        }
        else if (variable == "autoplay")                                            //自动播放相关
        {
            return (false);
        }
        else if (variable == "live")                                                //直播相关
        {
            return (false);
        }
        else if (variable == "suburl" && getQueryVariable("vidurl") == false)        //字幕相关,可用cdn加速
        {
            var defaultSubUrl = 'asset/demoSubtitle_en.vtt';
            return defaultSubUrl;
        }
        else if (variable == "webtitle")                                                //页面title相关
        {
            var defaultWebTitle = 'DPlayer';
            return defaultWebTitle;
        }
        else {
            return (true);
        }
    }
}

function getContextMenu()                                                           //返回右键的自定义功能目录（数组）
{
    var contextMenu = [];
    if (getQueryVariable("vidurl") == false)                                     //如果url中的vidurl参数为空，则返回默认menu
    {
        contextMenu[0] = {
            text: "HUAWEI Vision X65",
            click: (player) => {
                dp.notice('Switch to : HUAWEI Vision X65', 2000);                               //显示通知（string，time）时间单位毫秒
                dp.switchVideo(
                    {
                        url: 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/greate-china/cn/mkt/pdp/visions/plato/media/tvc.mp4',
                        pic: 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/greate-china/cn/mkt/pdp/visions/plato/img/pc/huawei-vision-x65.jpg',
                        //thumbnails: 'example.jpg',
                    },
                    {
                        //id: 'test',
                        //api: 'https://api.prprpr.me/dplayer/',
                        //maximum: 3000,
                        //user: 'DIYgod',
                    });
            },
        };
        contextMenu[1] = {
            text: "HUAWEI MatePad Pro",
            click: (player) => {
                dp.notice("Switch to : HUAWEI MatePad Pro", 2000);                              //显示通知（string，time）时间单位毫秒
                dp.switchVideo(
                    {
                        url: 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/tablets/matepad-pro/img/video/huawei-matepad-pro-all-video.mp4',
                        pic: 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/greate-china/cn/mkt/pdp/tablets/matepad-pro/img/pc/huawei-matepad-pro-kv-pc-1@2x.jpg',
                        //thumbnails: 'example.jpg',
                    },
                    {
                        //id: 'test',
                        //api: 'https://api.prprpr.me/dplayer/',
                        //maximum: 3000,
                        //user: 'DIYgod',
                    });
            },

        };
        contextMenu[2] = {
            text: "HUAWEI P40 Pro+",
            click: (player) => {
                dp.notice("Switch to : HUAWEI P40 Pro+", 2000);                              //显示通知（string，time）时间单位毫秒
                dp.switchVideo(
                    {
                        url: 'https://consumer.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/p40-pro-plus/images/intro/tvc/video-e-plus.webm',
                        pic: 'https://consumer-img.huawei.com/content/dam/huawei-cbg-site/common/mkt/pdp/phones/p40-pro-plus/images/design/design-intro-e-plus.jpg',
                        //thumbnails: 'example.jpg',
                    },
                    {
                        //id: 'test',
                        //api: 'https://api.prprpr.me/dplayer/',
                        //maximum: 3000,
                        //user: 'DIYgod',
                    });
            },

        };
        contextMenu[3] = {
            text: "Instructions",
            link: "https://github.com/MoChanBW/CDN/tree/master/DPlayer",
        };
        return contextMenu;
    }
    else {
        return contextMenu;                                                            //返回一个空数组
    }
}

function getTrueorF(key) {                                                            //根据url中的1或0返回布伦值,默认true
    if (getVariable(key) == "1") {
        return (true);
    }
    else {
        return (false);
    }
}

function getTorFalse(key) {                                                           //根据url中的1或0返回布伦值,默认false
    if (getVariable(key) == "0") {
        return (false);
    }
    else {
        return (true);
    }
}

(function writeWebTitle() {                                                         //获取url中webtitle的参数并写入<title>
    if (getVariable("webtitle")) {
        var webTitle = getVariable("webtitle");
        document.title = webTitle;
    }
})();

//window.onfocus = function () {                                                      //标签页焦点更改
//    document.title = '恢复正常了...';
//   };
//   window.onblur = function () {
//    document.title = '快回来~页面崩溃了';
//   };


function getBrowserLang() {                                                                  //from https://blog.csdn.net/qq_26212731/java/article/details/78457198
    var lang = navigator.language || navigator.userLanguage;                            //常规浏览器语言和IE浏览器
    if (lang == 'zh-tw' || lang == 'zh-hk') {
        return 'zh-tw';
    }
    else if (lang.substring(0, 2) == 'zh') {
        return 'zh-cn';
    }
    else {
        return 'en'
    }
}

const dp = new DPlayer({												//DPlayer主控制函数,详见 http://dplayer.js.org
    container: document.getElementById('dplayer'),
    screenshot: true,
    live: getTorFalse("live"),                                          //是否开启直播模式
    autoplay: getTorFalse("autoplay"),									//自动播放 参数autoplay 值为1或0 默认false
    theme: '#8470FF',
    loop: false,
    lang: getBrowserLang(),
    screenshot: true,
    hotkey: true,
    preload: 'auto',
    logo: 'https://i.loli.net/2020/03/26/NeFKlai9bECDOIA.png',          //67% 不透明度左上角icon
    volume: 0.7,
    mutex: true,
    video: {
        url: getVariable("vidurl"),                                     //视频链接
        pic: getVariable("picurl"),
        thumbnails: getVariable("thumburl"),
        type: getVariable("vidtype"),                                   //视频类型(flv.mp4.hls.dash)(magnet在链接中用不了)
    },
    subtitle: {
        url: getVariable("suburl"),                                     //字幕链接，vtt格式
        type: 'webvtt',
        fontSize: '25px',
        bottom: '10%',
        color: '#b7daff',
    },
    //danmaku: {
    // id: '9E2E3368B56CDBB4',
    // api: 'https://api.prprpr.me/dplayer/',
    // token: 'tokendemo',
    //  maximum: 1000,
    //  addition: ['https://api.prprpr.me/dplayer/v3/bilibili?aid=4157142'],
    //  user: 'DIYgod',
    // bottom: '15%',
    // unlimited: true,
    // },
    contextmenu: getContextMenu(),                                      //默认contextMenu,自定义功能稍后添加
    //highlight: [
    //    {
    //        text: 'marker for 20s',
    //         time: 20,
    //   },
    //   {
    //        text: 'marker for 2mins',
    //        time: 120,
    //    },
    // ],
});


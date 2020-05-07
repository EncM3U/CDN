function transformRadian(inp) {  //角度转换为弧度
	var pi = Math.PI;
	return inp * pi / 180;
}

function transformSpaceRectangular(R, latitude, longitude) {  //将经纬度转化为空间直角坐标系，数组输出

	// 角度转弧度
	var Theta = transformRadian(90 - latitude);   //纬度转化为天顶角θ

	if (longitude < 0) {   //数据格式化：西经 格式化到180~360 范围内
		var longitude = longitude + 360;
	}
	var phi = transformRadian(longitude);

	var x = R * Math.sin(Theta) * Math.cos(phi);
	var y = R * Math.sin(Theta) * Math.sin(phi);
	var z = R * Math.cos(Theta);
	var spaceArray = new Array();
	spaceArray = [x, y, z];
	return spaceArray;
}

function calculate(usrloc, svloc) {  //输入用户位置和服务器位置（空间直角坐标系），输出球面距离（优弧长）
	var cosine = ((usrloc[0] * svloc[0]) + (usrloc[1] * svloc[1]) + (usrloc[2] * svloc[2])) / (Math.sqrt(Math.pow(usrloc[0], 2) + Math.pow(usrloc[1], 2) + Math.pow(usrloc[2], 2)) * Math.sqrt(Math.pow(svloc[0], 2) + Math.pow(svloc[1], 2) + Math.pow(svloc[2], 2)));
	var arccos = Math.acos(cosine);
	var sphericalDistance = arccos * 6371;
	return sphericalDistance;
}

function geoip(json) {
	var usrlatitude = json.latitude;  //更多信息：https://geojs.io/
	var usrlongtitude = json.longitude; //通过GeoJs获取json信息 举例：<script async src="https://get.geojs.io/v1/ip/geo.js">
	var usrcountrycode = json.country_code;
	//地球半径6371km
	//(6371,纬度,经度)
	//(R,latitude,longitude)
	if (usrcountrycode == "CN") {  //如果用户在境内
		var usrloc = transformSpaceRectangular(6371, usrlatitude, usrlongtitude);   //用户所在地理位置(球坐标)
		var svlocs = new Array();
		svlocs[0] = transformSpaceRectangular(6371, 34.7725, 113.7266); // cnsh 上海服务器地理位置 球坐标
		svlocs[1] = transformSpaceRectangular(6371, 1.3667, 103.8); // apsg  新加坡服务器
		svlocs[2] = transformSpaceRectangular(6371, 23.12911, 113.264385); // cngz  广州服务器
		var distance = new Array();  //初始化 距离 为数组
		for (var i = 0; i < svlocs.length; i++) {
			svloc = svlocs[i];
			distance[i] = calculate(usrloc, svloc);//计算用户与服务器距离，并按编号填入
		}
		var num = distance.indexOf(Math.min.apply(Math, distance));
		var server = ['https://mijisou.com/?q=上海', 'https://mijisou.com/?q=新加坡', 'https://mijisou.com/?q=广州']; //把重定向的链接以数组形式填进去(境内)（示例）
		location.href = server[num]; //重定向到最近的服务器
	}
	else {   //如果用户在境外
		var usrloc = transformSpaceRectangular(6371, usrlatitude, usrlongtitude);   //用户所在地理位置(球坐标)
		var svlocs = new Array();
		svlocs[0] = transformSpaceRectangular(6371, 1.3667, 103.8); // apsg 新加坡
		svlocs[1] = transformSpaceRectangular(6371, 34.7725, 113.7266); // cnsh  上海
		var distance = new Array();

		for (var i = 0; i < svlocs.length; i++) {
			svloc = svlocs[i];
			distance[i] = calculate(usrloc, svloc);  //计算用户与服务器距离，并按编号填入
		}

		var num = distance.indexOf(Math.min.apply(Math, distance));  //获得距离最小值对应的服务器编号
		var server = ['https://mijisou.com/?q=新加坡', 'https://mijisou.com/?q=上海'];//把重定向的链接以数组形式填进去 （境外）
		location.href = server[num];  //重定向到最近的服务器
	}

} 

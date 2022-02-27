# rpi-scan
使用树莓派+激光雷达扫描并成看见点阵图像  
使用方法：  
  
    apt install -y python3 python3-pip
记得给pip3换源  
	sudo mkdir ~/.pip  
    ls .pip  
    sudo vi pip.conf  
输入以下内容  
	[global]  
	timeout = 10  
	index-url =  http://mirrors.aliyun.com/pypi/simple/  
	extra-index-url= http://pypi.douban.com/simple/  
	[install]  
	trusted-host=  
        mirrors.aliyun.com  
		ypi.douban.com

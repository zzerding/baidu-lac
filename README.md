# baidu-lac
百度NLP：分词，词性标注，命名实体识别，词重要性的docker布署文件;集成flask genven 

[toc]

## install
### 1. install docker and docker-compose

### 2. download docker-compose.yml ,you can select wget or git
*  wget https://raw.githubusercontent.com/zzerding/baidu-lac/main/docker-compose.yml 
*  git clone https://github.com/zzerding/baidu-lac 

### 3. build and start

* ``` docker-compose up -d```
## http post
> METHOD:POST, {text:"seg text",password:"zzerd.com"} 

* 127.0.0.1:3001/seg
* 127.0.0.1:3001/lac
* 127.0.0.1:3001/rank

* ```curl -d'text=hello baidu lac&&password=zzerd.com' 127.0.0.1:3001/reg```

## change listen ip address and port
* change docker_compose.yml ```GEVENT_ADDRESS=0.0.0.0``` ,```GEVENT_PORT=3001``` ,```PASSWORD=zzerd.com```

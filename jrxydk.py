# -*- coding: utf-8 -*-
import requests
import json
import datetime

__G_Cpdaily_Extension = ''
__G_MOD_AUTH_CAS= ''

def task1():
  url = "https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/collector/queryCollectorProcessingList?Host= ahnu.cpdaily.com&Connection= keep-alive&Content-Length= 29&accept= application/json, text/plain, */*&Origin= https://ahnu.cpdaily.com&x-requested-with= XMLHttpRequest&User-Agent= Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 yiban/8.1.13 cpdaily/8.1.13 wisedu/8.1.13&content-type= application/json&Referer= https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html&Accept-Encoding= gzip,deflate&Accept-Language= zh-CN,en-US;q=0.8&Cookie= acw_tc=781bad3115970659948407638e7815007c1273f95121edb66eb62b38bec9b1; MOD_AUTH_CAS="+__G_MOD_AUTH_CAS+" clientType=cpdaily_student; tenantId=ahnu; sessionToken=60172bac-9191-441e-88b8-8c3220ac59b8"

  payload = "{\"pageSize\":6,\"pageNumber\":1}"
  headers = {
    'Host': 'ahnu.cpdaily.com',
    'Connection': 'keep-alive',
    'Content-Length': '29',
    'accept': 'application/json, text/plain, */*',
    'Origin': 'https://ahnu.cpdaily.com',
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 yiban/8.1.13 cpdaily/8.1.13 wisedu/8.1.13',
    'content-type': 'application/json',
    'Referer': 'https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': 'acw_tc=781bad3115970659948407638e7815007c1273f95121edb66eb62b38bec9b1; MOD_AUTH_CAS='+__G_MOD_AUTH_CAS+' clientType=cpdaily_student; tenantId=ahnu; sessionToken=60172bac-9191-441e-88b8-8c3220ac59b8'
  }

  response = requests.request("POST", url, headers=headers, data = payload)
  print(response.text)
  src = json.loads(response.text)

  if (src["datas"]["rows"] == []):#没有任务
      return [1, 1]
  if(src["datas"]["rows"][0]['isHandled'] == 1):#任务已经提交
      return [1, 1]
  # if(src["datas"]["rows"][0] ==  ):
  #     return [1,1]
  return [src["datas"]["rows"][0]['wid'], src["datas"]["rows"][0]['formWid']]

def task2(wid):
  url = "https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/collector/detailCollector"

  payload = "{\"collectorWid\":\""+str(wid)+"\"}"

  headers = {
    'Host': 'ahnu.cpdaily.com',
    'Connection': 'keep-alive',
    'Content-Length': '24',
    'accept': 'application/json, text/plain, */*',
    'Origin': 'https://ahnu.cpdaily.com',
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 yiban/8.1.13 cpdaily/8.1.13 wisedu/8.1.13',
    'content-type': 'application/json',
    'Referer': 'https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html?collectorWid=40084',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': 'acw_tc=781bad3115970659948407638e7815007c1273f95121edb66eb62b38bec9b1; MOD_AUTH_CAS='+__G_MOD_AUTH_CAS+' clientType=cpdaily_student; tenantId=ahnu; sessionToken=60172bac-9191-441e-88b8-8c3220ac59b8; acw_tc=781bad2315970740662301921e332dc32ff3b5bf66b1e32d72b043d0207b48'
  }

  response = requests.request("POST", url, headers=headers, data=payload)
  print(response.text)
  src = json.loads(response.text)
  # print(src["datas"]["collector"]["schoolTaskWid"])
  return src["datas"]["collector"]["schoolTaskWid"]

def task3(formWid,collectorWid):
  url = "https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/collector/getFormFields"

  payload = "{\"pageSize\":10,\"pageNumber\":1,\"formWid\":\""+str(formWid)+"\",\"collectorWid\":\""+str(collectorWid)+"\"}"
  headers = {
    'Host': 'ahnu.cpdaily.com',
    'Connection': 'keep-alive',
    'Content-Length': '70',
    'accept': 'application/json, text/plain, */*',
    'Origin': 'https://ahnu.cpdaily.com',
    'x-requested-with': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 yiban/8.1.13 cpdaily/8.1.13 wisedu/8.1.13',
    'content-type': 'application/json',
    'Referer': 'https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/mobile/index.html?collectorWid=40084',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8',
    'Cookie': 'acw_tc=781bad3115970659948407638e7815007c1273f95121edb66eb62b38bec9b1; MOD_AUTH_CAS='+__G_MOD_AUTH_CAS+' clientType=cpdaily_student; tenantId=ahnu; sessionToken=60172bac-9191-441e-88b8-8c3220ac59b8; acw_tc=781bad2315970740662301921e332dc32ff3b5bf66b1e32d72b043d0207b48'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)

  print(response.text)
  src = json.loads(response.text)

  return [int(src["datas"]["rows"][0]['wid']), int(src["datas"]["rows"][1]['fieldItems'][2]['itemWid'])]


def task4(formWid, wid, schoolTaskWid, Fwid, FitemWid):
  url = "https://ahnu.cpdaily.com/wec-counselor-collector-apps/stu/collector/submitForm"

 # payload = "{\"formWid\":\""+str(formWid)+"\",\"address\":\"\",\"collectWid\":\""+str(wid)+"\",\"schoolTaskWid\":\""+str(schoolTaskWid)+"\",\"form\":[{\"wid\":\"10996\",\"formWid\":\"1037\",\"fieldType\":1,\"title\":\"当前，你所在的位置是？\",\"description\":\"\",\"minLength\":1,\"sort\":\"1\",\"maxLength\":300,\"isRequired\":1,\"imageCount\":-2,\"hasOtherItems\":0,\"colName\":\"field001\",\"value\":\"安徽省/蚌埠市/龙子湖区\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":[],\"area1\":\"安徽省\",\"area2\":\"蚌埠市\",\"area3\":\"龙子湖区\"},{\"wid\":\"10997\",\"formWid\":\"1037\",\"fieldType\":2,\"title\":\"当前，你所处的单位是？\",\"description\":\"\",\"minLength\":0,\"sort\":\"2\",\"maxLength\":null,\"isRequired\":1,\"imageCount\":null,\"hasOtherItems\":0,\"colName\":\"field002\",\"value\":\"在实习或工作单位\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":[{\"itemWid\":\"31159\",\"content\":\"在实习或工作单位\",\"isOtherItems\":0,\"contendExtend\":null,\"isSelected\":null}]},{\"wid\":\"10998\",\"formWid\":\"1037\",\"fieldType\":3,\"title\":\"今天，你的身体健康状况如何？（可多选）\",\"description\":\"\",\"minLength\":0,\"sort\":\"3\",\"maxLength\":null,\"isRequired\":1,\"imageCount\":null,\"hasOtherItems\":0,\"colName\":\"field003\",\"value\":\"\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":[{\"itemWid\":\"31161\",\"content\":\"健康\",\"isOtherItems\":0,\"contendExtend\":null,\"isSelected\":null}]}]}"
  payload = "{\"formWid\":\"" + str(formWid) + "\",\"address\":\"\",\"collectWid\":\"" + str(
    wid) + "\",\"schoolTaskWid\":\"" + str(
    schoolTaskWid) + "\",\"form\":[{\"" \
                     "wid\":\"" + str(Fwid) + "\",\"formWid\":\"" + str(formWid) + "\",\"fieldType\":1,\"" \
                     "title\":\"当前，你所在的位置是？\",\"description\":\"\",\"minLength\":1,\"sort\":\"1\",\"maxLength\":300,\"isRequired\":1,\"imageCount\":-2,\"hasOtherItems\":0,\"colName\":\"field001\",\"value\":\"安徽省/蚌埠市/龙子湖区\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":[],\"area1\":\"安徽省\",\"area2\":\"蚌埠市\",\"area3\":\"龙子湖区\"},{\"" \
                     "wid\":\"" + str(Fwid+1) + "\",\"formWid\":\"" + str(formWid) + "\",\"fieldType\":2,\"title\":\"当前，你所处的单位是？\",\"description\":\"\",\"minLength\":0,\"sort\":\"2\",\"maxLength\":null,\"isRequired\":1,\"imageCount\":null,\"hasOtherItems\":0,\"colName\":\"field002\",\"value\":\"在实习或工作单位\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":" \
                     "[{\"itemWid\":\"" + str(FitemWid) + "\",\"content\":\"在实习或工作单位\",\"isOtherItems\":0,\"contendExtend\":null,\"isSelected\":null}]}," \
                     "{\"wid\":\"" + str(Fwid+2) + "\",\"formWid\":\"" + str(formWid) + "\",\"fieldType\":3,\"title\":\"今天，你的身体健康状况如何？（可多选）\",\"description\":\"\",\"minLength\":0,\"sort\":\"3\",\"maxLength\":null,\"isRequired\":1,\"imageCount\":null,\"hasOtherItems\":0,\"colName\":\"field003\",\"value\":\"\",\"minValue\":0,\"maxValue\":0,\"isDecimal\":true,\"fieldItems\":[" \
                     "{\"itemWid\":\"" + str(FitemWid+2) + "\",\"content\":\"健康\",\"isOtherItems\":0,\"contendExtend\":null,\"isSelected\":null}]}]}"
  headers = {
    'tenantId': 'ahnu',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 4.4.4; HD1910 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Safari/537.36 okhttp/3.12.4',
    'CpdailyStandAlone': '0',
    'extension': '1',
    'Cpdaily-Extension': __G_Cpdaily_Extension, #'CEzs4zRiNZBrVyVJIR48j06/FSrnXSMireGIV0IQrwKwHqCTu0tLvCE/7jhk CRKnYDvSNdzZz9XaVPU/nVOpEybIWKkJFryRrytn81Tc3QTEatyX1FDx7/hf bH99t5ir4/Pn+Fhes4P+Z7gG59ybwitco6lHw0Mb4xfMPJQaNwPhyMdzBZtc XxfTgE5PunM/o5FZsxO0OwRHvj/FLPhDI8/xCVBk6tzuHaeyxUraYgsJAtHJ rClti0f82UlasAr+U2yqnlSp9Y8=',
    'Content-Type': 'application/json; charset=utf-8',
    'Content-Length': '1307',
    'Host': 'ahnu.cpdaily.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'Cookie': 'acw_tc=781bad3115970659948407638e7815007c1273f95121edb66eb62b38bec9b1; MOD_AUTH_CAS='+__G_MOD_AUTH_CAS+' clientType=cpdaily_student; tenantId=ahnu; sessionToken=60172bac-9191-441e-88b8-8c3220ac59b8'
  }

  response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))
  print(response.text)
  src = json.loads(response.text)
  print(src["message"])
  return src["message"]

def main_handler(event, context):
    curr_time = datetime.datetime.now()
    # print(type(curr_time.hour))
    data = task1()
    if(data[0] != 1):#判断是否已经提交，已经提交不用重复提交,或者没有任务
      print(data[0]) #wid
      print(data[1]) #formWid
      schoolTaskWid = task2(data[0])   #获取学校的任务Id schoolTaskWid
      print(schoolTaskWid)
      data1 = task3(data[1], data[0])#获取具体内容
      print(data1[0]) #wid
      print(data1[1]) #formWid
      #if(curr_time.hour >= 0 and curr_time.hour <=5):
      task4(data[1], data[0], schoolTaskWid, data1[0], data1[1])
    else:
      print(data)



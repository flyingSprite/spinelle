
import json
import time
import requests


cookies = dict(
    sid='R5sHHsbKiwVZbiEBdxs1qcSLIMp.aeB%2FB8I%2FM48XemUO5peZ%2Bdv0yQQgQXHOR6H1GDuBXpM',
    uid='20270811',
    crtg_rta='criteo_250x250crtnative3criteo_200x200_Pins%3Bcriteo_200x200_Search%3B',
    BDTUJIAID='f3a76c2cbec425183118cc83dce168dd',
    __asc='9762836915b1a979b753313af52',
    __auc='960c91e115a2840d3be945aed93',
    _cnzz_CV1256903590='is-logon%7Clogged-in%7C1490806035838%26urlname%7Czrkongxiao%7C1490806035838',
    UM_distinctid='15b08b4a15d19c-0a03b273a3b34f-396f7b07-fa000-15b08b4a15e1c7',
    CNZZDATA1256914954='1430102040-1488538496-null%7C1490511462',
    referer='https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DVwBo36Acy216AwqQx7Phh_ivBYl5oqI5FqZu29vUd-vDD9E_SrgGaVxDmx9ZvR3k%26wd%3D%26eqid%3D905a2e300007731b0000000358dbc925'
)

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36'}


def get_response(last_pin_id, cookies):
    time.sleep(0.3)
    request_url = 'http://huaban.com/from/drawcrowd.com/?j0v6z8wg&max=%s&limit=20&wfl=1' % (str(last_pin_id))
    print request_url
    print cookies
    response = requests.get(request_url, headers=headers, cookies=cookies)
    result = response.text
    print result
    anasisly_json(json.loads(result))


def anasisly_json(result):
    response_list = result.get('pins')
    for item in response_list:
        if item and item['file'] and item['file']['key']:
            # print item['file']['key']
            pass
    print result
    last_item = response_list[len(response_list) - 1]
    last_pin_id = last_item['pin_id']
    get_response(last_pin_id, cookies)


get_response(1079920040, cookies=cookies)

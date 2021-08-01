import sys
from time import sleep

import requests

from lxml import etree

requests.packages.urllib3.disable_warnings()


# 获取所有手机地址
def get_phone_url(page):
    url = "https://detail.zol.com.cn/cell_phone_index/subcate57_0_list_1_0_1_2_0_{}.html"
    data = requests.get(url.format(str(page))).text
    html = etree.HTML(data)
    html_data = html.xpath('// *[ @ id = "J_PicMode"] / li / a / @ href')
    return html_data


# 获取手机大概信息
def get_info_url(info_url):
    url = "https://detail.zol.com.cn/"
    sleep(0.5)
    phone_info = requests.get(url + info_url).text
    html = etree.HTML(phone_info)
    html_data = html.xpath('//*[@id="secondsUnderstand"]/div[2]/div/div/a/@href')

    return html_data


def get_info():
    pass


# 获取每个页面所有的手机信息的url地址
def get_every_phone_info_url(page):
    for i in get_phone_url(page):
        yield get_info_url(i)


def get_jd_info(jd_url):
    phone_info = {}
    header = {
        'connection': 'keep-alive',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"chromium";v="92", " noT A;brand";v="99", "googlE chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'DNT': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'mozilla/5.0 (windowS NT 10.0; win64; x64) appLewEbkit/537.36 (KHTML, likE gecko) chrome/92.0.4515.107 safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zH-Cn,zh;q=0.9,eN-Us;q=0.8,en;q=0.7,zH-Tw;q=0.6',
        'cookie': 'mba_muid=1626537007610278271360; shshshfpb=w9m45R%201Cd4PzZngboT5UfQ%3D%3D; shshshfpa=cde3884b-dc70-9c78-5042-771016cefe1a-1617448719; trackERID=hruA3DC7tOnlDBVWpIk7KiK61sUg-7BSPZeztPyiWrCZnNaZ56mkG5ufeM0CTKxFqa6nasw_1cMLEWaBoA56qE_JfQFygHcVP7jtpnu8yWXRmNhOEADjeADKT99iRgmelsu6dwqArKDbHil9HCpNnQ; pt_keY=AaJg8VXIADA2yWAAfCFQr_gRSEjmlSwgNyqel1SLDS1OP7FlB77dTQdfCdLMkpsAbV7vxrEaUaA; pt_pin=jd_77f17207d4baa; pt_token=r9kgawtq; pwdt_id=jd_77f17207d4baa; retina=1; cid=9; webp=1; __wga=1626537042315.1626537042315.1626537042315.1626537042315.1.1; sc_width=400; visitkey=8321007253072248; shshshfp=8ce328dd390d87260a02c2cdff95ce0e; __jdc=122270672; __jda=122270672.1626537007610278271360.1626537007.1626537007.1627794562.2; __jdu=1626537007610278271360; arEaId=19; Iploc-djd=19-1601-50258-51885; wlfstk_smdl=yda9ey9pj93wby71qsyzbfem7r1cpb7o; CCC_SE=ADc_jbZGGoWQ1D8FKZo7Yalzp%2FPRB3Mebplzj2aP6ytrPnlIzdrCoG8yWj05i9xKu%2bYLQJ2CLMe6MEMApNu4bFbL8EQ0U1pdGTPKOqyOcMHAN6GPJr4ulcLBMx8ceo7TXC8mbq%2bIAdGEjCg7WpOf%2fcdnDkriiPEEZCyQM6BiTPKN%2BmhIQbIXZgkxFHEb8hO%2fA6EoopmQQIs1GfuUpHoCMAnfJOROuvYSmwqYvNvCP2KoFZSyMn7%2BHpivCwfvjD1yPLCDz5mSZaknAuqLaF3JN3h9MpHH3rwwIUEVAuEFDzSi5Y9EM3MoPjqUiuThYBDoSJGUbzKNTe2SnRXTF%2BZePMdiqDjTf%2BcNzjrq034BHJoCdLTcPD2Et4vCZzKvJeJK6I3ENU%2fn46BINLmHo3CMmZXHGoGIDAX216PRNV%2BguLAzrhes%2bv%2BQcwTzLTTRJECSKqUmKaLy07zGmR10B6Sp7Hjzrkzno6l8N5QBxxZdfgr2Z2svm1%2fdUux4J6LwYz9jsFvrMHZdLwG%2biWYxzXYAZYvPfA%3d%3d; unpL=V2_ZznTBRYdRhR9DKbvcKOIUGIDQFVLBBevdG9BvxGbWgYyVHvvCLRcFNUUR11NgFWuZWEZXuJCqBXFcedKEbBCNWQceLTdXkmCdALGzeSAXdVuMxJAQVBHF3MJR1J8GV0GyQORW0JVRBRFOefkexHDbGCLFFVCX0QUrTHDVH0ZXdVmMxNTAaMFHXEKQ1V4vFWCZAQWX0RwQhNYcEdXFrBfa2CBfvXyVNMW; shshsHSID=72fbf9aafcdb50a5342011cd9900110e_3_1627794782370; __jdb=122270672.4.1626537007610278271360|2.1627794562; __jdv=122270672|norefer|t_281_20170818001|cpc|_0_ee4097708bed41c98bc126602372dd69|1627794782382; 3AB9D23F7A4B3C9B=WLLN56654XFVQXQNOOF5FPWECULFF2HWFGB7PQJXH26WRRD7R3UX7QG7V5MGBDT64BKUXZYIJ34JBHE2UIQZYALAY4',
        'if-modified-since': 'sun, 01 aug 2021 05:16:40 GMT',
    }
    a = requests.get(
        jd_url,
        headers=header, verify=False).text
    html = etree.HTML(a)

    def get_info(xpath):
        return html.xpath(xpath)

    a = get_info("//dl[@class='clearfix']/dt/text()|//dl[@class='clearfix']/dd[last()]/text()")
    # print(dict(zip(a[::2],a[1::2])))
    return dict(zip(a[::2],a[1::2]))


def get_all_info(url):
    domain = "https://detail.zol.com.cn"
    phone_info = {}

    all_info = requests.get(domain + url).text.replace("，", "")
    html = etree.HTML(all_info)

    def get_info(xpath):
        return html.xpath(xpath)

    key = get_info("//table/tr/th/span/text()")
    value = get_info("//table/tr/td/span[1]/text()|//table/tr/td/span[1]/a[1]/text()")
    phone_info.update(dict(zip(key, value)))
    model_jd_url = get_info('//*[@id="param-list-b2c-jd"]/@href')
    if model_jd_url:
        index = model_jd_url[0].find("to=")
        jd_url = model_jd_url[0][index + 3:]
        jd_phone_info = get_jd_info(jd_url)

    phone_info.update(jd_phone_info)
    # phone_info["product_model__name"] = product_model__name
    # phone_info["model_chicun"] = model_chicun
    # phone_info["model_fenbianlv"] = model_fenbianlv
    # phone_info["model_jiage"] = model_jiage
    # phone_info["model_sys"] = model_sys
    # phone_info["jd_url"] = jd_url
    print(domain + url, "\n", phone_info)
    return phone_info


def main():
    page = 1
    while True:

        phone_info_url = get_every_phone_info_url(str(page))

        while phone_info_url:
            try:
                a = next(phone_info_url)
                if a:
                    get_all_info(a[0])
                else:
                    continue


            except StopIteration:
                sys.exit()

        page += 1


if __name__ == '__main__':
    main()
    # get_jd_info("https://item.jd.com/100019141940.html")

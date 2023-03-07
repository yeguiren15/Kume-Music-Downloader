# 1.找我们数据所在的地址
print('欢迎使用酷我音乐破解工具，请新建一个名为酷我音乐的文件夹')
import requests
singer = input('请输入你想下载的歌手或专辑:')
num = input('请输入你想下载第几页:')
num_1 = input('请输入你想下载的页数:')
number = input('请输入你想下载的歌曲数量:')

url = 'https://kuwo.cn/api/www/search/searchMusicBykeyWord?'
# 2.伪装
head = {
    'Cookie': '_ga=GA1.2.258740410.1664949340; _gid=GA1.2.754700688.1670064990; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1668856108,1668859774,1670064990,1670067320; _gat=1; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1670067537; kw_token=D4ANIYLWVQU',
    'csrf': 'D4ANIYLWVQU',
    'Host': 'kuwo.cn',
    'Referer': 'https://kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}  # 定义一个名叫head的字典
par = {
    'key': singer,
    'pn': num,
    'rn': number,
    'httpsStatus': num_1,
    'reqId': '735ecba1-7300-11ed-882b-092df05a5418',
}  # 定义一个名叫par的字典

proxies={
'http':'120.197.179.166',
'https':'120.197.179.166'
}

# 3.发送请求 得到响应的数据
res = requests.get(url=url, headers=head, params=par,proxies=proxies).json()
# print(res)
# 解析数据  分两次提取 第一次先提取列表  第二次再提取列表里面具体的数据
lis = res['data']['list']
for li in lis:
    name = li['name']
    rid = li['rid']
    api_url = f'https://antiserver.kuwo.cn/anti.s?type=convert_url&rid={rid}&format=mp3&response=url'
    music_url = requests.get(url=api_url).text  # 获取音乐播放的地址
    con = requests.get(url=music_url).content  # 获取音乐的二进制数据
    # 5.保存数据
    with open('酷我音乐\\' + name + '.mp3', 'wb') as f:
        f.write(con)
        print('下载成功', name)
print('声明：本程序仅用于学习和参考，禁止商用，违者后果自负！！！')
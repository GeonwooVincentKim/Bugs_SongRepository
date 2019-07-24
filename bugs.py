from bs4 import BeautifulSoup
import requests


# strip() : 문자열 앞 / 뒤의 불필요한 빈 칸을 제거합니다.
# lstrip() : 문자열 앞의 불필요한 빈 칸을 제거합니다.
# rstrip() : 문자열 뒤의 불필요한 빈 칸을 제거합니다.
# split() : 인수로 지정된 구분자를 이용해서 문자열을 분리합니다. split() 함수의 인수가 생략되면
# 공백을 의미하고 함수 실행 결과는 List 로 출력합니다.

# File
# File 열기
# File 변수 = open('Text File 명', '열기 모드')
# 열기 모드 : r(읽기 전용), w(쓰기 전용), a(쓰기, 추가)
# 열기 모드가 r인 File 은 Disk 에 반드시 File 이 존재해야 하고, 열기 모드가 w, a 인 File 은 Disk 에
# 파일이 존재하지 않을 경우 File 을 새로 만듭니다.
# w 는 File 이 Disk 에 있으면 저장되는 Data 로 덮어쓰기를 하고 a 는 File 이 Disk 에 있으면 기존
# File 의 맨 뒤에 Data 를 추가합니다.
# File 작업을 완료 할 경우 반드시 File 은 닫아줘야 합니다.

def bugs_song_chart():
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")
    chart = bsObj.findAll("p", {"class": "title"})
    artists = bsObj.findAll("p", {"class": "artist"})

    for i in range(len(chart)):
        # # print(artists[i].text)
        artist = artists[i].text.strip().split("\n")[0]
        titles = chart[i].text.strip()
        print("{0:3d}위 {1} - {2}".format(i + 1, artist, titles))
    #     for getchart in chart:
    #         song_chart.append(titles.text)
    #         artist_chart.append(artist.text)
    # #     rank = getchart.findAll("a")
    # #     for getrank in rank:
    # #         song_chart.append(getrank.text)

    # return song_chart, artist_chart

    file = open('bugsTop100.txt', 'w', -1, 'UTF-8')
    for i in range(len(chart)):
        # artist 는 밑에 두 줄에 공백이 나오기 때문에
        # 0번 배열로 적어 놓았습니다.
        artist = artists[i].text.strip().split('\n')[0]
        titles = chart[i].text.strip()
        data = '{0:3d}위 {1} - {2}'.format(i+i, artist, titles)
        file.write(data + '\n')

    print("파일 쓰기 완료")
    file.close()


if __name__ == "__main__":
    bugs_song_chart()
#     song_chart = bugs_song_chart()
#     artist_chart = bugs_song_chart()
#     # for i in range(len(song_chart)):
#     #    print("{0:3d}위 {1} - {2}".format(i+1, artist_chart[i], song_chart[i]))

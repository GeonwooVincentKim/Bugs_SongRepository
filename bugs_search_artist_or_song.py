from bs4 import BeautifulSoup
import requests


def bugs_artist():
    result = []

    artists = input("Please Input the artist name or song that you want to get information")
    request = requests.get("https://music.bugs.co.kr/chart")
    html = request.text
    bsObj = BeautifulSoup(html, "html.parser")

    artist_chart = bsObj.findAll("p", {"class": "artist"})
    song_chart = bsObj.findAll("p", {"class": "title"})

    print("입력하신 " + artists + "에 대한 검색 결과입니다.")
    for i in range(len(artist_chart)):
        artist = artist_chart[i].text.strip()
        song = song_chart[i].text.strip()

        if artists in artist or artists in song:
            result += ["{0:3d}위 {1} - {2}".format(i + 1, artist, song)]

    if len(result) > 0:
        for user_serach in result:
            print(user_serach)

    else:
        print("앗! " + artists + "에 데이터가 없어요!! 다시 검색해주세요")

    f = open("artist_list.txt", "w", -1, "UTF-8")
    for user_search_csv in result:
        f.write(user_search_csv + "\n")

    if len(result) > 0:
        print("파일이 정상적으로 완성되었습니다.")
        f.close()

    else:
        print(artists+"에 제대로 된 데이터가 없어서 저장을 못했어요ㅠㅠ")


if __name__ == "__main__":
    bugs_artist()


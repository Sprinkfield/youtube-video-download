from cgitb import html
import youtube_dl
from gethtml import HtmlPageManip


chars = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"


class VideoDownload:
    def __init__(self):
        pass

    def get_videos_ids(self, WEBSITE_LINK, id_list=list()):
        page_text=HtmlPageManip().get_html_of_page(WEBSITE_LINK)
        for _ in page_text:
            id = page_text.find("videoId")
            if id != -1:
                video_id = page_text[id+8:id+23]
                page_text = page_text[id+50:]
                string = ""
                for c in video_id:
                    if c in chars:
                        string += c
                id_list.append(string)
        return id_list

    def dowload_video(self, link):
        try:
            with youtube_dl.YoutubeDL() as ydl:
                ydl.download([link])
        except:
            print("Error! Can not download this video.")


def main():
    if input("Would you download some videos from 1 channel or just 1 video? (c/v): ") == "c":
        WEBSITE_LINK = input("Input channel's link: ")
        counter = 0
        list_of_video_llinks = VideoDownload().get_videos_ids(WEBSITE_LINK)
        videos_links = list()

        for v_link in list_of_video_llinks:
            if v_link not in videos_links:
                videos_links.append(v_link)

        print(videos_links)
        print(len(videos_links))

        for v_link in videos_links:
            print(counter)
            counter += 1
            VideoDownload().dowload_video(v_link)
    else:
        vid_link = input("Input the link to the video: ")
        VideoDownload().dowload_video(vid_link)


if __name__ == "__main__":
    main()

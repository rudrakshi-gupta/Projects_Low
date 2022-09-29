from tkinter import *
from PIL import Image,ImageTk
from bs4 import BeautifulSoup
from tkHyperlinkManager import HyperlinkManager
from Data_set_analysis import *
from functools import partial
import requests
from csv import writer
import webbrowser
import os

url = "https://timesofindia.indiatimes.com/"
news_dataset = []

class web_scrapper:
    def __init__(self,window):
        self.window = window
        self.window.title("Web Scrapper - Times of India!")
        self.window.geometry('1200x675+0+0')

        # function that searches google
        def search(*arg):
            headers = {'User-agent': 'Chrome/103.0.5060.134'}

            request = requests.get('https://timesofindia.indiatimes.com/', headers=headers)
            html = request.content

            soup = BeautifulSoup(html, 'html.parser')

            if(not arg):
                x = e.get()
            else:
                x = str(arg)[2:-3]
                print(x)

            def toi_news_scrapper(keyword):
                news_list = []
                with open('news_scraping.csv', 'w', encoding='utf8', newline='') as f:
                    thewriter = writer(f)
                    header = ['Index', 'Head Lines']
                    thewriter.writerow(header)
                    v = soup.find_all('figure')
                    for h in v:
                        news_title = h.a.figcaption.get_text()
                        news_link = h.a.get('href')

                        if news_title not in news_list:
                                if 'Times of India' not in news_title:
                                    k = [news_title,news_link]
                                    news_list.append(k)

                    no_of_news = 0
                    keyword_list = []
                    # Goes through the list and searches for the keyword
                    for i in range(1,len(news_list)):
                        text = ''
                        
                        if ((keyword in news_list[i][0]) or (keyword in news_list[i][1])):
                            text = ' <---------- KEYWORD FOUND!'
                            no_of_news += 1
                            keyword_list.append(news_list[i])
                    # Prints the Titles of the articles that contain the keywords
                    for j in range(len(keyword_list)):
                        info = [keyword_list[j][0],keyword_list[j][1], text]
                        thewriter.writerow(info)
                    
                    # tkinter display
                    section = Toplevel()
                    section.title(f"Searched keyword - {keyword}")
                    section.geometry('1200x675+0+0')

                    img=Image.open('images/keyword.jpg')
                    img=img.resize((1200,675),Image.Resampling.LANCZOS)
                    self.photobg=ImageTk.PhotoImage(img)
                    t = Label(section, image=self.photobg)
                    t.place(x=0,y=0)

                    w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text =f'News on {keyword} -- {no_of_news} Articles :\n' ,font=('calibri',20))
                    w_frame.place(x=120,y=80,width=900,height=600)
                    text_b = Text(w_frame,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
                    text_b.pack()
                    hyperlink = HyperlinkManager(text_b)
                    for p in range(0,len(keyword_list)):
                        text_b.insert(INSERT, keyword_list[p][0])
                        text_b.insert(INSERT,"\n")
                        text_b.insert(INSERT,"Click to read the article..", hyperlink.add(partial(webbrowser.open,keyword_list[p][1])))
                        text_b.insert(INSERT,"\n")
                        text_b.insert(INSERT,"\n")

                    
                with open('Searched_news.csv', 'a',encoding='utf8', newline='') as f:
                    thewriter = writer(f)
                    header1 = ['Keyword', 'Number of articles found']
                    file_is_empty = os.stat('Searched_news.csv').st_size==0
                    if file_is_empty:
                        thewriter.writerow(header1)
                    o = [keyword,no_of_news]
                    news_dataset.clear()
                    news_dataset.append(o)
                    thewriter.writerows(news_dataset)
            if(x != "Search here.."):
                toi_news_scrapper(x)


        Boardframe = LabelFrame(self.window,bd=20,bg="black",relief=FLAT,font=('calibri',12))
        Boardframe.place(x=120,y=80,width=900,height=200)

        # searchbar
        e=Entry(Boardframe,width=76,relief=FLAT,borderwidth=8, font=1)
        e.insert(0,"Search here..")
        e.grid(row=0,column=1)

        # popular searches
        def popular_searches(name):
            if(name == 'b'):
                section = Toplevel()
                section.title('Business section')
                section.geometry('1200x675+0+0')

                img=Image.open('images/business.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                b = Label(section, image=self.photobg)
                b.place(x=0,y=0)

                urlb = "https://timesofindia.indiatimes.com/business"
                content_requestb = requests.get(urlb)
                html_contentb = content_requestb.content
                soup_b = BeautifulSoup(html_contentb, 'html.parser')

                w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text ="Bussiness news --------\n" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                text_b = Text(w_frame,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
                text_b.pack()

                all_b = list()
                hyperlink = HyperlinkManager(text_b)
                figure_b = soup_b.find_all('figure')
                for ha in (figure_b):
                    all_b.append(ha.figcaption.get_text())
                    all_b.append(ha.a.get('href'))
                for p in range(0,len(all_b),2):
                    text_b.insert(INSERT, all_b[p])
                    text_b.insert(INSERT,"\n")
                    text_b.insert(INSERT,"Click to read the article..", hyperlink.add(partial(webbrowser.open,all_b[p+1])))
                    text_b.insert(INSERT,"\n")
                    text_b.insert(INSERT,"\n")

            if(name == 't'):
                section = Toplevel()
                section.title('Technology section')
                section.geometry('1200x675+0+0')

                img=Image.open('images/tech.jpg')
                img=img.resize((1200,675),Image.Resampling.LANCZOS)
                self.photobg=ImageTk.PhotoImage(img)
                t = Label(section, image=self.photobg)
                t.place(x=0,y=0)

                urlt = "https://www.gadgetsnow.com/"
                content_requestt = requests.get(urlt)
                html_contentt = content_requestt.content
                soup_t = BeautifulSoup(html_contentt, 'html.parser')

                w_frame = LabelFrame(section,bd=20,bg="white",relief=FLAT,text ="Tech and Gadgets news --------\n" ,font=('calibri',20))
                w_frame.place(x=120,y=80,width=900,height=600)

                text_t = Text(w_frame,width=800, height=595, font=('calibri',14),blockcursor=True,relief=FLAT)
                text_t.pack()

                all_t = list()
                hyperlink = HyperlinkManager(text_t)
                figure_t = soup_t.find_all('a',class_="")
                for ha in (figure_t):
                    if(ha.figcaption != None):
                      all_t.append(ha.figcaption.get_text())
                      all_t.append(ha.get('href'))
                for p in range(0,len(all_t),2):
                    text_t.insert(INSERT, all_t[p])
                    text_t.insert(INSERT,"\n")
                    text_t.insert(INSERT,"Click to read the article..", hyperlink.add(partial(webbrowser.open,all_t[p+1])))
                    text_t.insert(INSERT,"\n")
                    text_t.insert(INSERT,"\n")
                
            if(name == 's'):
                section = Toplevel()
                section.title('Sports section')
                section.geometry('1200x675+0+0')

                img = Image.open('images/sports.jpg')
                img = img.resize((1200, 675), Image.Resampling.LANCZOS)
                self.photobg = ImageTk.PhotoImage(img)
                s = Label(section, image=self.photobg)
                s.place(x=0, y=0)

                urls = "https://timesofindia.indiatimes.com/sports"
                content_requests = requests.get(urls)
                html_contents = content_requests.content
                soup_s = BeautifulSoup(html_contents, 'html.parser')

                w_frame = LabelFrame(section, bd=20, bg="white", relief=FLAT, text="Sports news --------\n",
                font=('calibri', 20))
                w_frame.place(x=120, y=80, width=900, height=600)

                text_s = Text(w_frame, width=800, height=595, font=('calibri', 14), blockcursor=True, relief=FLAT)
                text_s.pack()

                all_s = list()
                hyperlink = HyperlinkManager(text_s)
                figure_s = soup_s.find_all('span',class_="w_tle")
                for ha in (figure_s):
                    all_s.append(ha.a.get_text())
                    all_s.append(ha.a.get('href'))
                for p in range(0, len(all_s), 2):
                    text_s.insert(INSERT, all_s[p])
                    text_s.insert(INSERT, "\n")
                    text_s.insert(INSERT, "Click to read the article..",
                    hyperlink.add(partial(webbrowser.open, all_s[p + 1])))
                    text_s.insert(INSERT, "\n")
                    text_s.insert(INSERT, "\n")


            if(name == 'n'):
                section = Toplevel()
                section.title('News section')
                section.geometry('1200x675+0+0')

                img = Image.open('images/news.jpg')
                img = img.resize((1200, 675), Image.Resampling.LANCZOS)
                self.photobg = ImageTk.PhotoImage(img)
                n = Label(section, image=self.photobg)
                n.place(x=0, y=0)

                url_n = "https://timesofindia.indiatimes.com/home/headlines"
                content_request_n = requests.get(url_n)
                html_content_n = content_request_n.content
                soup_n = BeautifulSoup(html_content_n, 'html.parser')

                w_frame = LabelFrame(section, bd=20, bg="white", relief=FLAT, text="Explainers News --------\n",
                font=('calibri', 20))
                w_frame.place(x=120, y=80, width=900, height=600)

                text_n = Text(w_frame, width=800, height=595, font=('calibri', 14), blockcursor=True, relief=FLAT)
                text_n.pack()

                all_n = list()
                hyperlink = HyperlinkManager(text_n)
                figure_n = soup_n.find_all('span',class_="w_tle")
                for ha in (figure_n):
                    all_n.append(ha.a.get_text())
                    all_n.append(ha.a.get('href'))
                for p in range(0, len(all_n), 2):
                    text_n.insert(INSERT, all_n[p])
                    text_n.insert(INSERT, "\n")
                    text_n.insert(INSERT, "Click to read the article..",
                    hyperlink.add(partial(webbrowser.open, all_n[p + 1])))
                    text_n.insert(INSERT, "\n")
                    text_n.insert(INSERT, "\n")

            if(name == 'et'):
                section = Toplevel()
                section.title('Entertainment section')
                section.geometry('1200x675+0+0')

                img = Image.open('images/entertainment.jpg')
                img = img.resize((1200, 675), Image.Resampling.LANCZOS)
                self.photobg = ImageTk.PhotoImage(img)
                s = Label(section, image=self.photobg)
                s.place(x=0, y=0)

                url_et = "https://timesofindia.indiatimes.com/entertainment"
                content_request_et = requests.get(url_et)
                html_content_et = content_request_et.content
                soup_et = BeautifulSoup(html_content_et, 'html.parser')

                w_frame = LabelFrame(section, bd=20, bg="white", relief=FLAT, text="Entertainment news --------\n",
                font=('calibri', 20))
                w_frame.place(x=120, y=80, width=900, height=600)

                text_et = Text(w_frame, width=800, height=595, font=('calibri', 14), blockcursor=True, relief=FLAT)
                text_et.pack()

                all_et = list()
                hyperlink = HyperlinkManager(text_et)
                figure_et = soup_et.find_all('li',class_="small_video_lft clearfix")
                for ha in (figure_et):
                    all_et.append(ha.a.get_text())
                    all_et.append(ha.a.get('href'))
                for p in range(0, len(all_et), 2):
                    text_et.insert(INSERT, all_et[p])
                    text_et.insert(INSERT, "\n")
                    text_et.insert(INSERT, "Click to read the article..",
                    hyperlink.add(partial(webbrowser.open, all_et[p + 1])))
                    text_et.insert(INSERT, "\n")
                    text_et.insert(INSERT, "\n")
            if (name == 'e'):
                section = Toplevel()
                section.title('Education section')
                section.geometry('1200x675+0+0')

                img = Image.open('images/education.jpg')
                img = img.resize((1200, 675), Image.Resampling.LANCZOS)
                self.photobg = ImageTk.PhotoImage(img)
                e = Label(section, image=self.photobg)
                e.place(x=0, y=0)

                url_e = "https://timesofindia.indiatimes.com/education/exams"
                content_request_e = requests.get(url_e)
                html_content_e = content_request_e.content
                soup_e = BeautifulSoup(html_content_e, 'html.parser')

                w_frame = LabelFrame(section, bd=20, bg="white", relief=FLAT, text="Education news --------\n",
                                     font=('calibri', 20))
                w_frame.place(x=120, y=80, width=900, height=600)

                text_e = Text(w_frame, width=800, height=595, font=('calibri', 14), blockcursor=True, relief=FLAT)
                text_e.pack()

                all_e = list()
                hyperlink = HyperlinkManager(text_e)
                figure_e = soup_e.find_all('figure')
                for ha in (figure_e):
                    if (ha.figcaption != None):
                        all_e.append(ha.figcaption.get_text())
                        all_e.append(ha.a.get('href'))
                for p in range(0, len(all_e), 2):
                    text_e.insert(INSERT, all_e[p])
                    text_e.insert(INSERT, "\n")
                    text_e.insert(INSERT, "Click to read the article..",
                                  hyperlink.add(partial(webbrowser.open, all_e[p + 1])))
                    text_e.insert(INSERT, "\n")
                    text_e.insert(INSERT, "\n")

        p1 = Button(Boardframe, text = 'Business',bg='papaya whip',cursor='hand2' ,relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda : popular_searches('b')).place(x=40, y= 50)
        p2 = Button(Boardframe, text = 'Technology', bg='peach puff',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda: popular_searches('t')).place(x=170, y= 50)
        p3 = Button(Boardframe, text = 'Sports', bg='lavender',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda : popular_searches('s')).place(x=300, y= 50)
        p4 = Button(Boardframe, text = 'News', bg='lavender',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda : popular_searches('n')).place(x=430, y= 50)
        p5 = Button(Boardframe, text = 'Entertainment', bg='cadet blue',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda:popular_searches('et')).place(x=560, y= 50)
        p6 = Button(Boardframe, text = 'Education', bg='#116562',cursor='hand2',relief=FLAT, foreground='black', width=15, height=2,activebackground='orange', command=lambda:popular_searches('e')).place(x=690, y= 50)

        # submit button
        btn = Button(Boardframe, text = "Search", width=17, height=3 , foreground="black",relief=RAISED,cursor='hand2',background="yellow",command=search).place(x=372, y= 120)

        # recent search
        def recent_searches():
            rs = Toplevel()
            rs.title('Recent searches..')
            rs.config(bg='DarkOliveGreen4')
            rs.geometry('340x470')
            b = Label(rs, text = "Your recent searches :", font= 1).grid(row=0,column=0)
            l=Listbox(rs,font=('Calibri',14),width=32,height=15,selectmode=SINGLE)
            l.grid(row=5,column=0,columnspan=4)
            li = analyse.recentanalysis('Searched_news.csv')
            for j in range(len(li)):
                l.insert(j,li[j])
            
            s=Button(rs, text = 'Search',width=17, height=3 , foreground="black",relief=RAISED,background="gold",command=lambda : search(l.get(l.curselection()))).place(x=70,y=400)
        
        rsbtn = Button(window, text = "Recent Searches",cursor='hand2', width=17, height=3 , foreground="black",relief=RAISED,background="SlateGray4", font = 1,command=lambda : recent_searches()).place(x=480, y= 300)
        
        # Top 10 searches
        def topten_searches():
            t10 = Toplevel()
            t10.title('Top 10 searches on our website searches..')
            t10.config(bg='DarkOliveGreen4')
            t10.geometry('340x470')
            b = Label(t10, text = "Top 10 searches :", font= 1).grid(row=0,column=0)
            l=Listbox(t10,font=('Calibri',14),width=32,height=15,selectmode=SINGLE)
            l.grid(row=5,column=0,columnspan=4)
            li = analyse.toptenanalysis('Searched_news.csv')
            for j in range(len(li)):
                l.insert(j,li[j])
            
            s=Button(t10, text = 'Search',width=17, height=3 , foreground="black",relief=RAISED,background="gold",command=lambda : search(l.get(l.curselection()))).place(x=70,y=400)
        
        t10btn = Button(window, text = "Top 10 searches on our website",cursor='hand2', width=35, height=2 , foreground="black",relief=RAISED,background="plum3", font = 1,command=lambda : topten_searches()).place(x=390, y= 450)


window = Tk()

img=Image.open('images/web-cr.jpg')
img=img.resize((1200,675),Image.Resampling.LANCZOS)
photobg=ImageTk.PhotoImage(img)
img_l=Label(window,image=photobg).place(x=0,y=0)

player = web_scrapper(window)
window.mainloop()
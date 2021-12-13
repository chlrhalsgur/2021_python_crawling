from tkinter import *
import tkinter.ttk  # Treeview 메서드(table 관련)
from functools import partial
import crawling
import webbrowser

GEOMETRY = "1000x600"
COLOR_BG = '#5e7e9b' #5e7e9b 아쿠아마린
COLOR_BT = 'white'
WIDTH = 70
HEIGHT = 30
WARPLENGTH = 400

# 정렬 함수
def treeview_sort_column(tv, col, reverse, idx):
    l = [(tv.item(k)["values"], k) for k in tv.get_children()] 
    l.sort(key=lambda t: str(t[:][0][idx]), reverse=reverse)
    for index, (val, k) in enumerate(l):
        tv.move(k, '', index)
    tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse,idx))

win = Tk()

def create_window(movie_list, movie_list_r):
    window = Toplevel(win) #새로운 창 열기
    window.geometry(GEOMETRY)
    window.configure(bg=COLOR_BG)
    btn = Button(window, text = "Show Movie", command = partial(Naver_movie, movie_list))
    btn.configure(background=COLOR_BT)
    btn1 = Button(window, text = "Show Movie Ranking", command= partial(Naver_movie_Ranking, movie_list))
    btn1.configure(background=COLOR_BT)
    btn2 = Button(window, text = "Our New Movie Ranking", command= partial(Our_new_Ranking, movie_list_r))
    btn2.configure(background=COLOR_BT)

    
    button = Button(window,text = "<<back", command = window.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"), background=COLOR_BT)
    button.place(relx=0.8, rely=0.9)

    btn.pack(pady=40)
    btn1.pack(pady=20)
    btn2.pack(pady=20)

#Show Movie 클릭했을 경우 네이버 영화 사이트에 들어가서 상영영화 보여주기
def Naver_movie(movie_list):
    url="https://movie.naver.com/"
    webbrowser.open(url)
    

#Show Movie Ranking 클릭했을 경우 네이버 영화 랭킹 보여주기
def Naver_movie_Ranking(movie_list):
    # GUI창을 생성하고 라벨을 설정한다.
    root=tkinter.Tk()
    root.configure(bg=COLOR_BG)
    root.title("Naver Movie Ranking")
    root.geometry(GEOMETRY)
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="Naver Movie Ranking") # 제목
    lbl.pack() 
    button = Button(root,text = "<<back", command = root.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"),background=COLOR_BT)
    button.place(relx=0.8, rely=0.9)

    frame = Frame(root)
    frame.pack(pady=20)
    # 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
    treeview=tkinter.ttk.Treeview(frame, columns=["one", "two","three", "four"], displaycolumns=["one","two","three", "four"], height = 8)
    treeview.pack(side=LEFT)


    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=100)
    treeview.heading("#0", text="Index",command = lambda : treeview_sort_column(treeview, "#0", False,0))

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="Title", anchor="center", command = lambda : treeview_sort_column(treeview, "#1", False,0))

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Rate", anchor="center", command = lambda : treeview_sort_column(treeview, "#2", False,1))

    treeview.column("#3", width=70, anchor="center")
    treeview.heading("three", text="Genre_code", anchor="center", command = lambda : treeview_sort_column(treeview, "#3", False,2))

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("four", text="Detail", anchor="center", command = lambda : treeview_sort_column(treeview, "#4", False,0))

    # 스크롤바 
    sb = Scrollbar(frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    treeview.config(yscrollcommand=sb.set)
    sb.config(command=treeview.yview)


    # 표에 데이터 삽입
    for i in range(len(movie_list)):
        treeview.insert('', 'end', text=i, values=movie_list[i], iid=str(i)+"번")

    label = tkinter.Label(root, text="Select Movie", width = WIDTH, height = HEIGHT, wraplength = WARPLENGTH, bg = COLOR_BT) 
    label.pack()
    
    # 라벨 내용 바꾸기 (클릭시 이벤트)
    def click_item(event):
        selectedItem = treeview.focus() 
        getValue = treeview.item(selectedItem).get('values')[3] # 딕셔너리의 값만 가져오기
        detail = crawling.show_details(getValue)

        label.configure(text=detail) 

    treeview.bind('<ButtonRelease-1>', click_item) 

    # GUI 실행
    root.mainloop()

#Our New Movie Ranking 클릭했을 경우 새로운 랭킹 보여주기
def Our_new_Ranking(movie_list_r):
    # GUI창을 생성하고 라벨을 설정한다.
    root=tkinter.Tk()
    root.configure(bg=COLOR_BG)
    root.title("Our New Movie Ranking")
    root.geometry(GEOMETRY)
    root.resizable(False, False)

    lbl = tkinter.Label(root, text="Our new Movie Ranking") # 제목
    lbl.pack() 
    button = Button(root,text = "<<back", command = root.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"), background=COLOR_BT)
    button.place(relx=0.8, rely=0.9)


    frame = Frame(root)
    frame.pack(pady=20)

    # 표 생성하기. colums는 컬럼 이름, displaycolums는 실행될 때 보여지는 순서다.
    treeview=tkinter.ttk.Treeview(frame, columns=["one", "two","three", "four"], displaycolumns=["one","two","three","four"], height = 8)
    treeview.pack(side=LEFT)

    # 각 컬럼 설정. 컬럼 이름, 컬럼 넓이, 정렬 등
    treeview.column("#0", width=100)
    treeview.heading("#0", text="Index",command = lambda : treeview_sort_column(treeview, "#0", False,0))

    treeview.column("#1", width=100, anchor="center")
    treeview.heading("one", text="Title", anchor="center", command = lambda : treeview_sort_column(treeview, "#0", False,0))

    treeview.column("#2", width=100, anchor="center")
    treeview.heading("two", text="Rate", anchor="center", command = lambda : treeview_sort_column(treeview, "#2", False,1))

    treeview.column("#3", width=70, anchor="center")
    treeview.heading("three", text="Genre_code", anchor="center", command = lambda : treeview_sort_column(treeview, "#3", False,2))

    treeview.column("#4", width=100, anchor="center")
    treeview.heading("four", text="Detail", anchor="center", command = lambda : treeview_sort_column(treeview, "#4", False,3))


    # 스크롤바 
    sb = Scrollbar(frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)
    treeview.config(yscrollcommand=sb.set)
    sb.config(command=treeview.yview)

    # 표에 데이터 삽입
    for i in range(len(movie_list_r)):
        treeview.insert('', 'end', text=i, values=movie_list_r[i], iid=str(i)+"번")

    label = tkinter.Label(root, text="Select Movie", width = WIDTH, height = HEIGHT, wraplength = WARPLENGTH, bg = COLOR_BT) 
    label.pack()
    
    # 라벨 내용 바꾸기 (클릭시 이벤트)
    def click_item(event):
        selectedItem = treeview.focus() 
        getValue = treeview.item(selectedItem).get('values')[3] # 딕셔너리의 값만 가져오기
        detail = crawling.show_details(getValue)

        label.configure(text=detail) 

    treeview.bind('<ButtonRelease-1>', click_item) 


    # GUI 실행
    root.mainloop()

#두 번째 페이지
def make_front(movie_list, movie_list_r):
    win.geometry(GEOMETRY)  #사이즈 가로x세로(픽셀)
    win.title("Movie Ranking") #타이틀
    win.option_add("*Font","Courier 40") #기본 폰트와 글자크기 설정

    #첫 번째 페이지
    lab=Label(win, text = "Pop Corn Movie")
    lab.pack(side=TOP, pady=60)
    lab.configure(font=("Courier", 70, "italic"), background=COLOR_BT)

    #첫 번째 페이지 버튼
    btn = Button(win, text="Let's start", command = partial(create_window, movie_list, movie_list_r))
    btn.configure(background=COLOR_BT)
    btn.pack(side=BOTTOM, pady=50)

    button = Button(win,text = "<<Quit", command = win.destroy, width=7,height=1)
    button.configure(font=("Courier", 15, "italic"),background=COLOR_BT)
    button.place(relx=0.8, rely=0.9)

    #배경색
    win.configure(bg=COLOR_BG)

    win.mainloop() #창 열기


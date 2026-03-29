import tkinter
import os
import webbrowser
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class notepad:
	
	__root = Tk()

	# 기본창 크기 설정
	__thisWidth = 300
	__thisHeight = 300
	__thisTextArea = Text(__root)
	__thisMenuBar = Menu(__root)
	__thisFileMenu = Menu(__thisMenuBar, tearoff=0)
	__thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
	
	# 스크롤 설정
	__thisScrollBar = Scrollbar(__thisTextArea)
	__file = None

	def __init__(self,**kwargs):
		# 아이콘 설정
		try:
			self.__root.wm_iconbitmap("MemoX.ico")
		except:
			print("아이콘 에러")
		
		# 창 크기 설정
		try:
			self.__thisWidth = kwargs['width']
		except KeyError:
			print("가로창 크기 에러")
		try:
			self.__thisHeight = kwargs['height']
		except KeyError:
			print("세로창 크기 에러")

		# 창 이름 설정
		self.__root.title("제목없음 - MemoX")
		
		# 가운데로 창 설정
		screenWidth = self.__root.winfo_screenwidth()
		screenHeight = self.__root.winfo_screenheight()
		
		# 왼쪽 오른쪽 정렬
		left = (screenWidth / 2) - (self.__thisWidth / 2)
		
		# 위 아래 정렬
		top = (screenHeight / 2) - (self.__thisHeight /2)

		self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))
		
		# 텍스트 영역의 크기를 자동으로 조절
		self.__root.grid_rowconfigure(0, weight=3)
		self.__root.grid_columnconfigure(0, weight=3)
		self.__thisTextArea.grid(sticky=N + E + S + W)

		# 파일 설정창
		self.__thisMenuBar.add_cascade(label="파일", menu=self.__thisFileMenu)

		# 새로운 파일 열기
		self.__thisFileMenu.add_command(label="새로 만들기", command=self.__newFile)
		
		# 이미 존재하는 파일 열기
		self.__thisFileMenu.add_command(label="열기", command=self.__openFile)
		
		# 파일 저장하기
		self.__thisFileMenu.add_command(label="저장하기", command=self.__saveFile)
		
		# 줄 추가
		self.__thisFileMenu.add_separator()
		self.__thisFileMenu.add_command(label="끝내기", command=self.__quitApplication)

		# 도움창
		self.__thisMenuBar.add_cascade(label="도움말", menu=self.__thisHelpMenu)
		self.__thisHelpMenu.add_command(label="도움말 보기", command=self.__showAbout)
		self.__root.config(menu=self.__thisMenuBar)
		self.__thisScrollBar.pack(side=RIGHT,fill=Y)
		
		# 스크롤바 자동으로 설정
		self.__thisScrollBar.config(command=self.__thisTextArea.yview)
		self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

	# 메모장 끝내는 함수
	def __quitApplication(self):
		self.__root.destroy()

	# 메모장 도움말 보여주는 함수
	def __showAbout(self):
		showinfo("Notepad",view =webbrowser.open("https://github.com/Laytally/memox"))
	
	# 메모장 여는 함수
	def __openFile(self):
		self.__file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
		
		# 조건문
		if self.__file == "":
			self.__file = None
		else:
			self.__root.title(os.path.basename(self.__file) + " - MemoX")
			self.__thisTextArea.delete(1.0,END)
			file = open(self.__file,"r")
			self.__thisTextArea.insert(1.0,file.read())
			file.close()

	# 메모장 새로 여는 함수
	def __newFile(self):
		self.__root.title("제목없음 - MemoX")
		self.__file = None
		self.__thisTextArea.delete(1.0,END)

	# 메모장 저장하는 함수
	def __saveFile(self):
		if self.__file == None:
			self.__file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents","*.txt")])

			if self.__file == "":
				self.__file = None
			else:
				file = open(self.__file,"Untitled")
				file.write(self.__thisTextArea.get(1.0,END))
				file.close()
				self.__root.title(os.path.basename(self.__file) + " - MemoX")

		else:
			file = open(self.__file,"w")
			file.write(self.__thisTextArea.get(1.0,END))
			file.close()

	def run(self):
		# 메인 애플리케이션 실행
		self.__root.mainloop()

# 메인 애플리케이션 실행
notepad = notepad(width=600,height=400)
notepad.run()
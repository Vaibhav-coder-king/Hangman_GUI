import random as r
from tkinter import *
from tkinter import messagebox as mb 
from PIL import Image
from customtkinter import *

def get_words():
	with open(r"assets\hangman_words.txt","r") as f:
		wrd=f.readlines()
		s=[]
		for w in wrd[:-1]:
			s.append(w[:-1])
		s.append(wrd[-1])
		return s


def ex_t():
	if mb.askokcancel(title="exit",message="Are you sure you want to quit?"):
		a.destroy()
	else:
		pass

def backtm():
	if mb.askokcancel(title="exit",message="Are you sure\nyou want to Return to main?"):
		frm_k.place_forget()
		h_l.place_forget()
		chance_left.place_forget()
		w_L.place_forget()
		back_b.place_forget()
		try:
			Restart.grid_forget()
		except:
			pass
		mode_b.place(relx=0.1,rely=0.01,relwidth=0.2,anchor=N)
		theme_b.place(relx=0.35,rely=0.01,relwidth=0.25,anchor=N)
		exit_b.place(relx=0.9,rely=0.01,relwidth=0.2,relheight=0.1,anchor=N)
		play_b.place(relx=0.35,rely=0.5,relwidth=0.2,relheight=0.1,anchor=N)
		rul_b.place(relx=0.6,rely=0.5,relwidth=0.2,relheight=0.1,anchor=N)
		han_l.place(relx=0.5,rely=0.05,anchor=N)

	else:
		pass
		
def show_rules():
	mb.showinfo("Rules", 
		" HANGMAN RULES\n\n"
		"• Guess the hidden word.\n"
		"• Choose one letter at a time.\n"
		"• Correct letters are revealed.\n"
		"• 7 wrong guesses = You lose!\n"
		"• Reveal all letters to win.\n\n"
		"            Good luck!")

def set_mode(mode):
	global kk
	if mode=="Light":
		set_appearance_mode("light")
		a.config(background="white")
		kk=0
	else:
		set_appearance_mode("dark")
		a.config(background="#2b2b2b")
		kk=1
	mode_b.set("Mode")

def set_theme(theme):
	set_default_color_theme(theme)
	a.destroy()
	main()
	

def main():
	global a,words,kk,mode_b,theme_b,exit_b,play_b,rul_b,han_l
	
	words=get_words() #words list 
	
	a=CTk()
	a.title("HANGMAN")
	a.geometry("1200x700")
	a.resizable(True,True)
	if kk==0:
		a.config(background="white")
	else:
		a.config(background="#2b2b2b")
	#for image 
	a_i=CTkImage(light_image=Image.open(r"assets\HANGMAN.jpg"),dark_image=Image.open(r"assets\HANGMAN_d.jpg"),size=(600,300))
	
	
	#__________________________________________________________________
	
	#background 
	han_l=CTkLabel(master=a,image=a_i,text="")
	han_l.place(relx=0.5,rely=0.05,anchor=N)
	
	#for mode change
	mode_b=CTkOptionMenu(master=a,values=["Light","Dark"],command=set_mode,corner_radius=40,height=80,dropdown_font=("Arial",30,"bold"),font=("Arial",40,"bold"),bg_color=("white","#2b2b2b"))
	mode_b.place(relx=0.1,rely=0.01,relwidth=0.2,anchor=N)
	mode_b.set("Mode")

	#for theme change
	theme_b=CTkOptionMenu(master=a,values=["blue","green","dark-blue"],corner_radius=40,height=80,dropdown_font=("Arial",30,"bold"),font=("Arial",40,"bold"),bg_color=("white","#2b2b2b"),command=set_theme)
	theme_b.place(relx=0.35,rely=0.01,relwidth=0.25,anchor=N)
	theme_b.set("Theme")

	#exit button
	exit_b=CTkButton(master=a,command=ex_t,text='Exit',corner_radius=40,font=("Arial",50,"bold"),fg_color="red",bg_color=("white","#2b2b2b"))
	exit_b.place(relx=0.9,rely=0.01,relwidth=0.2,relheight=0.1,anchor=N)
	
	#play Button 
	play_b=CTkButton(master=a,text="Play",font=('consolas',50,"bold"),bg_color=("white","#2b2b2b"),corner_radius=80,command=game)
	play_b.place(relx=0.35,rely=0.5,relwidth=0.2,relheight=0.1,anchor=N)
	
	rul_b=CTkButton(master=a,text="Rule",font=('consolas',50,"bold"),bg_color=("white","#2b2b2b"),corner_radius=80,command=show_rules)
	rul_b.place(relx=0.6,rely=0.5,relwidth=0.2,relheight=0.1,anchor=N)
	a.bind("<Escape>",lambda event: ex_t())
	a.mainloop()
#done_______________________________________________________________________________________________________________________________________________________________________________________________________________________________


def game():
	global h,btm,exit,h_l,Restart,wrong_n,word_c,w_L,l_c,k,words,h_w,chance_left,dl,frm_k,back_b,sw
	try:
		mode_b.place_forget()
		theme_b.place_forget()
		exit_b.place_forget()
		play_b.place_forget()
		rul_b.place_forget()
		han_l.place(relx=0.5,rely=0.0,anchor=N)
	except:
		pass
	#variable
	
	wrong_n=0
	
	word_c=r.choice(words) #word of choice 
	words.remove(word_c)
	l_c=list(word_c) #list of choice 
	
	len_c=len(l_c) #length of choice
	
	dl=["_"]*len_c #display list
	sw="_ "*len_c #string of word
	
	#_________________________________________
	
	h_w=CTkImage(light_image=Image.open(r"assets\hangman_win.png"),dark_image=Image.open(r"assets\hangman_win.png"),size=(500,400))
	
	h=[0 for i in range(8)]
	for j in range(8):
		h[j]=CTkImage(light_image=Image.open(f"assets\\hangman{j}.png"),size=(400,400))
		
	
	
	#_________________________________________
	
	
	back_b=CTkButton(a,text="Back",command=backtm,corner_radius=40,font=("Arial",50,"bold"),fg_color="red",bg_color=("white","#2b2b2b"))
	back_b.place(relx=0.9,rely=0.01,relwidth=0.2,relheight=0.1,anchor=N)
	
	h_l=CTkLabel(a,image=h[wrong_n],text="",bg_color="white")
	h_l.place(relx=0.2,rely=0.35,anchor=N)
	
	chance_left=CTkLabel(a,text=f"{7-wrong_n} Chances Left!!",fg_color=("white","#2b2b2b"),text_color=("red","#00ff00"),font=("Arial",40,"bold"))
	chance_left.place(relx=0.2,rely=0.25,anchor=N)
	
	
	x1=0.65
	w_L=CTkLabel(a,text=sw,text_color="#0000ff",fg_color=("white","#2b2b2b"),font=('Arial', 30,"bold"))
	w_L.place(relx=x1,rely=0.45,anchor=N)
	
	#_______________keyboard_______________
	
	frm_k=CTkFrame(a,fg_color=("white","#2b2b2b"))
	frm_k.place(relx=0.65,rely=0.55,anchor=N)	
	k=[[x for x in "abcdefg"],[x for x in "hijklmn"],[x for x in "opqrstu"],[x for x in "vwxyz"]]
	
	for nl,lst in enumerate(k):
		for wl,www in enumerate(lst):
			a.bind(f"<{www}>",lambda event,x=www,y=(nl,wl): clk(x,y))

	for j,n in enumerate(k[:-1]):
		for i,v in enumerate(n):
			k[j][i]=Button(frm_k,text=v,fg="#0000ff",font=('consolas',30,"bold"),bg="white",width=3,height=1,relief="raised",bd=3,command=lambda x=v,y=(j,i): clk(x,y))
			k[j][i].grid(row=j,column=i)
			
	for i,v in enumerate(k[-1]):
		k[3][i]=Button(frm_k,text=v,fg="#0000ff",font=('consolas',30,"bold"),bg="white",width=3,height=1,relief="raised",bd=3,command=lambda x=v,y=(3,i): clk(x,y))
		k[3][i].grid(row=3,column=i+1)
	
	Restart=Button(frm_k,text="Restart",font=('consolas',15,"bold"),fg="gold",bg="black",activeforeground="cyan",activebackground="black",relief="raised", bd=10,command=restart)
	#Restart.grid(row=4,column=1,columnspan=5)
	
	#_______________________________________

def win_chk(w):
	go=False
	if w==7:
		mb.showinfo(title="Result",message="You Lose!!!")
		sw=""
		for e in l_c:
			sw+=e+" "
		w_L.configure(text=sw)
		go=True
	elif dl==l_c:
		h_l.configure(image=h_w)
		mb.showinfo(title="Result",message="You win!!!")
		go=True
	if go:
		for j,n in enumerate(k[:-1]):
			for i,v in enumerate(n):
				k[j][i].config(state="disabled")
		for i,v in enumerate(k[-1]):
			k[3][i].config(state="disabled")
		Restart.grid(row=4,column=1,columnspan=5)
		
#clk		
def clk(x,y):
	global wrong_n,dl
	if k[y[0]][y[1]]["state"]=="disabled":
		return
	
	if x in word_c:
		for i,s in enumerate(l_c):
			if x==s:
				dl[i]=s
			sw=""
			for e in dl:
				sw+=e+" "
			w_L.configure(text=sw)
		ro,co=y
		k[ro][co]["bg"]="#00ff00"
		k[ro][co]["state"]="disabled"
		
	else:
		wrong_n+=1
		h_l.configure(image=h[wrong_n])
		chance_left.configure(text=f"{7-wrong_n} Chances Left!!")
		ro,co=y
		k[ro][co]["bg"]="red"
		k[ro][co]["fg"]="#00ff00"
		k[ro][co]["state"]="disabled"
	win_chk(wrong_n)
	
def restart():
	global wrong_n,dl,word_c,l_c,len_c,sw,k,words,h_w,h_l,chance_left
	Restart.grid_forget()
	for j,n in enumerate(k[:-1]):
		for i,v in enumerate(n):
			k[j][i].config(state="normal",bg="white",fg="#0000ff")
	for i,v in enumerate(k[-1]):
		k[3][i].config(state="normal",bg="white",fg="#0000ff")
	
	wrong_n=0
	if len(words)==0:
		mb.showinfo(title="No more words",message="No more words available\nReturning to main menu")
		a.destroy()
		main()
		return
	word_c=r.choice(words) #word of choice 
	words.remove(word_c)
	l_c=list(word_c) #list of choice 
	
	len_c=len(l_c) #length of choice
	
	dl=["_"]*len_c #display list
	sw="_ "*len_c #string of word
	w_L.configure(text=sw)
	h_l.configure(image=h[wrong_n])
	chance_left.configure(text=f"{7-wrong_n} Chances Left!!")	
#_________________________________________
if __name__=="__main__":
	#set appearance mode
	kk=0
	set_appearance_mode("light")
	set_default_color_theme("blue")
	#starting window
	main()

import tkinter as t
import math
from os import path as op
# from PIL import Image, ImageTk - image import for icon not working as intended.

w_reps = 0
w_timer = None
def main() -> None:
    # ---------------------------- CONSTANTS ------------------------------- #
    PINK = "#e2979c"
    RED = "#e7305b"
    GREEN = "#9bdeac"
    YELLOW = "#f7f5dd"
    FONT_NAME = "Courier"
    WORK_MIN = 25
    SHORT_BREAK_MIN = 5
    LONG_BREAK_MIN = 20  
    
    w_curr_dir = op.dirname(__file__)

    w_window = t.Tk()
    w_window.title("Pomodoro Timer")  
    
    # w_im = Image.open('images/timer.png')
    # w_photo = ImageTk.PhotoImage(w_im)
    # w_window.wm_iconphoto(True, w_photo)                  
    
    w_window.config(padx=100, pady=50, bg=YELLOW)        
    
    
    # ---------------------------- TIMER RESET ------------------------------- # 
    
    def start_timer() -> None:
        # raise NotImplementedError("'Start' is not impletemeted yet!")
        global w_reps
        w_reps += 1
        w_work_secs        = WORK_MIN * 60
        w_short_break_secs = SHORT_BREAK_MIN * 60
        w_long_break_secs = LONG_BREAK_MIN * 60        
        w_start_button["state"] = "disabled"
                
        if w_reps%8 == 0:
            w_title_label.config(text="Break", fg=RED)
            count_down(w_long_break_secs)                 
        elif w_reps%2 == 0 :                
            w_title_label.config(text="Break", fg=PINK)                
            count_down(w_short_break_secs)                   
        else:
            count_down(w_work_secs)       
            w_title_label.config(text="Work", fg=GREEN)                         
        
    # ---------------------------- TIMER MECHANISM ------------------------------- # 
    def reset_timer() -> None:
        # raise NotImplementedError("'Reset' is not impletemeted yet!")        
        global w_reps, w_timer
        w_reps = 0
        w_window.after_cancel(w_timer)
        w_canvas.itemconfig(w_timer_text, text="00:00")
        w_check_marks.config(text="")
        w_title_label.config(text="Timer", fg=GREEN)
        w_start_button["state"] = "active"

        
        
    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    def count_down(p_count) -> None:                
        w_min: int  = math.floor(p_count / 60)
        w_sec: int  = p_count % 60
        w_time_remain: str = f"{w_min:02}:{w_sec:02}"
        w_canvas.itemconfig(w_timer_text, text=w_time_remain)        
        if p_count > 0:        
            global w_timer            
            w_timer = w_window.after(1000, count_down, p_count - 1)
        else:
            start_timer()
            w_marks=""
            w_work_sessions = math.floor(w_reps/2)
            for _ in w_work_sessions:
                w_marks += "✔"
            w_check_marks.config(text=w_marks)
                


    # ---------------------------- UI SETUP ------------------------------- #    
    
    w_title_label  = t.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"))         
    w_start_button = t.Button(text="Start", command=start_timer)
    w_end_button   = t.Button(text="Reset", command=reset_timer)    
    w_check_marks  = t.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 28, "bold"))

    # Create Canvas 
    w_canvas = t.Canvas(w_window, width=200, height=224, bg=YELLOW, highlightthickness=0)    
    # Display image and Text
    w_bg_image = t.PhotoImage(file = f"{w_curr_dir}/images/matrix.png")     
    #x,y..., image, anchor(optional, eg t.CENTER)
    w_canvas.create_image(100, 112, image = w_bg_image)     
    w_timer_text = w_canvas.create_text(112, 130, text = "00:00", fill="white", font=(FONT_NAME, 28, "bold"))             

    #Add to display using grid    
    w_title_label.grid(row=0, column=1)
    w_canvas.grid(row=1, column=1)
    w_start_button.grid(row=2, column=0)    
    w_end_button.grid(row=2, column=2)
    w_check_marks.grid(row=3, column=1)        
    


    w_window.mainloop()#Keep window open

if __name__ == "__main__":
    main()

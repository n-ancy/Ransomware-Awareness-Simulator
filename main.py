import tkinter as tk
from PIL import Image, ImageTk
import random
import time

SIMULATION_TIME = 120

root = tk.Tk()
root.title("YOUR FILES ARE ENCRYPTING")

root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

start_time = time.time()

screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()

# ==========================
# Background Image
# ==========================

img = Image.open("background.png")
img = img.resize((screen_w, screen_h))
bg_img = ImageTk.PhotoImage(img)

canvas = tk.Canvas(
    root,
    width=screen_w,
    height=screen_h,
    highlightthickness=0
)

canvas.pack(fill="both", expand=True)

canvas.create_image(
    0,
    0,
    image=bg_img,
    anchor="nw"
)

# ==========================
# Overlay Panel
# ==========================

canvas.create_rectangle(
    20,
    20,
    950,
    700,
    fill="black",
    stipple="gray50",
    outline=""
)

# ==========================
# Header
# ==========================

canvas.create_text(
    50,
    50,
    anchor="nw",
    fill="#ff2222",
    font=("Consolas", 30, "bold"),
    text="FILES ARE BEING PROCESSED"
)

# ==========================
# Timer
# ==========================

timer_text = canvas.create_text(
    50,
    110,
    anchor="nw",
    fill="white",
    font=("Consolas", 18),
    text=""
)

# ==========================
# Progress Bar
# ==========================

canvas.create_rectangle(
    50,
    160,
    750,
    190,
    outline="white"
)

progress_bar = canvas.create_rectangle(
    50,
    160,
    50,
    190,
    fill="#ff2222",
    outline=""
)

# ==========================
# Status Text
# ==========================

canvas.create_text(
    50,
    230,
    anchor="nw",
    fill="white",
    font=("Consolas", 14),
    text="""
Processing files...
Scanning local storage...
Preparing file inventory...

"""
)

# ==========================
# Activity Log
# ==========================

log_box = tk.Text(
    root,
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    font=("Consolas", 10)
)

canvas.create_window(
    50,
    380,
    anchor="nw",
    width=850,
    height=260,
    window=log_box
)

fake_files = [
    "Budget_2026.xlsx",
    "Payroll.xlsx",
    "Employee_Records.xlsx",
    "Customer_List.csv",
    "Contracts.pdf",
    "Engineering_Drawing.dwg",
    "SAP_Backup.zip",
    "Project_Plan.pptx",
    "HR_Database.accdb",
    "Invoices_2026.pdf",
    "Production_Data.db",
    "Research_Data.xlsx",
    "Photos_Archive.zip",
    "Source_Code_Backup.zip",
    "Meeting_Notes.docx",
    "Financial_Report_Q4.xlsx",
    "Design_Specification.docx",
    "Backup_Server_01.zip",
    "Operations_Data.csv",
    "Inventory_Report.xlsx"
]

# ==========================
# Prevent Window Close
# ==========================

def on_close():
    elapsed = time.time() - start_time

    if elapsed >= SIMULATION_TIME:
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# ==========================
# Focus Monitoring
# ==========================

def on_focus_out(event):
    log_box.insert(
        "end",
        "[INFO] User switched away from simulator\n"
    )
    log_box.see("end")

def on_focus_in(event):
    log_box.insert(
        "end",
        "[INFO] User returned to simulator\n"
    )
    log_box.see("end")

root.bind("<FocusOut>", on_focus_out)
root.bind("<FocusIn>", on_focus_in)

# ==========================
# Updates
# ==========================

def update_screen():

    elapsed = int(time.time() - start_time)
    remaining = max(0, SIMULATION_TIME - elapsed)

    mins = remaining // 60
    secs = remaining % 60

    canvas.itemconfig(
        timer_text,
        text=f"TIME REMAINING: {mins:02d}:{secs:02d}"
    )

    percent = min(
        100,
        (elapsed / SIMULATION_TIME) * 100
    )

    canvas.coords(
        progress_bar,
        50,
        160,
        50 + (700 * percent / 100),
        190
    )

    if random.random() < 0.7:

        filename = random.choice(fake_files)

        action = random.choice([
            "Scanning",
            "Processing",
            "Indexing",
            "Reviewing"
        ])

        log_box.insert(
            "end",
            f"[{time.strftime('%H:%M:%S')}] {action} {filename}\n"
        )

        log_box.see("end")

    if remaining <= 0:
        root.destroy()
    else:
        root.after(500, update_screen)

update_screen()

root.mainloop()
import tkinter as tk


def convert():
    try:
        rub = ent_r.get()
        if var.get() == 0:
            res = float(rub) * 9.1
            lbl_result["text"] = f"{round(res, 2)} Рублей"
        elif var.get() == 1:
            res = float(rub) / 9.1
            lbl_result["text"] = f"{round(res, 2)} Юаней"
    except ValueError:
        lbl_result["text"] = "ОШИБКА!"



window = tk.Tk()
window.title("Конвертер валют")
window.geometry('400x100')
frm_entry = tk.Frame(master=window)
ent_r = tk.Entry(master=frm_entry, width=10)
lbl_r = tk.Label(master=frm_entry, text="Введите сумму перевода")

ent_r.grid(row=0, column=0, sticky="e")
lbl_r.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(master=window, text="Перевести", command=convert)
lbl_result = tk.Label(master=window)

var = tk.IntVar()
var.set(0)

rad_fld = tk.Frame(master=window)
r1 = tk.Radiobutton(master=rad_fld, text="В рубли", variable=var, value=0)
r2 = tk.Radiobutton(master=rad_fld, text="В Юани", variable=var, value=1)


r1.grid(row=0, column=0)
r2.grid(row=0, column=1)


frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)
rad_fld.grid(row=1, column=0)

window.mainloop()
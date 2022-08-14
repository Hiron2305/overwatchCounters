from tkinter import *
from PIL import ImageTk
from PIL import Image
roles = {"Tank": ["Roadhog", "Wrecking_Ball", "D.Va", "Winston", "Sigma", "Orisa", "Zarya", "Reinhardt"],
         "DD": ["Hanzo", "Cassidy", "Reaper", "Echo", "Ashe", "Genji", "Widowmaker", "Doomfist",
                "Tracer", "Solider_76", "Junkrat", "Mei", "Pharah", "Torbjorn", "Sombra", "Symmetra", "Bastion"],
         "Healer": ["Moira", "Baptiste", "Lucio", "Mercy", "Ana", "Zenyatta", "Brigitte"]}

Damage = list()
Tank = list()
Heal = list()

root = Tk()
root.geometry("1920x1080")
root.title("OverCounters")
greeting = Label(text="Version for 35'th season of Competitive mode", font="Courier 10")
greeting.pack()
dd_label = Label(text="Damage dealers: ", font="Courier 15")
dd_label.place(x=10, y=70)
cls = Button(text="ready", command=root.destroy, height=1, width=15, font="Courier 15")
cls.pack(fill=Y, pady=350)

genji_image = ImageTk.PhotoImage(file="genji_profile_pic.png")
genji_larger_image = genji_image._PhotoImage__photo.subsample(2, 2)
Genji = Button(root,
               image=genji_larger_image,
               command=lambda: Damage.append("Genji"),
               height=80,
               width=80)
Genji.place(x=200, y=40)

ashe_image = ImageTk.PhotoImage(file="ashe_profile_pic.png")
ashe_larger_image = ashe_image._PhotoImage__photo.subsample(2, 2)
Ashe = Button(root,
              image=ashe_larger_image,
              command=lambda: Damage.append("Ashe"),
              height=80,
              width=80)
Ashe.place(x=300, y=40)

bastion_image = ImageTk.PhotoImage(file="bastion_profile_pic.png")
bastion_larger_image = bastion_image._PhotoImage__photo.subsample(2, 2)
Bastion = Button(root,
                 image=bastion_larger_image,
                 command=lambda: Damage.append("Bastion"),
                 height=80,
                 width=80)
Bastion.place(x=400, y=40)

cassidy_image = ImageTk.PhotoImage(file="cassidy_profile_pic.png")
cassidy_larger_image = cassidy_image._PhotoImage__photo.subsample(2, 2)
Cassidy = Button(root,
                 image=cassidy_larger_image,
                 command=lambda: Damage.append("Cassidy"),
                 height=80,
                 width=80)
Cassidy.place(x=500, y=40)

doom_image = ImageTk.PhotoImage(file="doom_profile_pic.png")
doom_larger_image = doom_image._PhotoImage__photo.subsample(2, 2)
Doom = Button(root,
              image=doom_larger_image,
              command=lambda: Damage.append("Doomfist"),
              height=80,
              width=80)
Doom.place(x=600, y=40)

echo_image = ImageTk.PhotoImage(file="echo_profile_pic.png")
echo_larger_image = echo_image._PhotoImage__photo.subsample(2, 2)
Echo = Button(root,
              image=echo_larger_image,
              command=lambda: Damage.append("Echo"),
              height=80,
              width=80)
Echo.place(x=700, y=40)

hanzo_image = ImageTk.PhotoImage(file="hanzo_profile_pic.png")
hanzo_larger_image = hanzo_image._PhotoImage__photo.subsample(2, 2)
Hanzo = Button(root,
               image=hanzo_larger_image,
               command=lambda: Damage.append("Hanzo"),
               height=80,
               width=80)
Hanzo.place(x=800, y=40)

junk_image = ImageTk.PhotoImage(file="junk_profile_pic.png")
junk_larger_image = junk_image._PhotoImage__photo.subsample(2, 2)
Junk = Button(root,
              image=junk_larger_image,
              command=lambda: Damage.append("Junkrat"),
              height=80,
              width=80)
Junk.place(x=900, y=40)

mei_image = ImageTk.PhotoImage(file="mei_profile_pic.png")
mei_larger_image = mei_image._PhotoImage__photo.subsample(2, 2)
Mei = Button(root,
             image=mei_larger_image,
             command=lambda: Damage.append("Mei"),
             height=80,
             width=80)
Mei.place(x=1000, y=40)

pharah_image = ImageTk.PhotoImage(file="Pharah_profile_pic.png")
pharah_larger_image = pharah_image._PhotoImage__photo.subsample(2, 2)
Pharah = Button(root,
                image=pharah_larger_image,
                command=lambda: Damage.append("Pharah"),
                height=80,
                width=80)
Pharah.place(x=1100, y=40)

reaper_image = ImageTk.PhotoImage(file="reaper_profile_pic.png")
reaper_larger_image = reaper_image._PhotoImage__photo.subsample(2, 2)
Reaper = Button(root,
                image=reaper_larger_image,
                command=lambda: Damage.append("Reaper"),
                height=80,
                width=80)
Reaper.place(x=1200, y=40)

solider_image = ImageTk.PhotoImage(file="solider_profile_pic.png")
solider_larger_image = solider_image._PhotoImage__photo.subsample(2, 2)
Solider = Button(root,
                 image=solider_larger_image,
                 command=lambda: Damage.append("Solider_76"),
                 height=80,
                 width=80)
Solider.place(x=1200, y=40)

sombra_image = ImageTk.PhotoImage(file="sombra_profile_pic.png")
sombra_larger_image = sombra_image._PhotoImage__photo.subsample(2, 2)
Sombra = Button(root,
                image=sombra_larger_image,
                command=lambda: Damage.append("Sombra"),
                height=80,
                width=80)
Sombra.place(x=1300, y=40)

sym_image = ImageTk.PhotoImage(file="sym_profile_pic.png")
sym_larger_image = sym_image._PhotoImage__photo.subsample(2, 2)
Sym = Button(root,
             image=sym_larger_image,
             command=lambda: Damage.append("Symmetra"),
             height=80,
             width=80)
Sym.place(x=1400, y=40)

torb_image = ImageTk.PhotoImage(file="torb_profile_pic.png")
torb_larger_image = torb_image._PhotoImage__photo.subsample(2, 2)
Torb = Button(root,
              image=torb_larger_image,
              command=lambda: Damage.append("Torbjorn"),
              height=80,
              width=80)
Torb.place(x=1500, y=40)

tracer_image = ImageTk.PhotoImage(file="tracer_profile_pic.png")
tracer_larger_image = tracer_image._PhotoImage__photo.subsample(2, 2)
Tracer = Button(root,
                image=tracer_larger_image,
                command=lambda: Damage.append("Tracer"),
                height=80,
                width=80)
Tracer.place(x=1600, y=40)

widow_image = ImageTk.PhotoImage(file="widow_profile_pic.png")
widow_larger_image = widow_image._PhotoImage__photo.subsample(2, 2)
Widow = Button(root,
               image=widow_larger_image,
               command=lambda: Damage.append("Widowmaker"),
               height=80,
               width=80)
Widow.place(x=1700, y=40)

Tank_label = Label(text="Tanks: ", font="Courier 15")
Tank_label.place(x=120, y=180)

dva_image = ImageTk.PhotoImage(file="dva_profile_pic.png")
dva_larger_image = dva_image._PhotoImage__photo.subsample(2, 2)
Dva = Button(root,
             image=dva_larger_image,
             command=lambda: Tank.append("D.Va"),
             height=80,
             width=80)
Dva.place(x=200, y=150)

orisa_image = ImageTk.PhotoImage(file="orisa_profile_pic.png")
orisa_larger_image = orisa_image._PhotoImage__photo.subsample(2, 2)
Orisa = Button(root,
               image=orisa_larger_image,
               command=lambda: Tank.append("Orisa"),
               height=80,
               width=80)
Orisa.place(x=300, y=150)

rein_image = ImageTk.PhotoImage(file="rein_profile_pic.png")
rein_larger_image = rein_image._PhotoImage__photo.subsample(2, 2)
Rein = Button(root,
              image=rein_larger_image,
              command=lambda: Tank.append("Reinhardt"),
              height=80,
              width=80)
Rein.place(x=400, y=150)

hog_image = ImageTk.PhotoImage(file="hog_profile_pic.png")
hog_larger_image = hog_image._PhotoImage__photo.subsample(2, 2)
Hog = Button(root,
             image=hog_larger_image,
             command=lambda: Tank.append("Roadhog"),
             height=80,
             width=80)
Hog.place(x=500, y=150)

sig_image = ImageTk.PhotoImage(file="Sigma_profile_pic.png")
sig_larger_image = sig_image._PhotoImage__photo.subsample(2, 2)
Sig = Button(root,
             image=sig_larger_image,
             command=lambda: Tank.append("Sigma"),
             height=80,
             width=80)
Sig.place(x=600, y=150)

win_image = ImageTk.PhotoImage(file="win_profile_pic.png")
win_larger_image = win_image._PhotoImage__photo.subsample(2, 2)
Win = Button(root,
             image=win_larger_image,
             command=lambda: Tank.append("Winston"),
             height=80,
             width=80)
Win.place(x=700, y=150)

wreck_image = ImageTk.PhotoImage(file="wreck_profile_pic.png")
wreck_larger_image = wreck_image._PhotoImage__photo.subsample(2, 2)
Wreck = Button(root,
               image=wreck_larger_image,
               command=lambda: Tank.append("Wrecking_Ball"),
               height=80,
               width=80)
Wreck.place(x=800, y=150)

zar_image = ImageTk.PhotoImage(file="zar_profile_pic.png")
zar_larger_image = zar_image._PhotoImage__photo.subsample(2, 2)
Zar = Button(root,
             image=zar_larger_image,
             command=lambda: Tank.append("Zarya"),
             height=80,
             width=80)
Zar.place(x=900, y=150)

Heal_label = Label(text="Healers: ", font="Courier 15")
Heal_label.place(x=90, y=290)

ana_image = ImageTk.PhotoImage(file="ana_profile_pic.png")
ana_larger_image = ana_image._PhotoImage__photo.subsample(2, 2)
Ana = Button(root,
             image=ana_larger_image,
             command=lambda: Heal.append("Ana"),
             height=80,
             width=80)
Ana.place(x=200, y=260)

bap_image = ImageTk.PhotoImage(file="bap_profile_pic.png")
bap_larger_image = bap_image._PhotoImage__photo.subsample(2, 2)
Bap = Button(root,
             image=bap_larger_image,
             command=lambda: Heal.append("Baptiste"),
             height=80,
             width=80)
Bap.place(x=300, y=260)

brg_image = ImageTk.PhotoImage(file="brg_profile_pic.png")
brg_larger_image = brg_image._PhotoImage__photo.subsample(2, 2)
Brg = Button(root,
             image=brg_larger_image,
             command=lambda: Heal.append("Brigitte"),
             height=80,
             width=80)
Brg.place(x=400, y=260)

luc_image = ImageTk.PhotoImage(file="luc_profile_pic.png")
luc_larger_image = luc_image._PhotoImage__photo.subsample(2, 2)
Luc = Button(root,
             image=luc_larger_image,
             command=lambda: Heal.append("Lucio"),
             height=80,
             width=80)
Luc.place(x=500, y=260)

mer_image = ImageTk.PhotoImage(file="mer_profie_pic.png")
mer_larger_image = mer_image._PhotoImage__photo.subsample(2, 2)
Mer = Button(root,
             image=mer_larger_image,
             command=lambda: Heal.append("Mercy"),
             height=80,
             width=80)
Mer.place(x=600, y=260)

moi_image = ImageTk.PhotoImage(file="moi_profile_pic.png")
moi_larger_image = moi_image._PhotoImage__photo.subsample(2, 2)
Moi = Button(root,
             image=moi_larger_image,
             command=lambda: Heal.append("Moira"),
             height=80,
             width=80)
Moi.place(x=700, y=260)

zen_image = ImageTk.PhotoImage(file="zen_profile_pic.png")
zen_larger_image = zen_image._PhotoImage__photo.subsample(2, 2)
Zen = Button(root,
             image=zen_larger_image,
             command=lambda: Heal.append("Zenyatta"),
             height=80,
             width=80)
Zen.place(x=800, y=260)
root.mainloop()

print("List of character: ")

for key, value in roles.items():
    print(key, ':', value)

print(" ")
print("Version for 35'th season of Competitive mode")
print(" ")
first_tank = Tank[0]
second_tank = Tank[1]
first_dd = Damage[0]
second_dd = Damage[1]
first_healer = Heal[0]
second_healer = Heal[1]
print(" ")

first_enemy = {"Bastion": ["Genji", "Widowmaker", "Hanzo"],
               "D.Va": ["Mei", "Junkrat", "Reaper"],
               "Genji": ["Mei", "Winston", "Zarya"],
               "Hanzo": ["Genji", "Tracer", "Winston"],
               "Mercy": ["Tracer", "Genji", "Roadhog"],
               "Junkrat": ["Pharah", "Widowmaker", "Solider_76"],
               "Lucio": ["Mei", "Pharah", "Cassidy"],
               "Cassidy": ["Widowmaker", "Genji", "Pharah"],
               "Mei": ["Pharah", "Reaper", "Widowmaker"],
               "Pharah": ["Solider_76", "Roadhog", "Torbjorn"],
               "Reaper": ["Cassidy", "Pharah", "Genji"],
               "Reinhardt": ["Mei", "Bastion", "Junkrat"],
               "Roadhog": ["Reaper", "Mei", "D.Va"],
               "Solider_76": ["Genji", "Roadhog", "Cassidy"],
               "Symmetra": ["Pharah", "Roadhog", "Winston"],
               "Torbjorn": ["Widowmaker", "Hanzo", "Junkrat"],
               "Tracer": ["Cassidy", "Roadhog", "Pharah"],
               "Widowmaker": ["Genji", "D.Va", "Winston"],
               "Zarya": ["Pharah", "Reaper", "Mei"],
               "Zenyatta": ["Widowmaker", "Reaper", "Genji"],
               "Sigma": ["D.Va", "Doomfist", "Mei"],
               "Wrecking_Ball": ["Ana", "Bastion", "Brigitte"],
               "Winston": ["D.Va", "Bastion", "Reaper"],
               "Orisa": ["Genji", "Hanzo", "Moira"],
               "Echo": ["Cassidy", "Solider_76", "Widowmaker"],
               "Ashe": ["Doomfist", "D.Va", "Genji"],
               "Doomfist": ["Cassidy", "Orisa", "Pharah"],
               "Sombra": ["Hanzo", "Junkrat", "Cassidy"],
               "Moira": ["Ana", "Baptiste", "D.Va"],
               "Baptiste": ["Ana", "Ashe", "Bastion"],
               "Ana": ["Doomfist", "D.Va", "Genji"],
               "Brigitte": ["Junkrat", "Pharah", "Reaper"]}

res_roles = {"Tank": [],
             "DD": [],
             "Healer": []}

res_list = list()
Team = list()
f_tank_counters = first_enemy[first_tank]
s_tank_counters = first_enemy[second_tank]
f_dd_counters = first_enemy[first_dd]
s_dd_counters = first_enemy[second_dd]
f_heal_counters = first_enemy[first_healer]
s_heal_counters = first_enemy[second_healer]
res_list.extend(
    [*f_tank_counters, *s_tank_counters, *f_dd_counters, *s_dd_counters, *f_heal_counters, *s_heal_counters])

for i in res_list:
    if i in roles["Tank"]:
        Tank_counter = res_list.count(i)
        for T in range(Tank_counter):
            res_list.remove(i)
        res_roles["Tank"].append([i, Tank_counter])

    if i in roles["DD"]:
        DD_counter = res_list.count(i)
        for D in range(DD_counter):
            res_list.remove(i)
        res_roles["DD"].append([i, DD_counter])

    if i in roles["Healer"]:
        Healer_counter = res_list.count(i)
        for H in range(Healer_counter):
            res_list.remove(i)
        res_roles["Healer"].append([i, Healer_counter])

list_for_max_DD = list()
list_for_max_Healer = list()
list_for_max_Tank = list()
t_res_2 = list()
for T_count in res_roles["Tank"]:
    list_for_max_Tank.append(T_count[1])
if len(list_for_max_Tank) >= 2:
    for p in range(2):
        for T_true_ret in res_roles["Tank"]:
            if T_true_ret[1] == max(list_for_max_Tank, default=0):
                t_res_2.append(T_true_ret[0])
                list_for_max_Tank.remove(max(list_for_max_Tank))
else:
    if len(res_roles["Tank"]) == 0:
        Save_pack_for_Tank = [["Reinhardt", 1], ["Roadhog", 1]]
        res_roles["Tank"].extend(Save_pack_for_Tank)
        for T_true_ret in res_roles["Tank"]:
            t_res_2.append(T_true_ret[0])
    else:
        for T_true_ret in res_roles["Tank"]:
            t_res_2 = (T_true_ret[0], "+ Everyone")

dd_res_2 = list()
for DD_count in res_roles["DD"]:
    list_for_max_DD.append(DD_count[1])
if len(list_for_max_DD) >= 2:
    for p in range(2):
        for D_true_ret in res_roles["DD"]:
            if D_true_ret[1] == max(list_for_max_DD, default=0):
                dd_res_2.append(D_true_ret[0])
                list_for_max_DD.remove(max(list_for_max_DD))
else:
    for D_true_ret in res_roles["DD"]:
        dd_res_2 = (D_true_ret[0], "+ Everyone")

for H_count in res_roles["Healer"]:
    list_for_max_Healer.append(H_count[1])

h_res_2 = list()
if len(list_for_max_Healer) >= 2:
    for H_true_ret in res_roles["Healer"]:
        if H_true_ret[1] == max(list_for_max_Healer):
            h_res_2.append(H_true_ret[0])
            list_for_max_Healer.remove(max(list_for_max_Healer))
else:
    if len(res_roles["Healer"]) == 0:
        Save_pack_for_healler = [["Mercy", 1], ["Moira", 1]]
        res_roles["Healer"].extend(Save_pack_for_healler)
        for H_true_ret in res_roles["Healer"]:
            h_res_2.append(H_true_ret[0])
    else:
        for H_true_ret in res_roles["Healer"]:
            h_res_2 = (H_true_ret[0], "+ Everyone")

sss_t = ", ".join(t_res_2)
sss_heal = ", ".join(h_res_2)
sss_dd = ", ".join(dd_res_2)

okno2 = Tk()
okno2.geometry("1920x1080")
okno2.title("OverCounters")
greeting2 = Label(text="Version for 35'th season of Competitive mode", font="Courier 10")
greeting2.pack()
res_label = Label(text="Your team - ", font="Courier 15")
res_label.place(x=10, y=70)
pre_res_label_t = Label(text="Tanks: ", font = "Courier 15")
pre_res_label_t.place(x=120,y=120)
res_label_t = Label(text=sss_t, font="Courier 15")
res_label_t.place(x=200, y=120)
pre_res_label_dd = Label(text = "DD: ",font="Courier 15")
pre_res_label_dd.place(x=120,y=150)
res_label_dd = Label(text=sss_dd, font="Courier 15")
res_label_dd.place(x=170, y=150)
pre_res_label_h = Label(text="Healers: ", font="Courier 15")
pre_res_label_h.place(x=120,y=180)
res_label_heal = Label(text= sss_heal, font="Courier 15")
res_label_heal.place(x=225, y=180)
thx_label = Label(text="Thank you for using my app!", font = "Courier 15")
thx_label.place(x=1200,y=150)
guess_label = Label(text="↑ the place in line determines mean the importance of the character in the team.",font="Courier 15")
guess_label.place(x=120,y=250)

file = "Paw.gif"
info = Image.open(file)
frames = info.n_frames

im = [PhotoImage(file=file,format=f'gif -index {i}')for i in range(frames)]
count=0
def animation(count):
    im2 = im[count]
    gif_label.configure(image = im2)
    count+=1
    if count == frames:
        count = 0
    anim = okno2.after(100,lambda: animation(count))

gif_label = Label(image="")

gif_label.place(x=1250,y=200)

animation(count)

okno2.mainloop()
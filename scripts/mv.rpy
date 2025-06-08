define popy = Character("POPY",   color="#ff528c", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#ff528c") ])
define rose = Character("ROSE",   color="#3933ab", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#3933ab") ])
define pstl = Character("PASTEL", color="#c8f0d8", who_outlines=[ (3, "#010101") ], what_outlines=[ (2, "#778f81") ]) #fabdba
define halo = Character("HALO",   color="#ffeaba", who_outlines=[ (3, "#010101") ], what_outlines=[ (2, "#baab88") ])
define aver = Character("AVER",   color="#871143", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#871143") ])

define popy_rose = Character("POPY & ROSE",   color="#c042d5", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#c042d5") ])
define halo_pstl = Character("HALO & PASTEL", color="#daf8c1", who_outlines=[ (3, "#010101") ], what_outlines=[ (2, "#a0b68d") ])

define idle = Character("", color="#ffffff", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#010101") ])
define popy_rose_halo_pstl = Character("YUME", color="#e6937d", who_outlines=[ (3, "#fefefe") ], what_outlines=[ (2, "#e6937d") ])

transform popy_single:
    ypos 300
    xalign 0.5
transform rose_single:
    ypos 300
    xalign 0.5
transform pstl_single:
    ypos 300
    xalign 0.4
transform halo_single:
    ypos 200
    xalign 0.5

transform popy_double:
    ypos 300
    xalign 0.2
transform rose_double:
    ypos 300
    xalign 0.8

transform halo_double:
    ypos 200
    xalign 0.1
transform pstl_double:
    ypos 300
    xalign 0.8

transform popy_all:
    ypos 300
    xalign 0.0
transform rose_all:
    ypos 300
    xalign 0.25
transform halo_all:
    ypos 200
    xalign 0.68
transform pstl_all:
    ypos 300
    xalign 1.1

define config.font_name_map["j"] = "epmarugo.ttf"
define config.font_name_map["z"] = "tsangeryuyangw5.ttf"

define shorten = 0.5
define load_shorten = 0.0

screen m_info():
    text "9-tie - Only one yell\n夢ノ結唱.exe":
        align (1.0, 0.0)
        text_align 1.0
        size 24
        color "#fefefe"
        outlines [(2, "#010101")]
        font "NotoSansMonoCJKjp-Bold.otf"

label mv:

    play music story noloop

    scene rain
    with dissolve

    # show narrator at narrator_single

    while (renpy.music.get_pos() or 0) < 1.0:
        $ renpy.pause(0.005, hard=True)

    idle "{font=j}{b}{color=#e6937d}
    Only one yell{/color}\n
    Original: 9-tie\n
    Cover: 夢ノ結唱{/b}{/font}
    {fast}{nw=[11.96-shorten-load_shorten]}"

    show screen m_info

    # hide narrator

    show halo at halo_single

    while (renpy.music.get_pos() or 0) < 13.55:
        $ renpy.pause(0.005, hard=True)

    halo "{font=j}{b}One day、雨が降る日も聞こえていたんだ。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.83-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 20.38:
        $ renpy.pause(0.005, hard=True)

    halo "{font=j}{b}私を呼ぶ声が。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[3.06-shorten]}"

    hide halo

    show popy at popy_single

    while (renpy.music.get_pos() or 0) < 23.44:
        $ renpy.pause(0.005, hard=True)

    popy "{font=j}{b}どんな時も私のそばに居てくれたね。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.31-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 28.75:
        $ renpy.pause(0.005, hard=True)

    popy "{font=j}{b}前を向いてまた歩いていけるように。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.16-shorten]}"

    hide popy

    show rose at rose_single

    while (renpy.music.get_pos() or 0) < 34.91:
        $ renpy.pause(0.005, hard=True)

    rose "{font=j}{b}夢のステージに立てたら、いつか、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.28-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 40.19:
        $ renpy.pause(0.005, hard=True)

    rose "{font=j}{b}私は思い浮かべるよ。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.39-shorten]}"

    while (renpy.music.get_pos() or 0) < 45.58:
        $ renpy.pause(0.005, hard=True)

    rose "{font=j}{b}あなたの顔を、きっと。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.04-shorten]}"

    scene class
    with dissolve

    hide rose

    show popy at popy_all

    show rose at rose_all

    show halo at halo_all

    show pstl at pstl_all

    while (renpy.music.get_pos() or 0) < 49.62:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}この歌がこの声が大切な想いと繋がる。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.59-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 56.21:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}気がつけば支えられていた。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.09-shorten]}"

    while (renpy.music.get_pos() or 0) < 60.3:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}この歌がこの声が、遠くまで届きますように。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.58-shorten]}"

    while (renpy.music.get_pos() or 0) < 66.88:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}一つ一つ暖かな気持ち。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.38-shorten]}"

    while (renpy.music.get_pos() or 0) < 71.26:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}君の想いが希望になるよ。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.33-shorten]}"

    while (renpy.music.get_pos() or 0) < 76.59:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}夢の先へ Only One Yell。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.95-shorten]}"

    scene class
    with dissolve

    # show narrator at narrator_single

    while (renpy.music.get_pos() or 0) < 83.54:
        $ renpy.pause(0.005, hard=True)

    narrator "{font=j}{b}{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.22-shorten-load_shorten]}"

    scene autumn
    with dissolve

    # hide narrator

    show pstl at pstl_single

    while (renpy.music.get_pos() or 0) < 88.26:
        $ renpy.pause(0.005, hard=True)

    pstl "{font=j}{b}Someday、季節が巡って進んでいくたびに、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.73-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 94.99:
        $ renpy.pause(0.005, hard=True)

    pstl "{font=j}{b}少しずつ変わっていく。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[3.27-shorten]}"

    hide pstl

    show halo at halo_single

    while (renpy.music.get_pos() or 0) < 98.26:
        $ renpy.pause(0.005, hard=True)

    halo "{font=j}{b}夕暮れの空の下で語り合った未来とは違うけど。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[11.29-shorten-load_shorten]}"

    hide halo

    show popy at popy_single

    while (renpy.music.get_pos() or 0) < 109.55:
        $ renpy.pause(0.005, hard=True)

    popy "{font=j}{b}確かなものはそう胸の中に。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.36-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 114.91:
        $ renpy.pause(0.005, hard=True)

    popy "{font=j}{b}優しい温もりを真っ直ぐに、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.35-shorten]}"

    while (renpy.music.get_pos() or 0) < 120.26:
        $ renpy.pause(0.005, hard=True)

    popy "{font=j}{b}あなたへ伝えるよ。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.0-shorten]}"

    scene ground
    with dissolve

    show popy at popy_all

    show rose at rose_all

    show halo at halo_all

    show pstl at pstl_all

    while (renpy.music.get_pos() or 0) < 124.26:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}いくつもの思い出が大切な宝物になる。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.62-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 130.88:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}手を取って積み重ねた日々。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.1-shorten]}"

    while (renpy.music.get_pos() or 0) < 134.98:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}どこまでもどこまでも遠くへと羽ばたけるから。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.56-shorten]}"

    while (renpy.music.get_pos() or 0) < 141.54:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}かけがえない光を信じて。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.41-shorten]}"

    while (renpy.music.get_pos() or 0) < 145.95:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}君と描いた明日へと続く。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.3-shorten]}"

    while (renpy.music.get_pos() or 0) < 151.25:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}夢の先へ Only One Yell。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.35-shorten]}"

    scene night
    with dissolve

    show rose at rose_single

    while (renpy.music.get_pos() or 0) < 157.6:
        $ renpy.pause(0.005, hard=True)

    rose "{font=j}{b}夜空に輝いた幾千の星よりも、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.25-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 162.85:
        $ renpy.pause(0.005, hard=True)

    rose "{font=j}{b}みんなの輝きがずっと。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.37-shorten]}"

    hide rose

    show pstl at pstl_single

    while (renpy.music.get_pos() or 0) < 168.22:
        $ renpy.pause(0.005, hard=True)

    pstl "{font=j}{b}私には何よりもそれが愛おしかった。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.99-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 174.21:
        $ renpy.pause(0.005, hard=True)

    pstl "{font=j}{b}心から「ありがとう」。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.01-shorten]}"

    scene cloud
    with dissolve

    hide pstl

    show popy at popy_double

    show rose at rose_double

    while (renpy.music.get_pos() or 0) < 180.22:
        $ renpy.pause(0.005, hard=True)

    popy_rose "{font=j}{b}まっさらな感情は透明なメロディーに乗って、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.66-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 186.88:
        $ renpy.pause(0.005, hard=True)

    popy_rose "{font=j}{b}響いてく、あの雲を越えて。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.05-shorten]}"

    hide popy

    hide rose

    show halo at halo_double

    show pstl at pstl_double

    while (renpy.music.get_pos() or 0) < 190.93:
        $ renpy.pause(0.005, hard=True)

    halo_pstl "{font=j}{b}特別な今日というこの時に、{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[3.97-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 194.9:
        $ renpy.pause(0.005, hard=True)

    halo_pstl "{font=j}{b}見せられるように溢れ出す笑顔。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.68-shorten]}"

    scene dawn
    with dissolve

    hide halo

    hide pstl

    show popy at popy_all

    show rose at rose_all

    show halo at halo_all

    show pstl at pstl_all

    while (renpy.music.get_pos() or 0) < 201.58:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}この歌がこの声が大切な想いと繋がる。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.69-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 208.27:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}気がつけば支えられていた。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.03-shorten]}"

    while (renpy.music.get_pos() or 0) < 212.3:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}この歌がこの声が、遠くまで届きますように。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.61-shorten]}"

    while (renpy.music.get_pos() or 0) < 218.91:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}一つ一つ暖かな気持ち。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[4.35-shorten]}"

    while (renpy.music.get_pos() or 0) < 223.26:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}君の想いが希望になるよ。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[5.27-shorten]}"

    while (renpy.music.get_pos() or 0) < 228.53:
        $ renpy.pause(0.005, hard=True)

    popy_rose_halo_pstl "{font=j}{b}夢の先へ Only One Yell。{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[6.35-shorten]}"

    scene dawn
    with dissolve

    # show narrator at narrator_single

    while (renpy.music.get_pos() or 0) < 251.58:
        $ renpy.pause(0.005, hard=True)

    narrator "{font=j}{b}{/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=[3.0-shorten-load_shorten]}"

    while (renpy.music.get_pos() or 0) < 261.58000000000004:
        $ renpy.pause(0.005, hard=True)

    # show idle

    idle "{font=j}{b}==idle=={/b}{/font}\n
    {font=z}{/font}\n
    {fast}{nw=10.000}"

    return

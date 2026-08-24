# label start:

label scene_5:
    scene black #sementara
    $ quick_menu = True
    # play music 
    # scene teras penginapan pagi with Dissolve(2.0)
    "Setelah ditinggal oleh Haruto, entah mengapa rasa lelahku kembali, rasanya sangat berat sekali untuk melangkah."
    "Kaki sakit, kepalaku pusing, rasanya seperti aku akan pingsan saat ini juga."
    show yuura normal animated at center
    with Dissolve(1.0)
    y "Ah... Kakiku sudah tak sanggup melangkah, apakah pada akhirnya...apakah aku..."
    
    "Aku berjalan dengan terhuyung-huyung, badanku gemetar, penglihatanku mulai kabur."
    # bgm stop
    hide yuura normal animated with moveoutbottom
    show layer master at shake_custom
    # 
    "Perlahan tubuhku mulai tersungkur tak berdaya, aku melihat seorang sedang berdiri diam di kejauhan."
    "Tanganku berusaha menggapainya, suaraku yang sudah serak berusaha berteriak ke arahnya."
    y "Tolong..."
    show Unknown at center with Dissolve(1.0)
    u "Anee ? ANEEE !?"
    "Orang itu langsung berlari menghampiriku, dengan tangannya yang lembut dia berusaha membangunkanku."
    y "Anee, bangun anee ! Siapa pun tolong ! Anee tidak sadarkan diri !"
    "Mendengar teriakan orang itu, anak penginapan langsung berlari ke arahku, membantu mengangkatku untuk masuk ke dalam penginapan."
    
    $ quick_menu = False

    return
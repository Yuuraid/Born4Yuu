# label start:

label scene_14:

    # BG: show lorong teras penginapan
    # play sound buk
    nd_narrator_brown "Pantatku menghantam tanah duluan."
    
    show yuura scared at right, speaking
    nd_yuura_brown "ADUH..."
    show yuura at idle
    
    show seiya netral at left, silhouette
    nd_unknown_brown "Ane gapapa ?"
    
    nd_narrator_brown "Aku menyadari bahwa ada orang di dekatku, aku segera mundur berapa langkah karena reflek."
    
    nd_narrator_brown "Menyadari bahwa itu adalah Seiya, orang sudah membantuku sebelumnya, aku segera mendekat meski sedikit ragu."
    
    show yuura happy at speaking
    nd_yuura_brown "Seiya !"
    
    nd_yuura_brown "Makasih banget udah nolongin aku dari tendangan itu. Bisa mampus aku kalau bukan karena kamu."
    show yuura at idle
        
    show seiya at speaking
    nd_seiya_brown "Aman aja, Anee. Tapi saranku sekarang kamu lari."
    show seiya at idle
        
    show yuura netral at speaking
    nd_yuura_brown "Kenapa emangnya ?"
    show yuura at idle

    transform movetoright(xalign_pos=0.5, duration=0.5):
        xalign 0.0
        linear 0.15 xalign 0.8
    
    transform slightright(xalign_pos=0.5, duration=0.5):
        xalign 1.0
        linear 0.15 xalign 1.2

    show seiya at speaking
    nd_seiya_brown "Tempat ini sudah tidak aman, sebaik-"
    show seiya at idle
    
    nd_narrator_brown "Belum sempat menyelesaikan bicaranya, Seiya mendengar suara yang sangat keras mengarah padanya."
    
    # Start CG
    show seiya at movetoright
    show yuura at slightright
    nd_narrator_brown "Dia berbalik dan menangkis tendangan mendadak dari pria yang berpakaian serba coklat yang membuat pria itu mundur beberapa langkah, sedangkan lengan Seiya sedikit berasap akibat tendangan tersebut."
    show layer master at shake

    show seiya hurt 
    show akasyah angry at left, speaking
    nd_akasyah_brown "KETEMU LU BANGSAT !"
    show akasyah at idle
        
    show seiya angry at speaking
    nd_seiya_brown "FAHH"
    
    nd_seiya_brown "Apa yang kau coba lakukan !?"
    
    nd_seiya_brown "Apa kau ga capek bikin masalah terus buat Yuura ?"
    show seiya at idle
            
    show akasyah at speaking
    nd_akasyah_brown "MASALAH ??? LU PIKIR APA YANG LU LAKUIN SEKARANG ?"
    
    nd_akasyah_brown "MINGGIR ! JANGAN GANGGU RENCANA GUA !"
    show akasyah at idle
        
    show seiya at speaking
    nd_seiya_brown "Rencana ? Maksudmu dengan mau menghajar Yuura ? APA ITU YANG KAU SEBUT RENCANA !?"
    show seiya at idle
            
    show akasyah at speaking
    nd_akasyah_brown "Mata lu buta apa gimana ?"
    
    nd_akasyah_brown "Apa emang lu gabisa bedain Yuura yang asli sama yang palsu ?"
    show akasyah at idle
        
    show seiya at speaking
    nd_seiya_brown "Apa sih maksudmu ? Apa kamu kebanyakan minum sake siang-siang ?"
    show seiya at idle
    
    nd_narrator_brown "Akasyah melempar sebuah linting."
            
    show akasyah at speaking
    nd_akasyah_brown "OI YUUR ! Lu tau ga benda apa ini ?"
    show akasyah at idle
    
    nd_narrator_brown "Aku kaget melihat benda yang dia lempar, aku tidak mengerti untuk apa benda itu dan mengapa dia menanyakan padaku."
            
    show akasyah at speaking
    nd_akasyah_brown "Kok diem ? Jawab bangsat !"
    show akasyah at idle
        
    show yuura at speaking
    nd_yuura_brown "Ah...um...ituu..."
    
    nd_yuura_brown "(ARGH SIAL, aku gatau linting apaan ! Lagian sejak kapan aku punya uang untuk melakukan kebiasaan yang sama seperti orang-orang kaya !)"
    show yuura at idle
        
    show akasyah at speaking
    nd_akasyah_brown "Hahaha... Udah gua duga lu pasti gabisa jawab pertanyaan gua."
    
    nd_akasyah_brown "Sekarang minggir dan biar gua hajar si palsu ini !"
    show akasyah at idle
    
    nd_narrator_brown "Aku melihat senyum lebar di wajah Akasyah yang berhasil mengungkap fakta yang selama ini kututupi. Badanku gemetar karena merasa takut bahwa aku tidak akan bisa jekuar dari sini hidup-hidup, aku menoleh ke arah Seiya dan mulai melihat raut wajah ragu padanya."
    
    nd_narrator_brown "Meski begitu, ia langsung menyiapkan kuda-kuda untuk menyerang, tetap inign melindungiku."
            
    show akasyah at speaking
    nd_akasyah_brown "Lu goblok apa gimana ?"
    
    nd_akasyah_brown "Masih mau ngelindungin si peniru sialan ini ? Seiya Seiya..."
    show akasyah at idle
        
    show seiya at speaking
    nd_seiya_brown "Mau palsu atau bukan, itu bukan urusanmu !"
    show seiya at idle
            
    show akasyah at speaking
    nd_akasyah_brown "Oh jelas... {w}ITU URUSAN GUA !!!"
    show akasyah at idle
    
    # Use CG here
    nd_narrator_brown "Dalam sekejap, Akasyah berpindah dan memberikan serangan akurat kepada Seiya. Seiya berhasil memprediksi serangan itu dan menangkisnya dengan tangan yang sudah diselimuti oleh bayangan hitam."
    
    nd_narrator_brown "Tak berhenti di sana, Akasyah mulai menghantam Seiya dengan tinju dan tendangan yang berulang. Tak tinggal diam, Seita melancarkan serangan berupa sihir proyektil yang mengarah ke Akasyah."
    
    nd_narrator_brown "Akasyah sesekali menepis serangan itu sebelum akhirnya mundur beberapa langkah untuk menghindar. Tak melewatkan kesempatan, Seiya muncul dari portal bayangan dan melayangkan tinjunya."
    
    nd_narrator_brown "Sayangnya, Akasyah berpindah dan memberikan tendangan telak ke belakang Seiya. Meski terpental, Seiya berhasil mengikat kaki Akasyah dan memanfaatkan momentum untuk menarik kakinya dan membantingkan tubuhnya ke lantai."
    
    # play sound lantai kayu patah
    nd_narrator_brown "Seiya berhasil memberikan serangan telak, tapi nampaknya itu tak terlalu berefek karena ketika kepulan debu memudar, terlihat Akasyah yang berdiri dengan darah yang mengalir dari mulutnya."
            
    show akasyah at speaking
    nd_akasyah_brown "Segitu doang serangan lu ? GUA JUGA BISA !"
    show akasyah at idle
    
    # Another CG?
    nd_narrator_brown "Baru menutup bicaranya, Seiya muncul dari portal bayangan dan melancarkan tinju yang diselimuti energi hitam. Akasyah yang sudah memprediksi serangannya langsung menahan serangan Seiya. Akasyah menyeringai membuat Seiya mundur karena merasakan sesuatu yang salah pada Akasyah."
            
    show akasyah at speaking
    nd_akasyah_brown "Udah puas ? Now, it's my turn..."
    show akasyah at idle
    
    nd_narrator_brown "Akasyah berpindah dan melancarkan serangan pada Seiya, berpindah dan menyerang secara berulang. Seiya lumayan dapat mengikuti alur pertarungan. Namun, nampaknya itu memang rencananya Akasyah supaya Seiya terpancing dalam jebakannya."
    
    nd_narrator_brown "Akasyah menendang kaki Seiya."
        
    show seiya at speaking
    nd_seiya_brown "Urghhh !!!"
    show seiya at idle
    
    nd_narrator_brown "Seiya kehilangan keseimbangannya karena tak menyadari serangan dadakan itu dan Akasyah segera memanfaatkan kesempatan itu."
    
    nd_narrator_brown "Akasyah berpindah dan melancarkan tinju ke ulu hati Seiya yang membuatnya tersentak. Tak berhenti, Akasyah menendang ulu hati Seiya dengan lututnya dan menendang Seiya ke atas."
    
    nd_narrator_brown "Seiya belum sempat berkutik, sedangkan Akasyah berpindah ke atasnya dan menendang Seiya ke bawah."
    
        # play sound lantai kayu patah
    show seiya at speaking
    nd_seiya_brown "Lu pikir serangan lemah kayak gitu bisa menghentikan gua ? Seiya Seiya..."
    
    nd_seiya_brown "SEKARANG LAH AKHIRNYA ! SELAMAT TINGGAL PAHLAWAN KESIANGAN !"
    show seiya at idle
    
    nd_narrator_brown "Akasyah yang sedari tadi melayang di udara mengangkat satu kakinya tinggi-tinggi dan berpindah tepat di tempat jatuh Seiya, melancarkan serangan."
    
        # play sound serangan lilitan
    nd_narrator_brown "Energi hitam melilit kaki Akasyah yang membuatnya terpaksa terhenti. Disaat kepulan debu mulai memudar, Seiya muncul dalam keadaan terduduk dengan posisi tangan sedang mengikat suatu. Kondisinya buruk, mungkin karena sempat menghantam lantai kayu yang langsung mengenai tubuhnya."
        
    show seiya at speaking
    nd_seiya_brown "Ha... Hah.. Hah" # kasih jeda
    show seiya at idle
            
    show akasyah at speaking
    nd_akasyah_brown "Kau pikir bisa menghentikanku hanya dengan mengikat kakiku ?"
    
    nd_akasyah_brown "DITYO !!" # shake
    show akasyah at idle
    
    nd_narrator_brown "Seiya tak menyadari bahwa Dityo telah tiba dan segera menembakkan serangan proyektil tepat ke arahku."
        
    show seiya at speaking
    nd_seiya_brown "SIALAN ! ANEEEE !!!!"
    show seiya at idle
        
    show yuura at speaking
    nd_yuura_brown "*Menutup mata"
    
        # show black with Dissolve(1.0)
        # play sound gigit roket
    nd_yuura_brown "!!" # improvisasi? Wkwkwkwk hapus aja kalo ga butuh
    
    nd_yuura_brown "*Membuka mata"
    show yuura at idle

    # show lorong teras penginapan with Dissolve(1.0)
    nd_narrator_brown "Aku terkejut mendapati Shark yang tiba-tiba berda di depanku, sembari menahan alat Dityo dengan giginya."
    
    show shark at speaking
    nd_shark_brown "Aw... Aw... sakit juga nahan rudal pake gigi."
    show shark at idle
    
    # This two suppose to speak the same time
        
    show yuura at speaking    
    show seiya at speaking
    nd_yuura_brown "Shark !"
    nd_seiya_brown "Shark !"
    show yuura at idle
    show seiya at idle

    show shark at speaking
    nd_shark_brown "Ah... Anu... Maaf membuat kalian menunggu."
    show shark at idle
    
    nd_narrator_brown "Kini situasi imbang, dua lawan dua. Meski begitu, melihat dari raut wajah Seiya, aku tahu bahwa perkara ini belum usai."
        
    show seiya at speaking
    nd_seiya_brown "Aneki, pergilah !"
    show seiya at idle
        
    show yuura at speaking
    nd_yuura_brown "T-tapi..."
    show yuura at idle
    
    show seiya at speaking
    nd_seiya_brown "Serahkan urusan ini padaku dan Shark !"
    show seiya at idle
    
    nd_narrator_brown "Meski enggan, aku berbalik dan lari meninggalkan mereka berdua."
        
    show akasyah at speaking
    nd_akasyah_brown "WOI MAU KE MANA LU NENEK TUA !"
    show akasyah at idle
    
    nd_narrator_brown "Akasyah berusaha menyerangku tapi Seiya langsung menghentikan gerakannya dengan bayangannya."
        
    show seiya at speaking
    nd_seiya_brown "Lawanmu adalah aku."
    show seiya at idle

    return


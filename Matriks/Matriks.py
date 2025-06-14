from manim import *


class matriks(Scene):
    def construct(self):
        
        # setup teks sama nilai
        judul = Text("Matriks").scale(.8).shift(UP*3)
        subjudul = Tex("Penjumlahan dan \\\\" \
            "Pengurangan Matriks").next_to(judul, DOWN).scale(.6)
        variable = MathTex("A=").shift(LEFT*1.6)
        matriks = Matrix([[1, 2], [3, 4]], h_buff=1.5)
        matriks1 = Matrix([[1, 2], [3, 4]], h_buff=.85).next_to(variable, RIGHT)
        matriks1.move_to(matriks)
        a = VGroup(variable, matriks1)
        a.scale(.6)

        # Munculin nilai A
        self.play(Write(judul), Write(subjudul), run_time=.5)
        self.play(Write(matriks), ReplacementTransform(matriks, matriks1), Write(variable), 
                  rate_func=rate_functions.ease_out_quart)
        self.wait(.5)

        # setup nilai B, dan ganti posisi A
        var2 = MathTex("B=").next_to(a).shift(LEFT*1.1)
        matriks2 = Matrix([[5, 6], [7, 8]], h_buff=.85).next_to(var2, RIGHT)
        b = VGroup(var2, matriks2)
        b.scale(.6)
        pos1 = LEFT*1.3 # ganti posisi A

        # munculin nilai B, dan gerakin posisi nilai A
        self.play(FadeIn(matriks2, shift=LEFT), a.animate.move_to(pos1), FadeIn(var2, shift=LEFT), run_time=.8)
        self.wait(.3)

        # setup Output matriks (jumlah), dan ubah subjudul
        mentah = VGroup(a, b)
        posmentah = (UP *.2) + LEFT*.2
        jumlah = MathTex("A+B= ?").next_to(mentah, DOWN*1.2)
        subjudul2 = Tex("Penjumlahan Matriks").next_to(judul, DOWN).scale(.6)

        # tampilkan perubahan pada Output matriks, dan mengganti subjudul
        self.play(FadeIn(jumlah, shift=UP), ReplacementTransform(subjudul, subjudul2), 
                  mentah.animate.move_to(posmentah), run_time=.5)
        
        self.wait()
        
        # setup output matriks beserta box
        targetbox1 = matriks1.get_entries()[0]
        targetbox2 = matriks2.get_entries()[0]
        box = SurroundingRectangle(targetbox1).set_color(BLUE)
        box2 = SurroundingRectangle(targetbox2).set_color(BLUE)
        jumlah2 = MathTex("A + B = \\left[\\begin{array}{cc}"
                            "1+5"
                        "\\end{array}\\right]").next_to(mentah, DOWN*1.2).scale(.65)
        jumlah2[0][5:8].set_color(BLUE_B) # setup warna
        # A = 0
        # + = 1
        # B = 2
        # = = 3
        

        # munculkan box, dan ubah text jumlah
        self.play(Write(box), Write(box2), ReplacementTransform(jumlah, jumlah2))
        self.wait(.5)

        # tambahin 2+6 di jumlah
        jumlah21 = MathTex("A + B = \\left[\\begin{array}{c@{\\hspace{0.5cm}}c}"
                            "1+5 & 2+6"
                        "\\end{array}\\right]").next_to(mentah, DOWN*1.2).scale(.65)
        
        # setup warna
        jumlah21[0][5:8].set_color(BLUE_B)
        jumlah21[0][8:11].set_color(GREEN_B)

        # ubah posisi box ke 2 & 6
        targetbox3 = matriks1.get_entries()[1]
        targetbox4 = matriks2.get_entries()[1]
        box3 = SurroundingRectangle(targetbox3).set_color(GREEN)
        box4 = SurroundingRectangle(targetbox4).set_color(GREEN)

        # munculkan 2 & 6
        self.play(ReplacementTransform(box, box3), ReplacementTransform(box2, box4), 
                  ReplacementTransform(jumlah2, jumlah21))
        self.wait(.3)

        # tambahkan 3 & 7
        jumlah22 = MathTex("A + B = \\left[\\begin{array}{c@{\\hspace{0.5cm}}c}"
                            "1+5 & 2+6 \\\\"
                            "\\rule{0pt}{1.2em} 3+7"
                        "\\end{array}\\right]").next_to(mentah, DOWN*1.2).scale(.65)
        
        # setup warna
        jumlah22[0][5:8].set_color(BLUE_B)
        jumlah22[0][8:11].set_color(GREEN_B)
        jumlah22[0][11:14].set_color(RED_B)

        # ubah posisi box ke 3 & 7
        targetbox3 = matriks1.get_entries()[2]
        targetbox4 = matriks2.get_entries()[2]
        box5 = SurroundingRectangle(targetbox3).set_color(RED)
        box6 = SurroundingRectangle(targetbox4).set_color(RED)

        # munculkan 3 & 7
        self.play(ReplacementTransform(box3, box5), ReplacementTransform(box4, box6), 
                  ReplacementTransform(jumlah21, jumlah22))
        
        self.wait(.4)

        # menambahkan 4 & 8
        jumlah23 = MathTex("A + B = \\left[\\begin{array}{c@{\\hspace{0.5cm}}c}"
                            "1+5 & 2+6 \\\\"
                            "\\rule{0pt}{1.2em} 3+7 & 4+8"
                        "\\end{array}\\right]").next_to(mentah, DOWN*1.2).scale(.65)
        
        # setup warna
        jumlah23[0][5:8].set_color(BLUE_B)
        jumlah23[0][8:11].set_color(GREEN_B)
        jumlah23[0][11:14].set_color(RED_B)
        jumlah23[0][14:17].set_color(YELLOW_B)

        # ubah posisi box ke 4 & 8
        targetbox5 = matriks1.get_entries()[3]
        targetbox6 = matriks2.get_entries()[3]
        box7 = SurroundingRectangle(targetbox5).set_color(YELLOW_C)
        box8 = SurroundingRectangle(targetbox6).set_color(YELLOW_C)

        # munculkan 4 & 8
        self.play(ReplacementTransform(box5, box7), ReplacementTransform(box6, box8), 
                  ReplacementTransform(jumlah22, jumlah23))
        
        self.wait()

        # setup buat memunculkan kembali semua kotak
        targetbox1 = matriks1.get_entries()[0]
        targetbox2 = matriks2.get_entries()[0]
        boxd = SurroundingRectangle(targetbox1).set_color(BLUE)
        boxd2 = SurroundingRectangle(targetbox2).set_color(BLUE)

        # munculkan semua kotak
        self.play(Write(box), Write(box2), 
                  Write(boxd), Write(boxd2),
                  Write(box3), Write(box4), 
                  Write(box5), Write(box6), 
                  lag_ratio = 1)
        self.wait()

        # menjumlahkan semua angka
        jumlah24 = MathTex("A + B = \\left[\\begin{array}{c@{\\hspace{0.5cm}}c}"
                            "6 & 8 \\\\"
                            "\\rule{0pt}{1.2em} 10 & 12"
                        "\\end{array}\\right]").next_to(mentah, DOWN*1.2).scale(.65)
        
        # setup warna (dan posisi text)
        jumlah24[0][5:6].set_color(BLUE_B)
        jumlah24[0][6:7].set_color(GREEN_B)
        jumlah24[0][7:9].set_color(RED_B)
        jumlah24[0][9:11].set_color(YELLOW_B)

        # munculkan hasil
        self.play(ReplacementTransform(jumlah23, jumlah24))

        self.wait()
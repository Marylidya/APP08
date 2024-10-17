import flet as ft


def main(page: ft.Page):
#establecer tamaño de pantalla

    page.window_width=800
    page.window_height=800
    
    page.bgcolor="black"
    page.title="Mictlan"
    page.fgcolor="gray"
    
    Intro=ft.Audio(src="Intro.mp3",volume=1,balance=0)
    page.overlay.append(Intro)
    
    PrimerNivel=ft.Audio(src="Primer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(PrimerNivel)
    
    SegundoNivel=ft.Audio(src="Segundo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SegundoNivel)
    
    TercerNivel=ft.Audio(src="Tercer_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(TercerNivel)
    
    CuartoNivel=ft.Audio(src="Cuarto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(CuartoNivel)
    
    QuintoNivel=ft.Audio(src="Quinto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(QuintoNivel)
    
    SextoNivel=ft.Audio(src="Sexto_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SextoNivel)
    
    SeptimoNivel=ft.Audio(src="Septimo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(SeptimoNivel)
    
    OctavoNivel=ft.Audio(src="Octavo_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(OctavoNivel)
    
    NovenoNivel=ft.Audio(src="Noveno_Nivel.mp3",volume=1,balance=0)
    page.overlay.append(NovenoNivel)
    
#se crea la interfaz
    btnIntro=ft.FilledButton(text="Escucha la intro",disabled=False)
    
    btnNivel1=ft.FilledButton(text="Primer-Nivel")
    img1=ft.Image(src="Primer-Nivel.jpng",width=150,height=1500)
    
    btnNivel2=ft.FilledButton(text="Segundo-Nivel")
    img1=ft.Image(src="Segundo-Nivel.jpng",width=150,height=150)
    
    btnNivel3=ft.FilledButton(text="Tercer-Nivel")
    img1=ft.Image(src="Tercer Nivel.png",width=150,height=150)
    
    btnNivel4=ft.FilledButton(text="Cuarto-Nivel")
    img1=ft.Image(src="Cuarto Nivel.jpng",width=150,height=150)
    
    btnNivel5=ft.FilledButton(text="Quinto-Nivel")
    img1=ft.Image(src="Quinto Nivel.jpng",width=150,height=150)
    
    btnNivel6=ft.FilledButton(text="Sexto-Nivel")
    img1=ft.Image(src="Sexto Nivel.jpng",width=150,height=150)
    
    btnNivel7=ft.FilledButton(text="Septimo-Nivel")
    img1=ft.Image(src="Septimo Nivel.jpng",width=150,height=150)
    
    btnNivel8=ft.FilledButton(text="Octavo-Nivel")
    img1=ft.Image(src="Octavo Nivel.png",width=150,height=150)
    
    btnNivel9=ft.FilledButton(text="Noveno-Nivel")
    img1=ft.Image(src="Noveno Nivel.jpng",width=150,height=150)
    
    page.add(
        ft.Row(
            alignment="start",
            controls=[btnIntro]
        ),
        ft.Column(
            aligment="CENTER"
            spacing=10,
            scroll=ft.ScrollMode.AUTO,
            controls=[
                ft.Row(
                    alignment="CENTER"
                    controls=[btnNivel1,img1]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel2,img2]
                ),
                ft.Column(
                    alignment="CENTER",
                    controls=[btnNivel3,img3]
                
ft.app(main)

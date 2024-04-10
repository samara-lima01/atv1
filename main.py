class TV:
    def __init__(self):
        self.ligada = False
        self.canal_atual = 0
        self.volume = 50
        self.lista_de_canais = list(range(10))  # Lista de canais de 0 a 9
        self.mudo = False 

    def ligar(self):
        if not self.ligada:
            print("A TV está ligada.")
            self.ligada = True
        else:
            print("A TV já está ligada.")

    def desligar(self):
        if self.ligada:
            print("A TV está desligada.")
            self.ligada = False
        else:
            print("A TV já está desligada.")

    def mudar_canal(self, novo_canal):
        if self.ligada:
            if novo_canal in self.lista_de_canais:
                self.canal_atual = novo_canal
                print("Canal alterado para", novo_canal)
            else:
                print("Canal inválido.")
        else:
            print("A TV está desligada. Ligue-a primeiro.")

    def aumentar_volume(self):
        if self.ligada and self.volume < 100:
            self.volume += 1
            print("Volume aumentado para", self.volume)
        elif self.ligada and self.volume == 100:
            print("Volume já está no máximo.")
        else:
            print("A TV está desligada. Ligue-a primeiro.")

    def diminuir_volume(self):
        if self.ligada and self.volume > 0:
            self.volume -= 1
            print("Volume diminuído para", self.volume)
        elif self.ligada and self.volume == 0:
            print("Volume já está no mínimo.")
        else:
            print("A TV está desligada. Ligue-a primeiro.")
    
    def alternar_mudo(self):  
        if self.ligada:
            self.mudo = not self.mudo
            if self.mudo:
                print("Mudo ativado.")
            else:
                print("Mudo desativado.")
        else:
            print("A TV está desligada. Ligue-a primeiro.")



tv = TV()
tv.ligar()
tv.mudar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.alternar_mudo() 
tv.aumentar_volume()  
tv.diminuir_volume()
tv.mudar_canal(10)  
tv.desligar()

#!/usr/bin/env python3.7
import sys, os, time

def spam(name, count, i):
    cmd = ""
    base = "airbase-ng -a AA:AA:AA:AA:AA:[X][Y] --essid '[NOME]' -c 1 " + i + " &\n"
    x = 0
    y = 0
    
    for i in range(count):
        if y > 9:
            y = 0
            x += 1

        print("Criando ponto de acesso: " + name)
        print("BSSID: AA:AA:AA:AA:AA:" + str(x) + str(y))
        print()
        cmd += base.replace("[X]", str(x)).replace("[Y]", str(y)).replace("[NOME]", name + (" "*i))
        y += 1
    cmd += "echo a\n"
    print("Agora ele vai travar, mas já está funcionando ok kkkkk")
    os.popen(cmd).read()

def stop_spamming(monitor):
    managed = monitor.replace("mon", "")
    print("airmon-ng stop " + monitor)
    print("airmon-ng start " + managed)
    os.popen("airmon-ng stop "+ monitor).read()
    os.popen("airmon-ng start "+ managed).read()
    
def banner():
    print("""
     __        ___  __ _   ____                                            
     \ \      / (_)/ _(_) / ___| _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
      \ \ /\ / /| | |_| | \___ \| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
       \ V  V / | |  _| |  ___) | |_) | (_| | | | | | | | | | | |  __/ |   
        \_/\_/  |_|_| |_| |____/| .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                |_|
    """)
    print("Programa para spammar pontos de Wi-Fi com o \"mesmo\" nome só pelo lulz.\n")
    print("Desenvolvido por Igor Costa Melo <igoracm@outlook.com>\n\n\n")


def close():
    print("\n\n\n\nEncerrando programa... Beijo no coração <3")
    exit()

def instructions():
    print("""
    Instruções de uso:
    -name = nome do wi-fi, ESSID
        exemplo: -name "Bom dia, vizinhos"
    -count = quantidade de wi-fis que irá criar com esse nome
        exemplo: -count 10
        irá gerar 10 pontos de acesso
    -i = interface, que deve destar em modo de monitoramento
        exemplo: -i wlan0mon
    """)


    
def main():
    banner()
    time.sleep(3)
    
    args = sys.argv
    name = ""
    count = 0
    interface = ""
    
    try:
        """stopi = args[args.index("-stop") + 1]
        if stopi:
            stop_spamming(stopi)
            close()
        else:"""
        name = args[args.index("-name") + 1]
        count = int(args[args.index("-count") + 1])
        interface = args[args.index("-i") + 1]
        
    except:
        sumargs = ""
        for a in args:
            sumargs += a

        print('"'+sumargs+'"')
        print("Erro: argumento inválido ou incompleto.")
        print()
        instructions()
        exit()

    if count > 100:
        print("Erro: tamanho supera limite de 100 pontos de acesso [count].")
        exit()
    spam(name, count, interface)
    time.sleep(1)

    print("\n\nTudo certo. Você pode ver o resultado usando o comando \"sudo airodump-ng " + interface + "\"")
    print("\nAgora escolha uma opção")
    
    """while True:
        print("1) Fechar programa e manter SPAM")
        print("2) Fechar programa e parar SPAM")
        resp = input("\n: ")

        if resp == "1":
            close()
        elif resp == "2":
            stop_spamming(interface)
            close()"""

            
if __name__ == "__main__":
    main()

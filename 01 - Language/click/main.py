import click
import os
os.system("cls")

msg1 = "Your name please"
msg2 = "Limpar tela"
msg3 = "Exibir relatorio sintetico"
msg4 = "Exibir relatorio analitico"
help = "Ask something"

@click.command()
@click.option('--recon', prompt=f"{msg1}", help=f"help", default="config.cfg")
@click.option('--c',     prompt=f"{msg2}", help=f"help", default=1)
@click.option('--rs',    prompt=f"{msg3}", help=f"help", default=0)
@click.option('--ra',    prompt=f"{msg4}", help=f"help", default=12)

def main(recon, c, rs, ra):
    print("Recon Name: ", recon)
    print("Limpar tela: ", recon)
    print("relatorio sintetico: ", rs)
    print("relatorio analitico: ", ra)
    
if __name__ == '__main__':
    main()
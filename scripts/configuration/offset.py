import ivtools
import multiprocessing
from time import sleep
from tqdm import tqdm

def configure(ep):
    interface = ivtools.interface(f'10.73.137.{ep}')
    print(f'Configuring Offset in 40 ch DAPHNE {ep} ')
    interface.command( f'CFG AFE ALL INITIAL')
    for ch in tqdm(range(40),unit='Channels'):
        interface.command(f'WR OFFSET CH {ch} V {(ch%8)*50+200+250*ch//8}')
        interface.command(f'CFG OFFSET CH {ch} GAIN 2')

    print(f'Configuring AFE registers 4, 51, 52 and Attenuators')
    for AFE in tqdm(range(5),unit='AFE'):
        interface.command(f'WR AFE {AFE} REG 52 V 21056')
        interface.command(f'WR AFE {AFE} REG 4 V 24')
        interface.command(f'WR AFE {AFE} REG 51 V 16')
        interface.command(f'WR AFE {AFE} VGAIN V 2667')
        alignment=[interface.write_reg(0x2001,[1234]) for _ in range (3)]
    print('Finished writing commands.')
    interface.close()




def main():
    #a=configure(104)
    #b=configure(105)
    #c=configure(107)
    #d=configure(109)
    #e=configure(111)
    #f=configure(112)
    g=configure(113)
if __name__ == "__main__":
    main()


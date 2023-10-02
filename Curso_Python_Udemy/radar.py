velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1 

vel_carro_pass_radar_1 = velocidade > RADAR_1

if vel_carro_pass_radar_1: 
    print('Velocidade excedida!')

#Barra invertidade quebra linha; 
if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1: 
    print('Carro multado em radar 1!')   

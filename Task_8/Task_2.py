import re

def parse_cgminer_stats(stats_string):
    # Используем регулярное выражение для поиска пар ключ-значение
    pattern = re.compile(r'(\w+)\[([^\]]*)\]|(\w+)=([^,|]+)')

    # Находим все совпадения в строке
    matches = pattern.findall(stats_string)

    # Создаем словарь для хранения результатов
    result = {}

    # Обрабатываем совпадения
    for match in matches:
        key1, value1, key2, value2 = match
        key = key1 if key1 else key2
        value = value1 if value1 else value2
        result[key] = value

    return result

# Пример использования
stats_string = "STATS=0,ID=AVA100,Elapsed=6979,Calls=0,Wait=0.000000,Max=0.000000,Min=99999999.000000,MM ID0=Ver[1126Pro-S-64-21072803_4ec6bb0_211fc46] DNA[0201000074a3f9e8] MEMFREE[1298896.0] NETFAIL[206 216 216 226 1943 1954 195 205] SYSTEMSTATU[Work: In Work, Hash Board: 2 ] Elapsed[7031] BOOTBY[0x0A.00000002] LW[6936143] MH[64 42] HW[106] DH[9.509%] Temp[29] TMax[83] TAvg[70] Fan1[6439] Fan2[6358] Fan3[6334] Fan4[0] FanR[88%] Vo[334] PS[0 1220 1339 239 3200 1340 3522] PLL0[8718 493 695 4014] PLL1[7206 1115 1567 4032] GHSspd[66559.56] DHspd[9.381%] GHSmm[73691.12] GHSavg[65410.21] WU[913770.14] Freq[661.74] Led[0] MGHS[31633.72 33776.49] MTmax[83 80] MTavg[72 69] TA[240] Core[A3201] PING[108] POWS[0] HASHS[0 0] POOLS[0] SoftOFF[0] ECHU[0 0] ECMM[4] SF0[640 660 680 700] SF1[640 660 680 700]"

result_dict = parse_cgminer_stats(stats_string)

# Выводим результат
for key, value in result_dict.items():
    print(f"{key}: {value}")


import argparse
import sys
import time
import minimalmodbus

# Define CLI Default paramater
METER_SERIALPORT = "/dev/ttyUSB0"
METER_MODBUSADDRESS = 1
METER_MODEL="SDM630"
OUTPUTFORMAT = "cli"
MEASUREMENT = "SDMTEST"
SLEEP = 0
BAUDRATE = 38400

def helpmessage():
    print('Options:')
    print('-d --device [Devicepath], Path to serial device. Default: ' + METER_SERIALPORT)
    print('-a --address [Modbusaddress], Modbusaddresss for the device. Default: ' + str(METER_MODBUSADDRESS))
    print('-m --model [Devicemodell], Default: ' + METER_MODEL)
    print('           aviable models: SDM630, SDM230, SDM220, SDMsimple')
    print('-o --output [outputformat], Default: ' + OUTPUTFORMAT)
    print('           aviable output formats: cli, influxlineprotocol')
    print('-t --measurement [measurement], Default: ' + MEASUREMENT)
    print('-s --sleep [sleeptime in seconds], Default: ' + str(SLEEP))
    print('-b --baudrate [baudrate], Default: ' + str(BAUDRATE))
    print()

def show_connection_parameters():
    print("used connection parameters:")
    print("Serial device: " + args.device)
    print("Serial baudrate: " + str(args.baudrate))
    print("Modbusaddress: " + str(args.address))
    print("Model: " + args.model)
    print("Outputformat: " + args.output)
    print("Measurement: " + args.measurement)

# Define Registersets for the different Models
def get_sdm_register(sdm_model="SDM630"):
    if sdm_model == "SDMsimple":
            sdm_register = {
                "U": {"port": 0, "digits": 2, "Unit": "V", "use": True},
                "I": {"port": 6, "digits": 2, "Unit": "A", "use": True},
                "P": {"port": 12, "digits": 2, "Unit": "W", "use": True},
                "Ps": {"port": 18, "digits": 2, "Unit": "VA", "use": True},
                "Pr": {"port": 24, "digits": 2, "Unit": "VAr", "use": True},
                "Leistungsfaktor": {"port": 30, "digits": 2, "Unit": "", "use": True},
                "Phasenwinkel": {"port": 36, "digits": 2, "Unit": "Grad", "use": True},
                "freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
                "P_import": {"port": 72, "digits": 2, "Unit": "kWh", "use": True},
                "P_export": {"port": 74, "digits": 2, "Unit": "kWh", "use": True},
                "Pr_import": {"port": 76, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_export": {"port": 78, "digits": 2, "Unit": "kVArh", "use": True},
                "P_sum": {"port": 342, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_sum": {"port": 344, "digits": 2, "Unit": "kVArh", "use": True},
            }

    elif sdm_model == "SDM220":
            sdm_register = {
                "U": {"port": 0, "digits": 2, "Unit": "V", "use": True},
                "I": {"port": 6, "digits": 2, "Unit": "A", "use": True},
                "P": {"port": 12, "digits": 2, "Unit": "W", "use": True},
                "Ps": {"port": 18, "digits": 2, "Unit": "VA", "use": True},
                "Pr": {"port": 24, "digits": 2, "Unit": "VAr", "use": True},
                "Leistungsfaktor": {"port": 30, "digits": 2, "Unit": "", "use": True},
                "Phasenwinkel": {"port": 36, "digits": 2, "Unit": "Grad", "use": True},
                "freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
                "P_import": {"port": 72, "digits": 2, "Unit": "kWh", "use": True},
                "P_export": {"port": 74, "digits": 2, "Unit": "kWh", "use": True},
                "Pr_import": {"port": 76, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_export": {"port": 78, "digits": 2, "Unit": "kVArh", "use": True},
                "P_sum": {"port": 342, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_sum": {"port": 344, "digits": 2, "Unit": "kVArh", "use": True},
            }

    elif sdm_model == "SDM230":
            sdm_register = {
                "U": {"port": 0, "digits": 2, "Unit": "V", "use": True},
                "I": {"port": 6, "digits": 2, "Unit": "A", "use": True},
                "P": {"port": 12, "digits": 2, "Unit": "W", "use": True},
                "Ps": {"port": 18, "digits": 2, "Unit": "VA", "use": True},
                "Pr": {"port": 24, "digits": 2, "Unit": "VAr", "use": True},
                "Leistungsfaktor": {"port": 30, "digits": 2, "Unit": "", "use": True},
                "Phasenwinkel": {"port": 36, "digits": 2, "Unit": "Grad", "use": True},
                "freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
                "P_import": {"port": 72, "digits": 2, "Unit": "kWh", "use": True},
                "P_export": {"port": 74, "digits": 2, "Unit": "kWh", "use": True},
                "Pr_import": {"port": 76, "digits": 2, "Unit": "kVArh", "use": True},
                "Pr_export": {"port": 78, "digits": 2, "Unit": "kVArh", "use": True},
                "P_tot_sys": {"port": 84, "digits": 2, "Unit": "W", "use": True},
                "P_max_tot_sys": {"port": 86, "digits": 2, "Unit": "W", "use": True},
                "P_current_sys": {"port": 88, "digits": 2, "Unit": "W", "use": True},
                "P_max_sys": {"port": 90, "digits": 2, "Unit": "W", "use": True},
                "P_current_sys_rev": {"port": 92, "digits": 2, "Unit": "W", "use": True},
                "P_max_sys_rev": {"port": 94, "digits": 2, "Unit": "W", "use": True},
                "I_current": {"port": 258, "digits": 2, "Unit": "A", "use": True},
                "I_max": {"port": 264, "digits": 2, "Unit": "A", "use": True},
                "P_tot": {"port": 342, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_tot": {"port": 344, "digits": 2, "Unit": "kVArh", "use": True},
                "P_sum": {"port": 384, "digits": 2, "Unit": "kVAh", "use": True},
                "Pr_sum": {"port": 386, "digits": 2, "Unit": "kVArh", "use": True},
            }

    elif sdm_model == "SDM630":
            sdm_register = {
                "U_L1": {"port": 0, "digits": 2, "Unit": "V", "use": True},
                "U_L2": {"port": 2, "digits": 2, "Unit": "V", "use": True},
                "U_L3": {"port": 4, "digits": 2, "Unit": "V", "use": True},
                "I_L1": {"port": 6, "digits": 2, "Unit": "A", "use": True},
                "I_L2": {"port": 8, "digits": 2, "Unit": "A", "use": True},
                "I_L3": {"port": 10, "digits": 2, "Unit": "A", "use": True},
                "P_L1": {"port": 12, "digits": 2, "Unit": "W", "use": True},
                "P_L2": {"port": 14, "digits": 2, "Unit": "W", "use": True},
                "P_L3": {"port": 16, "digits": 2, "Unit": "W", "use": True},
                "Ps_L1": {"port": 18, "digits": 2, "Unit": "VA", "use": True},
                "Ps_L2": {"port": 20, "digits": 2, "Unit": "VA", "use": True},
                "Ps_L3": {"port": 22, "digits": 2, "Unit": "VA", "use": True},
                "Pr_L1": {"port": 24, "digits": 2, "Unit": "VAr", "use": True},
                "Pr_L2": {"port": 26, "digits": 2, "Unit": "VAr", "use": True},
                "Pr_L3": {"port": 28, "digits": 2, "Unit": "VAr", "use": True},
                "Leistungsfaktor_L1": {"port": 30, "digits": 2, "Unit": "", "use": True},
                "Leistungsfaktor_L2": {"port": 32, "digits": 2, "Unit": "", "use": True},
                "Leistungsfaktor_L3": {"port": 34, "digits": 2, "Unit": "", "use": True},
                "Phasenwinkel_L1": {"port": 36, "digits": 2, "Unit": "Grad", "use": True},
                "Phasenwinkel_L2": {"port": 38, "digits": 2, "Unit": "Grad", "use": True},
                "Phasenwinkel_L3": {"port": 40, "digits": 2, "Unit": "Grad", "use": True},
                "U_avg": {"port": 42, "digits": 2, "Unit": "V", "use": True},
                "I_avg": {"port": 46, "digits": 2, "Unit": "A", "use": True},
                "I_sum": {"port": 48, "digits": 2, "Unit": "A", "use": True},
                "aktuelle_Gesamtwirkleistung": {"port": 52, "digits": 2, "Unit": "W", "use": True},
                "Ps_sum": {"port": 56, "digits": 2, "Unit": "VA", "use": True},
                "Pr_sum": {"port": 60, "digits": 2, "Unit": "VAr", "use": True},
                "Lfakt_sum": {"port": 62, "digits": 2, "Unit": "", "use": True},
                "Pwin_sum": {"port": 66, "digits": 2, "Unit": "A", "use": True},
                "freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
                "P_sum_import": {"port": 72, "digits": 2, "Unit": "kWh", "use": True},
                "P_sum_export": {"port": 74, "digits": 2, "Unit": "kWH", "use": True},
                "Pr_sum_import": {"port": 76, "digits": 2, "Unit": "kVArh", "use": True},
                "Pr_sum_export": {"port": 78, "digits": 2, "Unit": "kVArh", "use": True},
                "VAh_seit_reset": {"port": 80, "digits": 2, "Unit": "kVAh", "use": True},
                "Ah_seit_reset": {"port": 82, "digits": 2, "Unit": "Ah", "use": True},
                "P_sum": {"port": 84, "digits": 2, "Unit": "W", "use": True},
                "P_max": {"port": 86, "digits": 2, "Unit": "W", "use": True},
                "Gesamtscheinleistung": {"port": 100, "digits": 2, "Unit": "VA", "use": True},
                "Max_Gesamtscheinleistung": {"port": 102, "digits": 2, "Unit": "VA", "use": True},
                "Gesamtstrom_Neutralleiter": {"port": 104, "digits": 2, "Unit": "A", "use": True},
                "Max_Strom_Neutralleiter": {"port": 106, "digits": 2, "Unit": "A", "use": True},
                "U_L1_L2": {"port": 200, "digits": 2, "Unit": "V", "use": True},
                "U_L2_L3": {"port": 202, "digits": 2, "Unit": "V", "use": True},
                "U_L3_L1": {"port": 204, "digits": 2, "Unit": "V", "use": True},
                "U_L_L_avg": {"port": 206, "digits": 2, "Unit": "V", "use": True},
                "Strom_Neutralleiter": {"port": 224, "digits": 2, "Unit": "A", "use": True},
                "THD_U_L1": {"port": 234, "digits": 2, "Unit": "%", "use": True},
                "THD_U_L2": {"port": 236, "digits": 2, "Unit": "%", "use": True},
                "THD_U_L3": {"port": 238, "digits": 2, "Unit": "%", "use": True},
                "THD_I_L1": {"port": 240, "digits": 2, "Unit": "%", "use": True},
                "THD_I_L2": {"port": 242, "digits": 2, "Unit": "%", "use": True},
                "THD_I_L3": {"port": 244, "digits": 2, "Unit": "%", "use": True},
                "THD_U_avg": {"port": 248, "digits": 2, "Unit": "%", "use": True},
                "THD_I_avg": {"port": 250, "digits": 2, "Unit": "%", "use": True},
                "I_L1_demand": {"port": 258, "digits": 2, "Unit": "A", "use": True},
                "I_L2_demand": {"port": 260, "digits": 2, "Unit": "A", "use": True},
                "I_L3_demand": {"port": 262, "digits": 2, "Unit": "A", "use": True},
                "I_L1_demand_max": {"port": 264, "digits": 2, "Unit": "A", "use": True},
                "I_L2_demand_max": {"port": 266, "digits": 2, "Unit": "A", "use": True},
                "I_L3_demand_max": {"port": 268, "digits": 2, "Unit": "A", "use": True},
                "THD_U_L1_L2": {"port": 334, "digits": 2, "Unit": "%", "use": True},
                "THD_U_L2_L3": {"port": 336, "digits": 2, "Unit": "%", "use": True},
                "THD_U_L3_L1": {"port": 338, "digits": 2, "Unit": "%", "use": True},
                "THD_U_L_L_avg": {"port": 340, "digits": 2, "Unit": "%", "use": True},
                "Total_kwh": {"port": 342, "digits": 2, "Unit": "kwh", "use": True},
                "Total_kvarh": {"port": 344, "digits": 2, "Unit": "kvarh", "use": True},
                "P_L1_import": {"port": 346, "digits": 2, "Unit": "kwh", "use": True},
                "P_L2_import": {"port": 348, "digits": 2, "Unit": "kwh", "use": True},
                "P_L3_import": {"port": 350, "digits": 2, "Unit": "kwh", "use": True},
                "P_L1_export": {"port": 352, "digits": 2, "Unit": "kwh", "use": True},
                "P_L2_export": {"port": 354, "digits": 2, "Unit": "kwh", "use": True},
                "P_L3_export": {"port": 356, "digits": 2, "Unit": "kwh", "use": True},
                "I_L1_tot": {"port": 358, "digits": 2, "Unit": "kwh", "use": True},
                "I_L2_tot": {"port": 360, "digits": 2, "Unit": "kwh", "use": True},
                "I_L3_tot": {"port": 362, "digits": 2, "Unit": "kwh", "use": True},
                "Pr_L1_import": {"port": 364, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L2_import": {"port": 366, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L3_import": {"port": 368, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L1_export": {"port": 370, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L2_export": {"port": 372, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L3_export": {"port": 374, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L1_tot": {"port": 376, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L2_tot": {"port": 378, "digits": 2, "Unit": "kvarh", "use": True},
                "Pr_L3_tot": {"port": 380, "digits": 2, "Unit": "kvarh", "use": True},
            }
    elif sdm_model == "SDM630tiny":
            sdm_register = {
                "U_L1": {"port": 0, "digits": 2, "Unit": "V", "use": True},
                "U_L2": {"port": 2, "digits": 2, "Unit": "V", "use": True},
                "U_L3": {"port": 4, "digits": 2, "Unit": "V", "use": True},
                "I_L1": {"port": 6, "digits": 2, "Unit": "A", "use": True},
                "I_L2": {"port": 8, "digits": 2, "Unit": "A", "use": True},
                "I_L3": {"port": 10, "digits": 2, "Unit": "A", "use": True},
                "P_L1": {"port": 12, "digits": 2, "Unit": "W", "use": True},
                "P_L2": {"port": 14, "digits": 2, "Unit": "W", "use": True},
                "P_L3": {"port": 16, "digits": 2, "Unit": "W", "use": True},
                "freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
                "P_sum_import": {"port": 72, "digits": 2, "Unit": "kWh", "use": True},
                "P_sum_export": {"port": 74, "digits": 2, "Unit": "kWH", "use": True},
            }
    else:
        print("model not found")
        sys.exit(1)
    return sdm_register


def get_cli_arguments(scan_additional_arguments=None):
    parser = argparse.ArgumentParser()
    parser.prog='sdm'
    parser.description='get all paramater of a sdm-smartmeter device'  

    parser.add_argument('-d', '--device',
                        nargs='?', default=METER_SERIALPORT, const=None,
                        help='Path to serial device like /dev/ttyUSB0.'
                             'Default: %s' % METER_SERIALPORT)
    parser.add_argument('-a', '--address', type=int, 
                        nargs='?', default=METER_MODBUSADDRESS, const=None,
                        help='Modbusaddress of the device.'
                             'Default: %s' % METER_MODBUSADDRESS)
    parser.add_argument('-m', '--model',
                        nargs='?', default=METER_MODEL, const=None,
                        help='Modell of the device'
                             'Default: %s' % METER_MODEL)
    parser.add_argument('-o', '--output',
                        nargs='?', default=OUTPUTFORMAT, const=None,
                        help='Output format'
                             'Default: %s' % OUTPUTFORMAT)
    parser.add_argument('-t', '--measurement',
                        nargs='?', default=MEASUREMENT, const=None,
                        help='Output format'
                             'Default: %s' % MEASUREMENT)
    parser.add_argument('-s', '--sleep', type=int,
                        nargs='?', default=SLEEP, const=None,
                        help='Output format'
                             'Default: %s' % SLEEP)
    parser.add_argument('-b', '--baudrate', type=int,
                        nargs='?', default=BAUDRATE, const=None,
                        help='Output format'
                             'Default: %s' % BAUDRATE)
    if scan_additional_arguments:
        scan_additional_arguments(parser)
    args = parser.parse_args()
    return args

args = get_cli_arguments()

#print (args.device)
#print (str(args.baudrate))
#print (str(args.address))
wurst = args.device

if not args.device:
    print('device required')
    print()
    helpmessage()
    sys.exit(1)
else:
    try:
        instrument = minimalmodbus.Instrument( args.device, args.address)
        instrument.serial.baudrate = args.baudrate
        instrument.serial.timeout = 5
        instrument.debug = False
        instrument.clear_buffers_before_each_transaction = True
        sdm_register = get_sdm_register(args.model)
        for key in sdm_register:
            if sdm_register[key]["use"] == True:
                if args.output == "cli":
                    print(key + ": " 
                        + str(
                            round(
                                instrument.read_float(
                                    functioncode=4, 
                                    registeraddress=sdm_register[key]["port"], 
                                    number_of_registers=sdm_register[key]["digits"]
                                ), 
                                2
                            )
                        ) 
                        + sdm_register[key]["Unit"]
                    )
                elif args.output == "influxlineprotocol":
                    print("SDMTEST,address=" + str(args.address)  
                        + ",model='" + args.model + "'"
                        + " " + key + "=" + str(
                            round(
                                instrument.read_float(
                                    functioncode=4,
                                    registeraddress=sdm_register[key]["port"],
                                    number_of_registers=sdm_register[key]["digits"]
                                ),2
                            )
                        )
#                        + ",unit='" + sdm_register[key]["Unit"] + "'"
                    )
                else:
                    print("outputformat not found")
                    print()
                    show_connection_parameters()
                    sys.exit(1)
            time.sleep(SLEEP)
    except BaseException:
        #print(BaseException)
        #print("can not connect to device")
        #print()
        #show_connection_parameters()
        sys.exit(1)
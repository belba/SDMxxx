import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument.serial.baudrate = 38400
input_register = {
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

#for key in input_register:
#	if input_register[key]["use"] == True:
#		U_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register[key]["port"], number_of_registers=input_register[key]["digits"]), 2)) + input_register[key]["Unit"])
#		print(key + ": " + str(round(instrument.read_float(functioncode=4, registeraddress=input_register[key]["port"], number_of_registers=input_register[key]["digits"]), 2)) + input_register[key]["Unit"])

U_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L1"]["port"], number_of_registers=input_register["U_L1"]["digits"]), 2)) + input_register["U_L2"]["Unit"]
U_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L2"]["port"], number_of_registers=input_register["U_L2"]["digits"]), 2)) + input_register["U_L2"]["Unit"]
U_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L3"]["port"], number_of_registers=input_register["U_L3"]["digits"]), 2)) + input_register["U_L3"]["Unit"]
I_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L1"]["port"], number_of_registers=input_register["I_L1"]["digits"]), 2)) + input_register["I_L2"]["Unit"]
I_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L2"]["port"], number_of_registers=input_register["I_L2"]["digits"]), 2)) + input_register["I_L2"]["Unit"]
I_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L3"]["port"], number_of_registers=input_register["I_L3"]["digits"]), 2)) + input_register["I_L3"]["Unit"]
P_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L1"]["port"], number_of_registers=input_register["P_L1"]["digits"]), 2)) + input_register["P_L1"]["Unit"]
P_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L2"]["port"], number_of_registers=input_register["P_L2"]["digits"]), 2)) + input_register["P_L2"]["Unit"]
P_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L3"]["port"], number_of_registers=input_register["P_L3"]["digits"]), 2)) + input_register["P_L3"]["Unit"]
Ps_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps_L1"]["port"], number_of_registers=input_register["Ps_L1"]["digits"]), 2)) + input_register["Ps_L1"]["Unit"]
Ps_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps_L2"]["port"], number_of_registers=input_register["Ps_L2"]["digits"]), 2)) + input_register["Ps_L2"]["Unit"]
Ps_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps_L3"]["port"], number_of_registers=input_register["Ps_L3"]["digits"]), 2)) + input_register["Ps_L3"]["Unit"]
Pr_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L1"]["port"], number_of_registers=input_register["Pr_L1"]["digits"]), 2)) + input_register["Pr_L1"]["Unit"]
Pr_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L2"]["port"], number_of_registers=input_register["Pr_L2"]["digits"]), 2)) + input_register["Pr_L2"]["Unit"]
Pr_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L3"]["port"], number_of_registers=input_register["Pr_L3"]["digits"]), 2)) + input_register["Pr_L3"]["Unit"]
Lfakt_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Leistungsfaktor_L1"]["port"], number_of_registers=input_register["Leistungsfaktor_L1"]["digits"]), 2)) + input_register["Leistungsfaktor_L1"]["Unit"]
Lfakt_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Leistungsfaktor_L2"]["port"], number_of_registers=input_register["Leistungsfaktor_L2"]["digits"]), 2)) + input_register["Leistungsfaktor_L2"]["Unit"]
Lfakt_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Leistungsfaktor_L3"]["port"], number_of_registers=input_register["Leistungsfaktor_L3"]["digits"]), 2)) + input_register["Leistungsfaktor_L3"]["Unit"]
Pwin_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Phasenwinkel_L1"]["port"], number_of_registers=input_register["Phasenwinkel_L1"]["digits"]), 2)) + input_register["Phasenwinkel_L1"]["Unit"]
Pwin_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Phasenwinkel_L2"]["port"], number_of_registers=input_register["Phasenwinkel_L2"]["digits"]), 2)) + input_register["Phasenwinkel_L2"]["Unit"]
Pwin_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Phasenwinkel_L3"]["port"], number_of_registers=input_register["Phasenwinkel_L3"]["digits"]), 2)) + input_register["Phasenwinkel_L3"]["Unit"]
THD_U_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L1"]["port"], number_of_registers=input_register["THD_U_L1"]["digits"]), 2)) + input_register["THD_U_L1"]["Unit"]
THD_U_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L2"]["port"], number_of_registers=input_register["THD_U_L2"]["digits"]), 2)) + input_register["THD_U_L2"]["Unit"]
THD_U_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L3"]["port"], number_of_registers=input_register["THD_U_L3"]["digits"]), 2)) + input_register["THD_U_L3"]["Unit"]
THD_I_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_I_L1"]["port"], number_of_registers=input_register["THD_I_L1"]["digits"]), 2)) + input_register["THD_I_L1"]["Unit"]
THD_I_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_I_L2"]["port"], number_of_registers=input_register["THD_I_L2"]["digits"]), 2)) + input_register["THD_I_L2"]["Unit"]
THD_I_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_I_L3"]["port"], number_of_registers=input_register["THD_I_L3"]["digits"]), 2)) + input_register["THD_I_L3"]["Unit"]
I_L1_demand = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L1_demand"]["port"], number_of_registers=input_register["I_L1_demand"]["digits"]), 2)) + input_register["I_L1_demand"]["Unit"]
I_L2_demand = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L2_demand"]["port"], number_of_registers=input_register["I_L2_demand"]["digits"]), 2)) + input_register["I_L2_demand"]["Unit"]
I_L3_demand = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L3_demand"]["port"], number_of_registers=input_register["I_L3_demand"]["digits"]), 2)) + input_register["I_L3_demand"]["Unit"]
I_L1_demand_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L1_demand_max"]["port"], number_of_registers=input_register["I_L1_demand_max"]["digits"]), 2)) + input_register["I_L1_demand_max"]["Unit"]
I_L2_demand_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L2_demand_max"]["port"], number_of_registers=input_register["I_L2_demand_max"]["digits"]), 2)) + input_register["I_L2_demand_max"]["Unit"]
I_L3_demand_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L3_demand_max"]["port"], number_of_registers=input_register["I_L3_demand_max"]["digits"]), 2)) + input_register["I_L3_demand_max"]["Unit"]
I_L1_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L1_tot"]["port"], number_of_registers=input_register["I_L1_tot"]["digits"]), 2)) + input_register["I_L1_tot"]["Unit"]
I_L2_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L2_tot"]["port"], number_of_registers=input_register["I_L2_tot"]["digits"]), 2)) + input_register["I_L2_tot"]["Unit"]
I_L3_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_L3_tot"]["port"], number_of_registers=input_register["I_L3_tot"]["digits"]), 2)) + input_register["I_L3_tot"]["Unit"]
Pr_L1_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L1_tot"]["port"], number_of_registers=input_register["Pr_L1_tot"]["digits"]), 2)) + input_register["Pr_L1_tot"]["Unit"]
Pr_L2_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L2_tot"]["port"], number_of_registers=input_register["Pr_L2_tot"]["digits"]), 2)) + input_register["Pr_L2_tot"]["Unit"]
Pr_L3_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L3_tot"]["port"], number_of_registers=input_register["Pr_L3_tot"]["digits"]), 2)) + input_register["Pr_L3_tot"]["Unit"]
P_L1_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L1_import"]["port"], number_of_registers=input_register["P_L1_import"]["digits"]), 2)) + input_register["P_L1_import"]["Unit"]
P_L2_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L2_import"]["port"], number_of_registers=input_register["P_L2_import"]["digits"]), 2)) + input_register["P_L2_import"]["Unit"]
P_L3_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L3_import"]["port"], number_of_registers=input_register["P_L3_import"]["digits"]), 2)) + input_register["P_L3_import"]["Unit"]
P_L1_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L1_export"]["port"], number_of_registers=input_register["P_L1_export"]["digits"]), 2)) + input_register["P_L1_export"]["Unit"]
P_L2_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L2_export"]["port"], number_of_registers=input_register["P_L2_export"]["digits"]), 2)) + input_register["P_L2_export"]["Unit"]
P_L3_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_L3_export"]["port"], number_of_registers=input_register["P_L3_export"]["digits"]), 2)) + input_register["P_L3_export"]["Unit"]
Pr_L1_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L1_import"]["port"], number_of_registers=input_register["Pr_L1_import"]["digits"]), 2)) + input_register["Pr_L1_import"]["Unit"]
Pr_L2_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L2_import"]["port"], number_of_registers=input_register["Pr_L2_import"]["digits"]), 2)) + input_register["Pr_L2_import"]["Unit"]
Pr_L3_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L3_import"]["port"], number_of_registers=input_register["Pr_L3_import"]["digits"]), 2)) + input_register["Pr_L3_import"]["Unit"]
Pr_L1_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L1_export"]["port"], number_of_registers=input_register["Pr_L1_export"]["digits"]), 2)) + input_register["Pr_L1_export"]["Unit"]
Pr_L2_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L2_export"]["port"], number_of_registers=input_register["Pr_L2_export"]["digits"]), 2)) + input_register["Pr_L2_export"]["Unit"]
Pr_L3_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_L3_export"]["port"], number_of_registers=input_register["Pr_L3_export"]["digits"]), 2)) + input_register["Pr_L3_export"]["Unit"]
P_sum_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_sum_import"]["port"], number_of_registers=input_register["P_sum_import"]["digits"]), 2)) + input_register["P_sum_import"]["Unit"]
P_sum_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_sum_export"]["port"], number_of_registers=input_register["P_sum_export"]["digits"]), 2)) + input_register["P_sum_export"]["Unit"]
Pr_sum_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_sum_import"]["port"], number_of_registers=input_register["Pr_sum_import"]["digits"]), 2)) + input_register["Pr_sum_import"]["Unit"]
Pr_sum_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_sum_export"]["port"], number_of_registers=input_register["Pr_sum_export"]["digits"]), 2)) + input_register["Pr_sum_export"]["Unit"]
U_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_avg"]["port"], number_of_registers=input_register["U_avg"]["digits"]), 2)) + input_register["U_avg"]["Unit"]
I_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_avg"]["port"], number_of_registers=input_register["I_avg"]["digits"]), 2)) + input_register["I_avg"]["Unit"]
I_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_sum"]["port"], number_of_registers=input_register["I_sum"]["digits"]), 2)) + input_register["I_sum"]["Unit"]
P_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_sum"]["port"], number_of_registers=input_register["P_sum"]["digits"]), 2)) + input_register["P_sum"]["Unit"]
Ps_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps_sum"]["port"], number_of_registers=input_register["Ps_sum"]["digits"]), 2)) + input_register["Ps_sum"]["Unit"]
Pr_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_sum"]["port"], number_of_registers=input_register["Pr_sum"]["digits"]), 2)) + input_register["Pr_sum"]["Unit"]
Lfakt_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Lfakt_sum"]["port"], number_of_registers=input_register["Lfakt_sum"]["digits"]), 2)) + input_register["Lfakt_sum"]["Unit"]
Pwin_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pwin_sum"]["port"], number_of_registers=input_register["Pwin_sum"]["digits"]), 2)) + input_register["Pwin_sum"]["Unit"]
freq = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["freq"]["port"], number_of_registers=input_register["freq"]["digits"]), 2)) + input_register["freq"]["Unit"]
THD_U_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_avg"]["port"], number_of_registers=input_register["THD_U_avg"]["digits"]), 2)) + input_register["THD_U_avg"]["Unit"]
THD_I_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_I_avg"]["port"], number_of_registers=input_register["THD_I_avg"]["digits"]), 2)) + input_register["THD_I_avg"]["Unit"]
U_L1_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L1_L2"]["port"], number_of_registers=input_register["U_L1_L2"]["digits"]), 2)) + input_register["U_L1_L2"]["Unit"]
U_L2_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L2_L3"]["port"], number_of_registers=input_register["U_L2_L3"]["digits"]), 2)) + input_register["U_L2_L3"]["Unit"]
U_L3_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L3_L1"]["port"], number_of_registers=input_register["U_L3_L1"]["digits"]), 2)) + input_register["U_L3_L1"]["Unit"]
U_L_L_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U_L_L_avg"]["port"], number_of_registers=input_register["U_L_L_avg"]["digits"]), 2)) + input_register["U_L_L_avg"]["Unit"]
THD_U_L1_L2 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L1_L2"]["port"], number_of_registers=input_register["THD_U_L1_L2"]["digits"]), 2)) + input_register["THD_U_L1_L2"]["Unit"]
THD_U_L2_L3 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L2_L3"]["port"], number_of_registers=input_register["THD_U_L2_L3"]["digits"]), 2)) + input_register["THD_U_L2_L3"]["Unit"]
THD_U_L3_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L3_L1"]["port"], number_of_registers=input_register["THD_U_L3_L1"]["digits"]), 2)) + input_register["THD_U_L3_L1"]["Unit"]
THD_U_L_L_avg = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U_L_L_avg"]["port"], number_of_registers=input_register["THD_U_L_L_avg"]["digits"]), 2)) + input_register["THD_U_L_L_avg"]["Unit"]
P_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_max"]["port"], number_of_registers=input_register["P_max"]["digits"]), 2)) + input_register["P_max"]["Unit"]

#	"Gesamtwirkleistung": {"port": 84, "digits": 2, "Unit": "W", "use": True},
#	"Max_Gesamtwirkleistung": {"port": 86, "digits": 2, "Unit": "W", "use": True},

#	"Gesamtscheinleistung": {"port": 100, "digits": 2, "Unit": "VA", "use": True},
#	"Max_Gesamtscheinleistung": {"port": 102, "digits": 2, "Unit": "VA", "use": True},

#	"Gesamtstrom_Neutralleiter": {"port": 104, "digits": 2, "Unit": "A", "use": True},
#	"Max_Strom_Neutralleiter": {"port": 106, "digits": 2, "Unit": "A", "use": True},
#	"Strom_Neutralleiter": {"port": 224, "digits": 2, "Unit": "A", "use": True},

#	"VAh_seit_reset": {"port": 80, "digits": 2, "Unit": "kVAh", "use": True},
#	"Ah_seit_reset": {"port": 82, "digits": 2, "Unit": "Ah", "use": True},

#	"Total_kwh": {"port": 342, "digits": 2, "Unit": "kwh", "use": True},
#	"Total_kvarh": {"port": 344, "digits": 2, "Unit": "kvarh", "use": True},

print("Value                      L1          L2          L3            Sum           Avg        Max")
print("----------------------------------------------------------------------------------------------------")
print("U                          " + U_L1 + "        " + U_L2 + "        " + U_L3 + "                     " + U_avg);
print("I                          " + I_L1 + "        " + I_L2 + "        " + I_L3 + "         " + I_sum + "         " + I_avg);
print("f                          " + freq);
print("P                          " + P_L1 + "        " + P_L2 + "        " + P_L3 + "          " + P_sum + "                   " + P_max);
print("Ps                         " + Ps_L1 + "       " + Ps_L2 + "       " + Ps_L3 + "        " + Ps_sum);
print("Pr                         " + Pr_L1 + "      " + Ps_L2 + "       " + Pr_L3 + "      " + Pr_sum);
print("Leistungsfaktor            " + Lfakt_L1 + "         " + Lfakt_L2 + "         " + Lfakt_L3 + "           " + Lfakt_sum);
print("Phasenwinkel               " + Pwin_L1 + "     " + Pwin_L2 + "     " + Pwin_L3 + "      " + Pwin_sum);
print("THD U                      " + THD_U_L1 + "        " + THD_U_L2 + "        " + THD_U_L3 + "                       " + THD_U_avg);
print("THD I                      " + THD_I_L1 + "        " + THD_I_L2 + "        " + THD_I_L3 + "                       " + THD_I_avg);
print("I demand                   " + I_L1_demand + "        " + I_L2_demand + "        " + I_L3_demand);
print("I demand max               " + I_L1_demand_max + "        " + I_L2_demand_max + "        " + I_L3_demand_max);
print("I Total                    " + I_L1_tot + "     " + I_L2_tot + "     " + I_L3_tot);
print("Pr Total                   " + Pr_L1_tot + "   " + Pr_L2_tot + "   " + Pr_L3_tot);
print("P Import                   " + P_L1_import + "      " + P_L2_import + "      " + P_L3_import + "       " + P_sum_import);
print("P Export                   " + P_L1_export + "     " + P_L2_export + "     " + P_L3_export + "       " + P_sum_export);
print("Pr Import                  " + Pr_L1_import + "    " + Pr_L2_import + "    " + Pr_L3_import + "      " + Pr_sum_import);
print("Pr Export                  " + Pr_L1_export + "   " + Pr_L2_export + "   " + Pr_L3_export + "     " + Pr_sum_export);
print();
print("Value                      L1-L2          L2-L3          L3-L1            Sum           Avg")
print("--------------------------------------------------------------------------------------------------")
print("U                          " + U_L1_L2 + "           " + U_L2_L3 + "        " + U_L3_L1 + "                        " + U_L_L_avg);
print("THD U                      " + THD_U_L1_L2 + "           " + THD_U_L2_L3 + "           " + THD_U_L3_L1 + "                           " + THD_U_L_L_avg);

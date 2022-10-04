import minimalmodbus

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)  # port name, slave address (in decimal)
instrument.serial.baudrate = 38400
input_register = {
	"U": {"port": 4, "digits": 2, "Unit": "V", "use": True},
	"I": {"port": 10, "digits": 2, "Unit": "A", "use": True},
	"P": {"port": 16, "digits": 2, "Unit": "W", "use": True},
	"Ps": {"port": 22, "digits": 2, "Unit": "VA", "use": True},
	"Pr": {"port": 28, "digits": 2, "Unit": "VAr", "use": True},
	"Leistungsfaktor": {"port": 34, "digits": 2, "Unit": "", "use": True},
	"Phasenwinkel": {"port": 40, "digits": 2, "Unit": "Grad", "use": True},
	"freq": {"port": 70, "digits": 2, "Unit": "Hz", "use": True},
	"VAh_seit_reset": {"port": 80, "digits": 2, "Unit": "kVAh", "use": True},
	"Ah_seit_reset": {"port": 82, "digits": 2, "Unit": "Ah", "use": True},
	"P_sum": {"port": 84, "digits": 2, "Unit": "W", "use": True},
	"P_max": {"port": 86, "digits": 2, "Unit": "W", "use": True},
	"Gesamtscheinleistung": {"port": 100, "digits": 2, "Unit": "VA", "use": True},
	"Ps_max": {"port": 102, "digits": 2, "Unit": "VA", "use": True},
	"Gesamtstrom_Neutralleiter": {"port": 104, "digits": 2, "Unit": "A", "use": True},
	"Max_Strom_Neutralleiter": {"port": 106, "digits": 2, "Unit": "A", "use": True},
	"Strom_Neutralleiter": {"port": 224, "digits": 2, "Unit": "A", "use": True},
	"THD_U": {"port": 238, "digits": 2, "Unit": "%", "use": True},
	"THD_I": {"port": 244, "digits": 2, "Unit": "%", "use": True},
	"I_demand": {"port": 262, "digits": 2, "Unit": "A", "use": True},
	"I_demand_max": {"port": 268, "digits": 2, "Unit": "A", "use": True},
	"Total_kwh": {"port": 342, "digits": 2, "Unit": "kwh", "use": True},
	"Total_kvarh": {"port": 344, "digits": 2, "Unit": "kvarh", "use": True},
	"P_import": {"port": 350, "digits": 2, "Unit": "kwh", "use": True},
	"P_export": {"port": 356, "digits": 2, "Unit": "kwh", "use": True},
	"I_tot": {"port": 362, "digits": 2, "Unit": "kwh", "use": True},
	"Pr_import": {"port": 368, "digits": 2, "Unit": "kvarh", "use": True},
	"Pr_export": {"port": 374, "digits": 2, "Unit": "kvarh", "use": True},
	"Pr_tot": {"port": 380, "digits": 2, "Unit": "kvarh", "use": True},
}

#for key in input_register:
#	if input_register[key]["use"] == True:
#		U_L1 = str(round(instrument.read_float(functioncode=4, registeraddress=input_register[key]["port"], number_of_registers=input_register[key]["digits"]), 2)) + input_register[key]["Unit"])
#		print(key + ": " + str(round(instrument.read_float(functioncode=4, registeraddress=input_register[key]["port"], number_of_registers=input_register[key]["digits"]), 2)) + input_register[key]["Unit"])

U = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["U"]["port"], number_of_registers=input_register["U"]["digits"]), 2)) + input_register["U"]["Unit"]
I = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I"]["port"], number_of_registers=input_register["I"]["digits"]), 2)) + input_register["I"]["Unit"]
P = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P"]["port"], number_of_registers=input_register["P"]["digits"]), 2)) + input_register["P"]["Unit"]
Ps = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps"]["port"], number_of_registers=input_register["Ps"]["digits"]), 2)) + input_register["Ps"]["Unit"]
Pr = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr"]["port"], number_of_registers=input_register["Pr"]["digits"]), 2)) + input_register["Pr"]["Unit"]
Lfakt = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Leistungsfaktor"]["port"], number_of_registers=input_register["Leistungsfaktor"]["digits"]), 2)) + input_register["Leistungsfaktor"]["Unit"]
Pwin = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Phasenwinkel"]["port"], number_of_registers=input_register["Phasenwinkel"]["digits"]), 2)) + input_register["Phasenwinkel"]["Unit"]
THD_U = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_U"]["port"], number_of_registers=input_register["THD_U"]["digits"]), 2)) + input_register["THD_U"]["Unit"]
THD_I = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["THD_I"]["port"], number_of_registers=input_register["THD_I"]["digits"]), 2)) + input_register["THD_I"]["Unit"]
I_demand = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_demand"]["port"], number_of_registers=input_register["I_demand"]["digits"]), 2)) + input_register["I_demand"]["Unit"]
I_demand_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_demand_max"]["port"], number_of_registers=input_register["I_demand_max"]["digits"]), 2)) + input_register["I_demand_max"]["Unit"]
I_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["I_tot"]["port"], number_of_registers=input_register["I_tot"]["digits"]), 2)) + input_register["I_tot"]["Unit"]
Pr_tot = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_tot"]["port"], number_of_registers=input_register["Pr_tot"]["digits"]), 2)) + input_register["Pr_tot"]["Unit"]
P_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_import"]["port"], number_of_registers=input_register["P_import"]["digits"]), 2)) + input_register["P_import"]["Unit"]
P_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_export"]["port"], number_of_registers=input_register["P_export"]["digits"]), 2)) + input_register["P_export"]["Unit"]
Pr_import = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_import"]["port"], number_of_registers=input_register["Pr_import"]["digits"]), 2)) + input_register["Pr_import"]["Unit"]
Pr_export = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Pr_export"]["port"], number_of_registers=input_register["Pr_export"]["digits"]), 2)) + input_register["Pr_export"]["Unit"]
P_sum = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_sum"]["port"], number_of_registers=input_register["P_sum"]["digits"]), 2)) + input_register["P_sum"]["Unit"]
P_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["P_max"]["port"], number_of_registers=input_register["P_max"]["digits"]), 2)) + input_register["P_max"]["Unit"]
Ps_max = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["Ps_max"]["port"], number_of_registers=input_register["Ps_max"]["digits"]), 2)) + input_register["Ps_max"]["Unit"]
freq = str(round(instrument.read_float(functioncode=4, registeraddress=input_register["freq"]["port"], number_of_registers=input_register["freq"]["digits"]), 2)) + input_register["freq"]["Unit"]

print("U                  " + U);
print("I                  " + I);
print("f                  " + freq);
print("P                  " + P);
print("P                  " + P);
print("P max              " + P_max);
print("Ps                 " + Ps);
print("Ps max             " + Ps_max);
print("Pr                 " + Pr);
print("Leistungsfaktor    " + Lfakt);
print("Phasenwinkel       " + Pwin);
print("THD U              " + THD_U);
print("THD I              " + THD_I);
print("I demand           " + I_demand);
print("I demand max       " + I_demand_max);
print("I Total            " + I_tot);
print("Pr Total           " + Pr_tot);
print("P Import           " + P_import);
print("P Export           " + P_export);
print("Pr Import          " + Pr_import);
print("Pr Export          " + Pr_export);

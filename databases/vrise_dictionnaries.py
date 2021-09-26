AmPercent_dict = {
       "":{"1":""},
      "4": {"1":"205", "3": "412"},
      "6": {"1":"306", "3": "615"},
      "10": {"1":"515", "3": "1034"},
      "16": {"1":"818", "3": "1643"},
      "25": {"1":"1289", "3": "2588"},
      "35": {"1":"1773", "3": "3560"},
      "50": {"1":"2377", "3": "4772"},
      "70": {"1":"3342", "3": "6712"},
      "95": {"1":"4445", "3": "8927"}
   }

cable_type_dict = {
"Copper":"Copper",
"Aluminium":"Aluminium"
}

###############################################################################
                                #Table 4#
###############################################################################

ccc_1p_2c_thermo_cu_wiring_enclosure_dict_solid={
"1":"13",
"1.5":"18",
"2.5":"24",
"4":"32",
"6":"41",
"10":"54",
"16":"70",
"25":"94",
"35":"112",
"Ref":"column 15"
}

ccc_1p_2c_thermo_cu_wiring_enclosure_dict_flexible={
"1":"14",
"1.5":"18",
"2.5":"24",
"4":"31",
"6":"40",
"10":"54",
"16":"69",
"25":"91",
"35":"110",
"Ref":"column 16"
}


ccc_1p_2c_thermo_cu_partial_thermal_insulation_dict={
"1":"11",
"1.5":"14",
"2.5":"20",
"4":"25",
"6":"33",
"10":"44",
"16":"56",
"25":"75",
"35":"90",
"Ref":"column 18"
}

ccc_1p_2c_thermo_cu_complete_thermal_insulation_dict={
"1":"6",
"1.5":"8",
"2.5":"12",
"4":"16",
"6":"20",
"10":"27",
"16":"36",
"25":"48",
"35":"59",
"Ref":"column 20"
}

###############################################################################
                                #Table 5#
###############################################################################

ccc_1p_2c_xlpe_cu_wiring_enclosure_dict_solid={
"1":"16",
"1.5":"21",
"2.5":"30",
"4":"38",
"6":"47",
"10":"65",
"16":"84",
"25":"113",
"35":"135",
"Ref":"column 15"
}

ccc_1p_2c_xlpe_cu_wiring_enclosure_dict_flexible={
"1":"17",
"1.5":"21",
"2.5":"28",
"4":"37",
"6":"46",
"10":"64",
"16":"82",
"25":"109",
"35":"132",
"Ref":"column 16"
}

ccc_1p_2c_xlpe_cu_partial_thermal_insulation_dict={
"1":"13",
"1.5":"16",
"2.5":"24",
"4":"30",
"6":"38",
"10":"52",
"16":"67",
"25":"90",
"35":"108",
"Ref":"column 18"
}

ccc_1p_2c_xlpe_cu_complete_thermal_insulation_dict={
"1":"8",
"1.5":"10",
"2.5":"14",
"4":"19",
"6":"24",
"10":"32",
"16":"43",
"25":"58",
"35":"72",
"Ref":"column 20"
}



###############################################################################
                                #Table 13#
###############################################################################

ccc_3p_thermo_cu_wiring_enclosure_in_air_solid={
"1":"11",
"1.5":"14",
"2.5":"20",
"4":"25",
"6":"33",
"10":"44",
"16":"58",
"25":"76",
"35":"94",
"Ref":"column 11"
}

ccc_3p_thermo_cu_wiring_enclosure_in_air_flexible={
"1":"11",
"1.5":"14",
"2.5":"19",
"4":"24",
"6":"32",
"10":"43",
"16":"57",
"25":"73",
"35":"92",
"Ref":"column 12"
}

ccc_3p_thermo_cu_partial_thermal_insulation_dict={
"1":"9",
"1.5":"11",
"2.5":"16",
"4":"20",
"6":"26",
"10":"35",
"16":"47",
"25":"60",
"35":"75",
"Ref":"column 17"
}

ccc_3p_thermo_cu_complete_thermal_insulation_dict={
"1":"5",
"1.5":"7",
"2.5":"10",
"4":"13",
"6":"16",
"10":"22",
"16":"29",
"25":"38",
"35":"47",
"Ref":"column 21"
}

###############################################################################
                                #Table 14#
###############################################################################

ccc_3p_xlpe_cu_wiring_enclosure_in_air_solid={
"1":"13",
"1.5":"16",
"2.5":"24",
"4":"30",
"6":"38",
"10":"53",
"16":"68",
"25":"91",
"35":"114",
"Ref":"column 11"
}

ccc_3p_xlpe_cu_wiring_enclosure_in_air_flexible={
"1":"14",
"1.5":"17",
"2.5":"23",
"4":"29",
"6":"37",
"10":"52",
"16":"67",
"25":"89",
"35":"111",
"Ref":"column 12"
}

ccc_3p_xlpe_cu_partial_thermal_insulation_dict={
"1":"10",
"1.5":"13",
"2.5":"19",
"4":"24",
"6":"30",
"10":"42",
"16":"55",
"25":"73",
"35":"91",
"Ref":"column 17"
}

ccc_3p_xlpe_cu_complete_thermal_insulation_dict={
"1":"6",
"1.5":"8",
"2.5":"12",
"4":"15",
"6":"19",
"10":"26",
"16":"34",
"25":"46",
"35":"57",
"Ref":"column 21"
}

###############################################################################
                                #List of dicts#
###############################################################################

ccc_1p_xlpe_cu_dict= {
"Wiring enclosure in air / solid":ccc_1p_2c_xlpe_cu_wiring_enclosure_dict_solid,
"Wiring enclosure in air / flexible":ccc_1p_2c_xlpe_cu_wiring_enclosure_dict_flexible,
"PartialThermalInsulation":ccc_1p_2c_xlpe_cu_partial_thermal_insulation_dict,
"CompleteThermalInsulation":ccc_1p_2c_xlpe_cu_complete_thermal_insulation_dict
}

ccc_1p_thermo_cu_dict= {
"Wiring enclosure in air / solid":ccc_1p_2c_thermo_cu_wiring_enclosure_dict_solid,
"Wiring enclosure in air / flexible":ccc_1p_2c_thermo_cu_wiring_enclosure_dict_flexible,
"PartialThermalInsulation":ccc_1p_2c_thermo_cu_partial_thermal_insulation_dict,
"CompleteThermalInsulation":ccc_1p_2c_thermo_cu_complete_thermal_insulation_dict
}

ccc_3p_thermo_cu_dict= {
"Wiring Enclosure in air - Solid/Stranded ":ccc_3p_thermo_cu_wiring_enclosure_in_air_solid,
"Wiring Enclosure in air - Flexible ":ccc_3p_thermo_cu_wiring_enclosure_in_air_flexible,
"Partial Thermal Insulation":ccc_3p_thermo_cu_partial_thermal_insulation_dict,
"Complete Thermal Insulation":ccc_3p_thermo_cu_complete_thermal_insulation_dict
}

ccc_3p_xlpe_cu_dict= {
"Wiring Enclosure in air - Solid/Stranded ":ccc_3p_xlpe_cu_wiring_enclosure_in_air_solid,
"Wiring Enclosure in air - Flexible ":ccc_3p_xlpe_cu_wiring_enclosure_in_air_flexible,
"Partial Thermal Insulation":ccc_3p_xlpe_cu_partial_thermal_insulation_dict,
"Complete Thermal Insulation":ccc_3p_xlpe_cu_complete_thermal_insulation_dict
}

ccc_1p_xlpe_dict={
"Cu":ccc_1p_xlpe_cu_dict,
"Al":"",
"Ref":"Table 5 - Cable Type : Two Single Core - Insulation Type : Thermosetting (XLPE, R-EP-90...)"
}

ccc_1p_thermo_dict={
"Cu":ccc_1p_thermo_cu_dict,
"Al":"",
"Ref":"Table 4 - Cable Type : Two Single Core - Insulation Type : Thermoplastic"
}

ccc_3p_thermo_dict={
"Cu":ccc_3p_thermo_cu_dict,
"Al":"",
"Ref":"Table 13 - Cable Type : Three Core and Four Core- Insulation Type : Thermoplastic"
}

ccc_3p_xlpe_dict={
"Cu":ccc_3p_xlpe_cu_dict,
"Al":"",
"Ref":"Table 14 - Cable Type : Three Core and Four Core- Insulation Type : Thermosetting (XLPE, R-EP-90...)"
}

ccc_1p_dict ={
"Xlpe":ccc_1p_xlpe_dict,
"Thermo":ccc_1p_thermo_dict
}

ccc_3p_dict={
"Thermo":ccc_3p_thermo_dict,
"Xlpe":ccc_3p_xlpe_dict,
}

ccc_dict= {
"1":ccc_1p_dict,
"3":ccc_3p_dict
}

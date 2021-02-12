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

ccc_1p_xlpe_cu_touching_dict={
"1":"16",
"1.5":"20",
"2.5":"28",
"4":"37",
"6":"47",
"10":"65",
"16":"86",
"25":"117",
"35":"144"
}

ccc_1p_xlpe_cu_exposed_sun_dict={
"1":"12",
"1.5":"15",
"2.5":"21",
"4":"28",
"6":"36",
"10":"48",
"16":"64",
"25":"86",
"35":"105"
}

ccc_1p_xlpe_cu_partial_thermal_insulation_dict={
"1":"13",
"1.5":"16",
"2.5":"24",
"4":"30",
"6":"38",
"10":"52",
"16":"67",
"25":"90",
"35":"108"
}

ccc_1p_xlpe_cu_complete_thermal_insulation_dict={
"1":"8",
"1.5":"10",
"2.5":"14",
"4":"19",
"6":"24",
"10":"32",
"16":"43",
"25":"58",
"35":"72"
}

ccc_1p_xlpe_cu_dict= {
"Touching":ccc_1p_xlpe_cu_touching_dict,
"ExposedToSun":ccc_1p_xlpe_cu_exposed_sun_dict,
"PartialThermalInsulation":ccc_1p_xlpe_cu_partial_thermal_insulation_dict,
"CompleteThermalInsulation":ccc_1p_xlpe_cu_complete_thermal_insulation_dict
}

ccc_1p_xlpe_al_dict={
"":""
}

ccc_1p_dict ={
"XlpeCu":ccc_1p_xlpe_cu_dict,
"XlpeAL":ccc_1p_xlpe_al_dict
}

ccc_3p_dict={
"":""
}

ccc_dict= {
"1":ccc_1p_dict,
"3":ccc_3p_dict
}

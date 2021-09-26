lg_neon_dict = {
"LG355N": {"P":"355", "Voc": "41.4", "Isc":"10.65","model":"LG NeON 2","Vmp":"35.7","panelSerial":"LG35N1C-N5","Url":"https://www.lgenergy.com.au/uploads/download_files/075fed5145c7b387f78464077ec7f68d158a7950.pdf"},
"LG360N": {"P":"360", "Voc": "41.6", "Isc":"10.84","model":"LG NeON 2","Vmp":"35.1","panelSerial":"LG360N1C-N5","Url":"https://www.lgenergy.com.au/uploads/download_files/075fed5145c7b387f78464077ec7f68d158a7950.pdf"},
"LG365N": {"P":"365", "Voc": "41.7", "Isc":"10.88","model":"LG NeON 2","Vmp":"35.5","panelSerial":"LG365N1C-N5","Url":"https://www.lgenergy.com.au/uploads/download_files/c368443778f812ed588ab828f94d48665c29a89f.pdf"},
}

lg_monox_dict = {
"LG365M": {"P":"365", "Voc": "41.57", "Isc":"11.22","model":"LG Mono X Plus","Vmp":"33.82","panelSerial":"LG365S1C-U6","Url":"https://www.lgenergy.com.au/uploads/download_files/46110da0092b6cdf8feb6e84097201751420b38a.pdf"},
"LG370M": {"P":"370", "Voc": "41.72", "Isc":"11.32","model":"LG Mono X Plus","Vmp":"33.95","panelSerial":"LG370S1C-U6","Url":"https://www.lgenergy.com.au/uploads/download_files/46110da0092b6cdf8feb6e84097201751420b38a.pdf"}
}


lg_dict = {
"LG NeON":lg_neon_dict,
"LG MonoX":lg_monox_dict,
}

qmax_g2_dict = {
"Q350" : {"P":"350", "Voc": "40.7", "Isc":"10.74","model":"Q.MAXX-G2","Vmp":"34.24","panelSerial":"","Url":"https://www.q-cells.com/au/main/customer_support/download/datasheets.html"}
}


qcells_dict = {
"Q.MAXX-G2": qmax_g2_dict
}

panel_dict = {
  "LG Electronics":lg_dict,
  "Q Cells":qcells_dict
}

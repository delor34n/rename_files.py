# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
	wena compare
"""

import os
import sys
import argparse
import json
import calendar
from dateutil.parser import parse
from shutil import copyfile

__FILE_DIR__ = "input"
__RENAMED_FILE_DIR__ = "output"
MONTHS_MAPPER = {1: 'Enero', 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile_2015', help="Input file 2015", type=argparse.FileType('r'))
    parser.add_argument('infile_2016', help="Input file 2016", type=argparse.FileType('r'))

    args = parser.parse_args(arguments)
    data_2015 = json.load(args.infile_2015)
    data_2016 = json.load(args.infile_2016)

    check_data(data_2015)
    check_data(data_2016)

def check_data(data):
	for d in data:
		upload_date = parse(d['fecha subida'])
		year = int(upload_date.strftime('%Y'))
		month = int(upload_date.strftime('%m'))
		day = int(upload_date.strftime('%d'))
		file_name = d['nombre archivo']
		__PATH__ = "%s/%s/%s/%02d-%02d-%02d" % (__FILE_DIR__, year, MONTHS_MAPPER[month], day, month, year)

		# EXISTE EL DIRECTORIO ?
		if os.path.isdir(__PATH__):
			print "%s/%s" % (__PATH__, file_name)
			# EXISTE EL ARCHIVO ?
			if os.path.isfile("%s/%s" % (__PATH__, file_name)):
				__OUTPUT_PATH__ = "%s/%s/%s" % (__RENAMED_FILE_DIR__, year, MONTHS_MAPPER[month])
				src = "%s/%s" % (__PATH__, file_name)
				dst = "%s/%s" % (__OUTPUT_PATH__, d['hash'])
				rename_file(src, dst, __OUTPUT_PATH__)
				return
			else:
				print "404 - FILE NOT FOUND"
		else:
			print False

def rename_file(src, dst, __OUTPUT_PATH__):
	# NO EXISTE EL DIRECTORIO DE SALIDA (PARA ARCHIVOS RENOMBRADOS) ?
	if not os.path.isdir(__OUTPUT_PATH__):
		os.makedirs(__OUTPUT_PATH__)
	# COPIA ARCHIVO
	copyfile(src, dst)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


from questions import *
from quality_check_interfaces import *
from latex import *
from os_upgrade import *
import subprocess

engineer_name = get_engineer()

date = get_date()

equipment_manufacturer = get_brand()

os = get_os_upgrade(equipment_manufacturer, 9)

upgrade_os(equipment_manufacturer, os)
equipment_model = get_equipment_model()

serial_num = get_serial_number()

manufacturer_specs_url = get_device_specifications()

burn_in_time = get_burn_in_duration()

inventory_check = get_inventory()

damage_assement = get_damage_assesment()

# Quality checks
total_interface_count = get_num_of_interfaces()


interface_percentage = check_interfaces(total_interface_count, equipment_manufacturer)



# Write to LaTex
texfile = 'test.tex'
f = open(texfile, 'w')
f.write(begin)
f.write(set_title(engineer_name, date))
f.write(set_equipment_info(equipment_manufacturer, equipment_model, serial_num))
f.write(set_manufacturer_specs_url(manufacturer_specs_url))
f.write(set_quality_checks_table(os, damage_assement, total_interface_count * (interface_percentage / 100), interface_percentage, burn_in_time, inventory_check))
f.write(end_document())
f.close()


#generate PDF
proc = subprocess.Popen(['pdflatex', texfile])
proc.communicate()

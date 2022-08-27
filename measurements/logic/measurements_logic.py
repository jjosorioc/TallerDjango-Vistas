from datetime import datetime
from ..models import Measurement
from variables.logic import variables_logic as vl

def get_measurements():
    return Measurement.objects.all()

def get_measurement(id):
    return Measurement.objects.get(pk=id)

def update_measurement(var_pk, new_measurement):
    measurement = get_measurement(var_pk)
    measurement.value = new_measurement['value']
    measurement.save()
    return measurement

def create_measurement(mes) -> Measurement:
    measurement = Measurement(
        variable = vl.get_variable(mes['variable']),
        value=mes['value'],
        unit=mes['unit'],
        place=mes['place'],
        dateTime=mes["dateTime"]
    )
    measurement.save()
    return measurement

def delete_measurement(id):
    measurement = get_measurement(id)
    measurement.delete()
    return measurement
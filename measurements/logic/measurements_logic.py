from ..models import Measurement

def get_measurements():
    return Measurement.objects.all()

def get_measurement(id):
    return Measurement.objects.get(pk=id)

def update_measurement(var_pk, new_measurement):
    measurement = get_measurement(var_pk)
    measurement.name = new_measurement['name']
    measurement.save()
    return measurement

def create_measurement(mes) -> Measurement:
    measurement = Measurement(value=mes['value'])
    measurement.save()
    return measurement

def delete_measurement(id):
    measurement = get_measurement(id)
    measurement.delete()
    return measurement
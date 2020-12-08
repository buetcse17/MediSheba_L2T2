import cx_Oracle
from django.db import models


# Create your models here.

class DoctorName:

    def __init__(self, id, name, phone, gender, specialization, location, hospital_id, doctor_id):
        hospital_full_name = ""

        if hospital_id != -1:
            dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
            conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
            c = conn.cursor()
            c.execute("SELECT HOSPITAL_NAME FROM MEDI_SHEBA.HOSPITAL WHERE HOSPITAL_ID = " + str(hospital_id))
            for row in c:
                hospital_full_name = row[0]
        else:
            hospital_full_name = "NONE"

        self.id = id
        self.name = name
        self.phone = phone
        self.gender = gender
        self.specialization = specialization
        self.location = location
        self.hospital_name = hospital_full_name
        self.doctor_id = doctor_id


class HospitalCabinName:

    def __init__(self, id, name, location, available_cabin, hospital_id):
        self.id = id
        self.name = name
        self.location = location
        self.available_cabin = available_cabin
        self.hospital_id = hospital_id

class CabinName:

    def __init__(self, id, price, category,  cabin_id):
        self.id = id
        self.price = price
        self.category = category
        self.cabin_id = cabin_id


class BloodBankList:

    def __init__(self, id, name,a_plus, a_minus, b_plus, b_minus, o_plus, o_minus, ab_plus, ab_minus,blood_bank_id,location):
        self.id = id
        self.blood_bank_id=blood_bank_id
        self.name = name
        self.location=location
        self.a_plus = a_plus
        self.a_minus = a_minus
        self.b_plus = b_plus
        self.b_minus = b_minus
        self.o_plus = o_plus
        self.o_minus = o_minus
        self.ab_plus = ab_plus
        self.ab_minus = ab_minus


class HospitalName:

    def __init__(self, id, name, phone, location, hospital_id):
        self.id = id
        self.name = name
        self.phone = phone
        self.location = location
        self.hospital_id = hospital_id


class doctor_infos:
    def __init__(self,first_name, last_name, phone, email, hospital_id, fees, specialization):
        hospital_full_name = ""
        if hospital_id != -1:
            dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='ORCL')
            conn = cx_Oracle.connect(user='MEDI_SHEBA', password='1234', dsn=dsn_tns)
            c = conn.cursor()
            c.execute("SELECT HOSPITAL_NAME FROM MEDI_SHEBA.HOSPITAL WHERE HOSPITAL_ID = " + str(hospital_id))
            for row in c:
                hospital_full_name = row[0]
        else:
            hospital_full_name = "NONE"
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.hospital_name = hospital_full_name
        self.fees = fees
        self.specialization = specialization

class UserAppointment_in_blood_bank:

    def __init__(self, id, name, blood_group, amount):
        self.id = id
        self.name=name
        self.blood_group=blood_group
        self.amount=amount

class userCabinHistory:
    def __init__(self, id, cabin_id, user_id, hospital_name, entry_date, exit_date, user_type):
        self.id = id
        self.cabin_id = cabin_id
        self.user_id = user_id
        self.hospital_name = hospital_name
        self.entry_date = entry_date
        self.exit_date= exit_date
        self.user_type = user_type

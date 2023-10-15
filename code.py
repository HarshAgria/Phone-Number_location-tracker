import phonenumbers
from phonenumbers import timezone,geocoder,carrier

number=input("Enter Your NO. With +__: ")

try:
    phone=phonenumbers.parse(number)
    if not phonenumbers.is_valid_number(phone):
        print("Invalid phone number")
    else:
        time=timezone.time_zones_for_number(phone)
        car=carrier.name_for_number(phone,"en")
        # reg=geocoder.description_for_number(phone,"en")
        geo = geocoder.description_for_number(phone, "en")
        reg = geo.split(", ")[-1] if geo else "Unknown Region"
    
    print("Phone no. :",phone)
    print("Time zone: ",time)
    print("Carrier: ",car)
    print("Region: ",reg)

except phonenumbers.NumberParseException as e:
    print("Error: ",e)


''' To show available info '''


def set_personal_info(data=None):
    if data is None:
        data = {'First name': 'Gregory', 'Last Name': 'House', 'Birth year': '1959',
                'City of residence': 'Princeton', 'E-mail': 'greg@plainsboro.com', 'Phone number': '777 1234'}
    print('\nPersonal data:')
    for x, y in data.items():
        print('{}: {}'.format(x, y.title()), end='; ')


p_data = {'First name': '', 'Last Name': '', 'Birth year': '', 'City of residence': '', 'E-mail': '',
          'Phone number': ''}
for i in p_data.keys():
    p_data[i] = input('Enter {}: '.format(i))
set_personal_info(p_data)
set_personal_info()


'''I don't like following solution:'''

'''def set_personal_info(f_name='First_Name_Undefined', l_name='Last_Name_Undefined', y_birth='Birth_Year_Undefined',
                      city='Residence_City_Undefined', email='E-Mail_Undefined', phone='Phone_Number_Undefined'):
    sub, res = [f_name, l_name, y_birth, city, email, phone], ''
    for i in sub:
        res += str(i)
        res += ' '

    return res


while True:
    fi_name = input('Enter first name: ')
    if fi_name.isalpha() and len(fi_name.strip()) > 0:
        break
while True:
    la_name = input('Enter last name: ')
    if la_name.isalpha() and len(la_name.strip()) > 0:
        break
while True:
    ye_birth = input('Enter year of birth: ')
    if ye_birth.isdigit() and 1900 < int(ye_birth) < 2020:
        break
while True:
    _city = input('Enter residence city: ')
    if _city.isalpha() and len(_city.strip()) > 0:
        break
while True:
    e_mail = input('Enter e-mail: ')
    if len(e_mail.strip()) > 0:
        break
while True:
    phone_n = input('Enter phone number: ')
    if phone_n.isdigit():
        break

print(set_personal_info(fi_name, la_name, ye_birth, _city, e_mail, phone_n))'''

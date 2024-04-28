year = int(input('Nhập năm: '))
def calculate_can_chi_calendar(year):
  result = ''
  can_lst = ['Canh','Tân','Nhâm','Quý','Giáp','Ất','Bính','Đinh','Mậu','Kỷ']
  chi_lst = ['Thân','Dậu','Tuất','Hợi','Tý','Sửu','Dần','Mão','Thìn','Tỵ','Ngọ',
           'Mùi']
  mod_can = year%10
  mod_chi = year%12
  result = can_lst[mod_can] + ' ' + chi_lst[mod_chi]
  return result

# Test_case
print(calculate_can_chi_calendar(year))
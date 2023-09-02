import datetime
def main():
    name=str('Abdo Mostafa')
    age=int(25)
    today=datetime.datetime.today()
    degree=float(2.9)
    speciality=str('Computer Engineering')
    print(f'My name is {name},',
          f'I am {age} years old,',
          f'My Degree is {degree}/4.0 in {speciality} and',
          f'the time now is {today:%A %B %d, %Y}',sep="\n" )
    
main()
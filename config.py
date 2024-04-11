DATABASE = 'db.db'
TOKEN = '6077941896:AAFVHEWTP-OMpv6F7O9jjnNUcG_OBt0Uk0I'
ANSWER = "КОТИК НА ЧЕМОДАНЕ"
ANSWER_BONUS = 'ЛЕТИТ НА БАЛИ'

s1 = ['ТИ', 'О', 'К', 'К']
s2 = ['А', 'О', 'АН', 'Е', 'Н', 'Д', 'М', 'ЧЕ']
s3 = ['ТИ', 'ЛЕ', 'ТНАБ', 'АЛИ']
ANSWER_LIST = s1+s2+s3


ANSWER_DICT = {
    (1,4) : "КОТИК",
    (5,12) : "НА ЧЕМОДАНЕ",
    (13, 16): "ЛЕТИТ НА БАЛИ"
}

QUESTIONS_INFO = [
        {
            'list' : list(range(1,5)),
            'key' : "КОТИК",
            'bonus' : 15

        },
        {
            'list' : list(range(5,13)),
            'key' : "НА ЧЕМОДАНЕ",
            'bonus' : 30
        },
        {
            'list' : list(range(13,16)),
            'key' : "ЛЕТИТ НА БАЛИ",
            'bonus' : 60
        }
]
 

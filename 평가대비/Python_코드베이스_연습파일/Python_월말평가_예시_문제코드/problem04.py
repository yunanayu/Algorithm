def is_id_valid(user_data):
    # 여기에 코드를 작성합니다.
    value_data = list(user_data.values())
    list_id = list(value_data[0])
    len_id = list_id[len(list_id) - 1]
    if len_id.isdigit():
        if 0 < int(len_id) < 9:
            return True
    else:
        return False  

if __name__ == '__main__':
    # 아래의 코드는 수정하지 않습니다.
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False
    # 아래 부터 추가 예제 코드 작성 가능합니다.
    

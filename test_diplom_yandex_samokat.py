# Алёна Варовина, 29-я когорта - финальный проект. Инженер по тестированию расширенный.
import sender_stand_request

def test_get_order_info_by_track():
    response_create_order = sender_stand_request.post_new_order()
    
    assert response_create_order.status_code == 201
    
    track = response_create_order.json().get('track')
    
    response_get_order_info = sender_stand_request.get_order_info(track)
    
    assert response_get_order_info.status_code == 200

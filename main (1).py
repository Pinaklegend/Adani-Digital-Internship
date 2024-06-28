import duplication
import time 
import sys

s= time.time()

url_list = [
#     "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/10_Guest_Lounge_new_B1cQUD.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/11_Guest_Lounge_new_D0BBdV.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/ginger-goa_C37mIC.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Guest_Coridoor_L3Hy50.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/08_Cafe_Et_Cetera_new__r0cTeW.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/08a_Cafe_Et_Cetera_new__9rzEVu.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/proper-hotel-in-panjim_aawu2J.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Luxe_Single_Room_OI7miG.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Luxe_Single_Room1_ojJk9C.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/gym_6yyTGw.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/luxe-room_(1)_2W9Xx2.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/luxe-room_qrO2Xw.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/04a_Luxe_room_88XXfe.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/06_Shower_Area_v0Wekx.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Bath_Amenities_ipRe54.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/03_Reimagined_spaces_New_EBlkBG.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/07_Cafe_Et_Cetera_Swing_Bench_new_EdscXE.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/05_Luxe_Room_Twin_Bed_new_mNoQxT.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/02_Reimagined_Spaces_XW0K4K.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Ginger_Goa_Panaji_reception_y01yaU.jpg",
# "https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/04_Luxe_Room_angle2_gOJanu.jpg",
"https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/04a_Luxe_room_88XXfe.jpg",
"https://fastui.cltpstatic.com/image/upload/hotels/places/hotels/cms/8109/81094/images/Luxe_Single_Room_OI7miG.jpg"
]
obj = duplication.find_duplicates(url_list)
obj.embeddings()
output = obj.clustering()

# for k, v in output.items():
#     print(f'{k} - {v}')


print(f'Completed in {time.time() - s} seconds')
sys.stdout.write(str(output))



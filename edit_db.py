# import firebase as fb
#
# import hotels_db
# import restaurants_db
# import museums_db
# import beaches_db
# import cinemas_db
# import parks_db
# import places_db
#
# # removing all cities
# fb.db.child('Cities').child('Ashdod').remove()
# fb.db.child("Cities").child('Arad').remove()
# fb.db.child('Cities').child('Bat Yam').remove()
# fb.db.child("Cities").child('Beer Sheva').remove()
# fb.db.child('Cities').child('Eilat').remove()
# fb.db.child('Cities').child('Jerusalem').remove()
# fb.db.child('Cities').child('Netanya').remove()
# fb.db.child('Cities').child('Ramat Gan').remove()
# fb.db.child('Cities').child('Tel Aviv').remove()
# fb.db.child('Cities').child('Tsfat').remove()
# fb.db.child('Cities').child('Tveria').remove()
# fb.db.child('Cities').child('Haifa').remove()
#
# # hotels
# fb.db.child('Cities').child('Jerusalem').child('Hotels').update(hotels_db.jerusalem)
# fb.db.child('Cities').child('Tel Aviv').child('Hotels').update(hotels_db.tel_aviv)
# fb.db.child('Cities').child('Ashdod').child('Hotels').update(hotels_db.ashdod)
# fb.db.child('Cities').child('Netanya').child('Hotels').update(hotels_db.netanya)
# fb.db.child('Cities').child('Tveria').child('Hotels').update(hotels_db.tveria)
# fb.db.child('Cities').child('Beer Sheva').child('Hotels').update(hotels_db.beer_sheva)
# fb.db.child('Cities').child('Ramat Gan').child('Hotels').update(hotels_db.ramat_gan)
# fb.db.child('Cities').child('Tsfat').child('Hotels').update(hotels_db.tsfat)
# fb.db.child('Cities').child('Arad').child('Hotels').update(hotels_db.arad)
# fb.db.child('Cities').child('Bat Yam').child('Hotels').update(hotels_db.bat_yam)
# fb.db.child('Cities').child('Eilat').child('Hotels').update(hotels_db.eilat)
# fb.db.child('Cities').child('Haifa').child('Hotels').update(hotels_db.haifa)
#
# # restaurants
# fb.db.child('Cities').child('Ashdod').child('Restaurants').update(restaurants_db.ashdod)
# fb.db.child("Cities").child('Arad').child('Restaurants').update(restaurants_db.arad)
# fb.db.child('Cities').child('Bat Yam').child('Restaurants').update(restaurants_db.bat_yam)
# fb.db.child('Cities').child('Beer Sheva').child('Restaurants').update(restaurants_db.beer_sheva)
# fb.db.child('Cities').child('Eilat').child('Restaurants').update(restaurants_db.eilat)
# fb.db.child('Cities').child('Jerusalem').child('Restaurants').update(restaurants_db.jerusalem)
# fb.db.child('Cities').child('Netanya').child('Restaurants').update(restaurants_db.netanya)
# fb.db.child('Cities').child('Ramat Gan').child('Restaurants').update(restaurants_db.ramat_gan)
# fb.db.child('Cities').child('Tel Aviv').child('Restaurants').update(restaurants_db.tel_aviv)
# fb.db.child('Cities').child('Tsfat').child('Restaurants').update(restaurants_db.tsfat)
# fb.db.child('Cities').child('Tveria').child('Restaurants').update(restaurants_db.tveria)
# fb.db.child('Cities').child('Haifa').child('Restaurants').update(restaurants_db.haifa)
#
# # museums
# fb.db.child('Cities').child('Ashdod').child('Museums').update(museums_db.ashdod)
# fb.db.child('Cities').child('Arad').child('Museums').update(museums_db.arad)
# fb.db.child('Cities').child('Beer Sheva').child('Museums').update(museums_db.beer_sheva)
# fb.db.child('Cities').child('Eilat').child('Museums').update(museums_db.eilat)
# fb.db.child('Cities').child('Jerusalem').child('Museums').update(museums_db.jerusalem)
# fb.db.child('Cities').child('Netanya').child('Museums').update(museums_db.netanya)
# fb.db.child('Cities').child('Tel Aviv').child('Museums').update(museums_db.tel_aviv)
# fb.db.child('Cities').child('Tsfat').child('Museums').update(museums_db.tsfat)
# fb.db.child('Cities').child('Tveria').child('Museums').update(museums_db.tveria)
# fb.db.child('Cities').child('Haifa').child('Museums').update(museums_db.haifa)
#
# # beaches
# fb.db.child('Cities').child('Ashdod').child('Beaches').update(beaches_db.ashdod)
# fb.db.child('Cities').child('Bat Yam').child('Beaches').update(beaches_db.bat_yam)
# fb.db.child('Cities').child('Eilat').child('Beaches').update(beaches_db.eilat)
# fb.db.child('Cities').child('Netanya').child('Beaches').update(beaches_db.netanya)
# fb.db.child('Cities').child('Tel Aviv').child('Beaches').update(beaches_db.tel_aviv)
# fb.db.child('Cities').child('Tveria').child('Beaches').update(beaches_db.tveria)
# fb.db.child('Cities').child('Haifa').child('Beaches').update(beaches_db.haifa)
#
# # cinemas
# fb.db.child('Cities').child('Ashdod').child('Cinemas').update(cinemas_db.ashdod)
# fb.db.child('Cities').child('Beer Sheva').child('Cinemas').update(cinemas_db.beer_sheva)
# fb.db.child('Cities').child('Jerusalem').child('Cinemas').update(cinemas_db.jerusalem)
# fb.db.child('Cities').child('Netanya').child('Cinemas').update(cinemas_db.netanya)
# fb.db.child('Cities').child('Tel Aviv').child('Cinemas').update(cinemas_db.tel_aviv)
# fb.db.child('Cities').child('Haifa').child('Cinemas').update(cinemas_db.haifa)
#
# # parks
# fb.db.child('Cities').child('Ashdod').child('Parks').update(parks_db.ashdod)
# fb.db.child("Cities").child('Arad').child('Parks').update(parks_db.arad)
# fb.db.child('Cities').child('Beer Sheva').child('Parks').update(parks_db.beer_sheva)
# fb.db.child('Cities').child('Eilat').child('Parks').update(parks_db.eilat)
# fb.db.child('Cities').child('Jerusalem').child('Parks').update(parks_db.jerusalem)
# fb.db.child('Cities').child('Netanya').child('Parks').update(parks_db.netanya)
# fb.db.child('Cities').child('Ramat Gan').child('Parks').update(parks_db.ramat_gan)
# fb.db.child('Cities').child('Tel Aviv').child('Parks').update(parks_db.tel_aviv)
# fb.db.child('Cities').child('Tsfat').child('Parks').update(parks_db.tsfat)
# fb.db.child('Cities').child('Tveria').child('Parks').update(parks_db.tveria)
# fb.db.child('Cities').child('Haifa').child('Parks').update(parks_db.haifa)
#
# # places
# fb.db.child('Cities').child('Ashdod').child('Attractions').update(places_db.ashdod)
# fb.db.child("Cities").child('Arad').child('Attractions').update(places_db.arad)
# fb.db.child('Cities').child('Bat Yam').child('Attractions').update(places_db.bat_yam)
# fb.db.child('Cities').child('Beer Sheva').child('Attractions').update(places_db.beer_sheva)
# fb.db.child('Cities').child('Eilat').child('Attractions').update(places_db.eilat)
# fb.db.child('Cities').child('Jerusalem').child('Attractions').update(places_db.jerusalem)
# fb.db.child('Cities').child('Netanya').child('Attractions').update(places_db.netanya)
# fb.db.child('Cities').child('Ramat Gan').child('Attractions').update(places_db.ramat_gan)
# fb.db.child('Cities').child('Tel Aviv').child('Attractions').update(places_db.tel_aviv)
# fb.db.child('Cities').child('Tsfat').child('Attractions').update(places_db.tsfat)
# fb.db.child('Cities').child('Tveria').child('Attractions').update(places_db.tveria)
# fb.db.child('Cities').child('Haifa').child('Attractions').update(places_db.haifa)

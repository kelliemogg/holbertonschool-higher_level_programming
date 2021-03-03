-- Lists all the cities of California that can be found in hbtn_0d_usa
SELECT id FROM cities WHERE state_id = 'California' ORDER BY cities.id ASC;

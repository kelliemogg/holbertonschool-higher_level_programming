-- Lists all the cities of California that can be found in hbtn_0d_usa
SELECT id FROM states WHERE NOT EXISTS (
       SELECT * FROM cities
       WHERE cities.state_id = states.id ORDER BY cities.id ASC);

from flask import Flask
import mariadb
import json

app = Flask(__name__)

# Database connection configuration
db_connection = mariadb.connect(
    user='root',
    password='password',
    host='localhost',
    port=3306,
    database='flask_animals'
)
cursor = db_connection.cursor()

@app.route('/animals', methods=['GET'])
def get_all_animals():
    cursor.execute("SELECT name, species FROM animal")
    animals = cursor.fetchall()
    animal_list = [{'name': name, 'species': species} for name, species in animals]
    json_data = json.dumps(animal_list)
    return json_data

@app.route('/dogs', methods=['GET'])
def get_dogs():
    cursor.execute("SELECT name FROM animal WHERE species='dog'")
    dogs = cursor.fetchall()
    dog_list = [dog[0] for dog in dogs]
    json_data = json.dumps(dog_list)
    return json_data

@app.route('/cats', methods=['GET'])
def get_cats():
    cursor.execute("SELECT name FROM animal WHERE species='cat'")
    cats = cursor.fetchall()
    cat_list = [cat[0] for cat in cats]
    json_data = json.dumps(cat_list)
    return json_data

if __name__ == '__main__':
    app.run()

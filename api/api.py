

print("Teste de API");

config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'apijao'
    }
connection = mysql.connector.connect(**config)

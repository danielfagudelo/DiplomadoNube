import boto3

#Crear un elemento para dynamodb
dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1')

tabla = dynamodb.Table('tabla-daniel-agudelo')

#Leer un elemento de la tabla
response = tabla.get_item(Key={'id': '2'})

print(response['Item'])

#leer todos los elementos de la tabla
response = tabla.scan()

#print(response['Item'])

#crear un registro en la tabla
new_item = {
    "id":"3",
    "nombre":"tulio",
    "Ciudad":"cali"
}

tabla.put_item(Item = new_item)

print("elemento antes de actualizar", response['Items'] )

#actualizar un elemento
response = table.update_item(
    Key={
        'id': "1"
    },
UpdateExpression='SET Ciudad = :var1',
    ExpressionAttributeNames={
        ':var1': 'pereira'
    },

print("elemento despues de actualizar", response['Items'] )

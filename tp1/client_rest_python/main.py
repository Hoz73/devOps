import requests
from requests import Response


#http://server/ for comunication between 2 pods in k8s
#http://server:5000/ for comunication between two docker images/containers

def calling_api(get_name: str, params=None, put=None, delete=None, post=None) -> Response:
    if put:
        response: Response = requests.put(f'http://server/{get_name}', json=params)
    elif post:
        response: Response = requests.post(f'http://server/{get_name}', json=params)
    elif delete:
        response: Response = requests.delete(f'http://server/{get_name}')
    else:
        response: Response = requests.get(f'http://server/{get_name}')
    return response


if __name__ == '__main__':
    end = False
    while not end:
        services = {
            1: 'hello',
            2: 'product/getProducts',
            3: 'product/getProduct',
            4: 'product/updateProduct',
            5: 'product/addProduct',
            6: 'product/removeProduct',
            7: 'end'
        }
        print('Voici la liste des service ques vous pouvez appeler :\n'
              '1 - Hello\n'
              '2 - Get all products\n'
              '3 - Get a product\n'
              '4 - Update a product\n'
              '5 - Add a product\n'
              '6 - Delete a product\n'
              '7 - Exit\n'
              'Choisissez le numéro du service voulu :')
        choice = input()
        try:
            choice = int(choice)
            if len(services) < choice:
                print(f'the service {choice} does not exist')
            else:
                if choice == 7:
                    end = True
                elif choice == 3:
                    name = input('name: ')
                    res = calling_api(f'{services[choice]}/{name}')
                elif choice == 6:
                    name = input('name: ')
                    res = calling_api(f'{services[choice]}/{name}', delete=True)
                elif choice == 4:
                    name = input('name: ')
                    new_name = input('new name : ')
                    res = calling_api(f'{services[choice]}/{name}', params={'name': new_name}, put=True)
                elif choice == 5:
                    id = input('id : ')
                    name = input('name: ')
                    section = input('section : ')
                    product = {
                        'id': id,
                        'name': name,
                        'section': section
                    }
                    res = calling_api(services[choice], product, post=True)
                else:
                    res = calling_api(services[choice])

                if not end: print(res.content)
        except ValueError:
            print("error, not a valid character")

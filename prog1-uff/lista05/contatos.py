contact = {
    'name': str(input('Digite o nome da pessoa: ')),
    'age': int(input('Digite a idade da pessoa: ')),
    'gender': str(input('Digite o sexo da pessoa (m ou f): '))
}

contact['phone number'] = []
contact['social media'] = []

option = 0
while option != 6:
    print('-=' * 30)
    option = int(input('1- Mostrar todos os dados da pessoa.\n2- Acrescentar um número de telefone.\n3- Remover um número de telefone.\n4- Acrescentar uma rede social (nome da rede e @ da pessoa).\n5- Remover uma rede social (pelo nome da rede).\n6- Encerrar o programa.\nEscolha uma opção: '))
    match option:
        case 1:
            print('-=' * 30)
            print(contact)
        case 2:
            print('-=' * 30)
            newPhoneNumber = int(input('Digite o número de telefone: '))
            contact['phone number'].append(newPhoneNumber)
        case 3:
            print('-=' * 30)
            print(f'Esse contato possui {len(contact['phone number'])} números')
            for i in range(len(contact['phone number'])):
                print(f'{i+1} para o excluir o {i+1}°')
            excludePhoneNumber = int(input('Digite o número que deseja excluir: '))
            contact['phone number'].pop(excludePhoneNumber - 1)
        case 4:
            print('-=' * 30)
            newSocialMedia = {
                'name': str(input('Digite o nome da rede social: ')),
                '@': str(input('Digite o @ da pessoa: '))
            }
            contact['social media'].append(newSocialMedia)
        case 5:
            print('-=' * 30)
            excludeSocialMedia = str(input('Digite o nome da rede social que você deseja excluir: '))
            for i in range(len(contact['social media'])):
                if excludeSocialMedia == contact['social media'][i]['name']:
                    contact['social media'].pop(i)
                    break
        case 6:
            break
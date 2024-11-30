#START do sistema
print("\n---Cadastro de clientes---\n")

#Cadastro do cliente
nome = input("Informe o nome do cliente: ")
telefone = int(input("Informe o telefone do cliente: "))
email = input("Informe o e-mail do cliente: ")
saldo = float(input("Informe o saldo total que o cliente tem disponível: "))

# Criação da tabela_FIPE
tabela_FIPE = {

    "Volvo FMX": 234.5678, "Volvo FH": 456.7892,  "WESTERN STAR 49X": 40.000, # Caminhão Volvo
    "AeroStar": 56.897645, "HX": 4.567892, "International LT": 56.789123, # Caminhão Navistar 
    "VW 17-280": 286.000, "Volkswagen Delivery 11.180": 45.000, "VW 26260": 20.000, # Caminhão Volkswagen
    "Super-Liner - década de 1980": 5.97435000, "Mack Anthem": 18.000, "Mack MD": 32.000,  #Mack Trucks
    "Western Star 5700 XE Phantom": 13.4595, "WESTERN STAR 57X": 12.467, "WESTERN STAR 49X": 25.500 # Caminhão Western Star
}

# Lista para verificar se tem disponível
veiculos_disponiveis = {
    "Volvo": ["Volvo FMX", "Volvo FH" "WESTERN STAR 49X"],
    "Navistar": ["AeroStar", "HX", "International LT"],
    "Volkswagen": ["VW 17-280", "Volkswagen Delivery 11.180", "VW 26260"],
    "Mack Trucks": [ "Super-Liner - década de 1980", "Mack Anthem", "Mack MD"],
    "Wastern Star": ["Western Star 5700 XE Phantom", "WESTERN STAR 57X", "WESTERN STAR 49X"]
}


# Looping para menu de opções.
while True:


    print("\n---CAPOTARIA DO SEU ZÉ---\n")
    print("\n--- TABELA DE OPÇÕES ---\n")
    print("1. Vender Veículo. \n2. Alugar Veículo. \n3.Comprar Veículo. \n4.Sair do sistema.")
    escolha = int(input("Escolha uma opção: "))

    # Sistema para as vendas dos caminhões.
    if escolha == 1:
        print("\n---VENDAS DOS CAMINHÕES---\n")

         # FOR para a verificação da existência da marca do veículo
        for marca_veiculo in veiculos_disponiveis:
            print(marca_veiculo)
        
        marca_veiculo = input("Escolha uma marca: ")
        # FOR para verificar a existência do modelo do veículo
        for modelo in tabela_FIPE:
            print(veiculos_disponiveis[marca_veiculo])
            modelo = input("Escolha um modelo: ")

            desconto_doze = tabela_FIPE[modelo] * 0.12
            proposta = tabela_FIPE[modelo] - desconto_doze

            print(f"\nA proposta para o veículo será de R${proposta:.2f}")
            finalizarproposta = input("Deseja finalizar o negocio de acordo com a proposta [S/N]: ").lower()
            
        # If para confirmarção de venda
        if finalizarproposta == "s":
            saldo_cliente = proposta + saldo

            print(f"Compra realizada com sucesso, saldo disponivel do cliente é R${saldo_cliente}")
            
        # Else utilizado para (NÃO) venda do veículo
        else:
            print("Negócio cancelado")

    # If para a opção 2.
    if escolha == 2:
        print("---ALUGUEL DE CAMINHÃO---")

        for modelo in tabela_FIPE:
             taxa_fipe = tabela_FIPE[modelo] * 0.25
        valor_venda = tabela_FIPE[modelo] + taxa_fipe

        print(f"O caminhão desejado {marca_veiculo} {modelo} no valor de R${valor_venda}")

        finalizar_compra = input("Deseja finalizar compra (S/N): ").lower()
          
          # If usado para confirmar a compra.
        if finalizar_compra == "s":
             
             # If para verificar o saldo.
           if saldo < valor_venda:
            print("Saldo insuficiente")
            
            #Else para verificar o se o saldo é suficiente ou insuficiente.
           else:
              saldocliente = saldo - valor_venda
              print(f"Venda realizado com sucesso, saldo do cliente é de: R${saldocliente}")
              veiculos_disponiveis[marca_veiculo].remove(modelo)
              
           #Else para o cancelamento de negociação.
        else:
              print("Negociação cancelada, obrigado por utilizar dos nossos serviços!!!")
      
      #ELse para veículo NÃO disponível.
    else:
       print("Caminhão já vendido, selecione outro disponível!")
       continue
  
    #IF para a opção 3.
    if escolha == 3:
        print("---COMPRA DE CAMINHÃO---")
        
        #FOR utilizado para verificar se o veículo está na tabela
        for marca_veiculo in veiculos_disponiveis:
            print(marca_veiculo)
        
        marca_veiculo = input("Escolha uma marca: ")
        
        print(veiculos_disponiveis[marca_veiculo])
        modelo = input("Escolha um modelo: ")

        diaria = int(input("Insira quantos dias deseja alugar o carro: "))

        # If é utilizado para verificar a disponibilidade do veículo.
        if modelo in veiculos_disponiveis[marca_veiculo]:
        
            valoraluguel = 77 * diaria

            print(f"O caminhão desejado {marca_veiculo} {modelo}, o valor de locação será de R${valoraluguel}")

            finalizar_aluguel = input("Deseja finalizar o pedido para alugar o caminhão [S/N]: ").lower()
            
            #If usado para confirmar a venda do veículo.
            if finalizar_aluguel == "s":
                
                #If para verificar o saldo.
                if saldo < valoraluguel:
                        print("Saldo insuficiente")
    
                # Else para verificação de saldo suficiente ou insuficiente.
                else:
                    saldocliente = saldo - valoraluguel
                    print(f"Caminhão alugado com sucesso, saldo do cliente é de: R${saldocliente}")
                    veiculos_disponiveis[marca_veiculo].remove(modelo)
                
            # Else para a NÃO venda de veículo.
            else:
                print("Negóciação cancelada, obrigado por utilizar dos nossos serviços!!!")
        
        # Else usado para verificar se o veículo está ou não disponível.
        else:
            print("Caminhão já alugado, selecione outro disponível!")

    #FINALIZAÇÃO DO SISTEMA
    if escolha == 4:
        print("Encerrando Sistema...Pé na estrada, cabeça erguida e foco no destino!!!!!")

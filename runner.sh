#!/bin/bash

echo "Escolha a opção:"
echo "1 - Perfil de Teste"
echo "0 - Perfil de Desenvolvimento"
read -n 1 choice

case $choice in
    1)
        FILE="docker-compose.test.yaml"
        ENV="test.env"
        ;;
    0)
        FILE="docker-compose.dev.yaml"
        ENV="dev.env"
        ;;
    *)
        echo "Opção inválida."
        exit 1
        ;;
esac

docker compose -f "$FILE" --env-file "$ENV" up --build

echo "Digite a tecla Q para parar os serviços..."
while : ; do
    read -n 1 k <&1
    if [[ $k = q ]] ; then
        break
    fi
done

docker compose -f "$FILE" down

echo "Serviços encerrados."

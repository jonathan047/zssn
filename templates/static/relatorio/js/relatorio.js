function dados_sobrevivente(){
    sobrevivente = document.getElementById('sobrevivente-select')
    csrf_token = document.querrySelector('[name=csrf_tokenfmiddlewaretoken]').value
    id_sobrevivente = sobrevivente.value
    data = new FormData()
    data.append('id_cliente', id_cliente)
    fetch("/sobreviventes/atualiza_sobreviventes/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrf_token,
        },
        body: data
        
    }).then(function(result){
        return result.json()
    }).then(funtion(data){
        
        colosel.log('teste')
    })
}
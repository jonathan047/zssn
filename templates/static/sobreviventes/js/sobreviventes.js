function add_item(){
    container = document.getElementById("form-item")
    
    html = "<br><div class='row'> <div class='col-md'><input type='text' placeholder='Item' class='form-control' name='item'></div><div class='col-md'><input type='number' placeholder='Quant.' class='form-control' name='quant'></div></div>"
    
    container.innerHTML  += html
}

function exibir_form(tipo){
    add_sobrevivente = document.getElementById('Adicionar-sobrevivente')
    att_sobrevivente = document.getElementById('att_sobrevivente')
    
    if(tipo == "1"){
        att_sobrevivente.style.display = "none"
        add_sobrevivente.style.display = "block"
    
    }else if(tipo == "2"){
        att_sobrevivente.style.display = "block"
        add_sobrevivente.style.display = "none"
    }
}

function dados_sobrevivente(){
    sobrevivente = document.getElementById('sobrevivente-select')
    csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value
    
    id_sobrevivente = sobrevivente.value
    data = new FormData()
    data.append('id_sobrevivente', id_sobrevivente)
    
    fetch("/sobreviventes/atualiza_sobrevivente/",{
        method: "POST",
        headers: {
            'X-CSRFToken': csrf_token, 
        },
        body: data
    }).then(function(result){
        return result.json()
    }).then(function(data){
        
        document.getElementById('form-att-sobrevivente').style.display = 'block'
        
        id = document.getElementById('id')
        id.value = data['cliente_id']
        
        nome = document.getElementById('nome')
        nome.value = data['nome']
        
        idade = document.getElementById('idade')
        idade.value = data['idade']
        
        sexo = document.getElementById('sexo')
        sexo.value = data['sexo']
        
        localizacao = document.getElementById('localizacao')
        localizacao.value = data['localizacao']
    })
}


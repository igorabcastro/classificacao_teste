function confirmaExclusao(url){
    if (confirm('Esta operação não poderá ser desfeita.\n\nTem certeza que deseja apagar este registro?\n \n')){
        window.location = url
    }
  }


function confirmaNovaSenha(url){
    if (confirm('Será envianda uma nova senha para o email do usuário. Deseja realmente continuar? \n \n')){
        window.location = url
    }
  }


function confirmaBloqueio(url){
    if (confirm('Isso impedirá o acesso do usuário ao sistema. Deseja realmente continuar? \n \n')){
        window.location = url
    }
  }

function confirmaDesbloqueio(url){
    if (confirm('Isso liberará o acesso do usuário ao sistema. Deseja realmente continuar? \n \n')){
        window.location = url
    }
  }
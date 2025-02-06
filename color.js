document.addEventListener("DOMContentLoaded",function(){
    //change color 
    document.querySelectorAll('button').forEach(function(button){
        button.onclick=function(){
            document.querySelector('#hello').style.color=button.dataset.color;
        }
    })
    /*document.querySelector('#red').onclick=function(){
        document.querySelector('#hello').style.color='red';
    }
    document.querySelector('#blue').onclick=function(){
        document.querySelector('#hello').style.color='blue';
    }
    document.querySelector('#green').onclick=function(){
        document.querySelector('#hello').style.color='green';
    }*/
})
/* Tic-tac-Toe 
** javascript
** 2011 Eric Schug
*/
var left=0;
var top=-20;
var velup=0;

function move()
{
    art=document.getElementById('art')
    if(art) {
        art.style.display='block'
        art.style.top= (top-art.offsetHeight)+'px'
        top += 5;
        //console.log(art.offsetHeight);
    }
    if(top<445) {
        t=setTimeout("move()",30);
    }
} 

setTimeout('move()',10);


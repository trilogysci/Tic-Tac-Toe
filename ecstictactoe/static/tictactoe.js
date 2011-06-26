/* Tic-tac-Toe 
** javascript
** 2011 Eric Schug
*/
var left=0;
var top=-20;
var velup=0;

function move()
{
    art=document.getElementById("art");
    if(art) {
        art.style.display="block";
        art.style.top= (top-art.offsetHeight)+"px";
        top += 5;
        //console.log(art.offsetHeight);
    }
    if(top<445) {
        t=setTimeout("move()",30);
    }
} 

setTimeout("move()",10);
var urlmove = "/move/";

$(document).ready(function() {
    // play using ajax 
    csrf=$("input[name='csrfmiddlewaretoken']").attr('value');
    var play={"board": "_________",
                "winner":""
                };
    function userMove() {
        cell=$(this).attr('value'); 
        var jsonData={};
        jsonData['board']=play['board'];
        jsonData['cell']=cell;
        $.ajax({
            type: "GET",
            dataType: "json",
            data: jsonData,
            beforeSend: function(x) {
                if(x && x.overrideMimeType) {
                    x.overrideMimeType("application/json;charset=UTF-8");
                }
            },
            url: urlmove,
            success: function(data) {
                if(data["board"]) {
                    play=data;
                    updateBoard(play);
                }
            }
        });
    }
    function updateBoard(play)
    {
        var i,j;
        board=play["board"];
        for (i=0;i<3;i++) {
            for (j=0;j<3;j++) {
                if(board[i*3+j]=="X") {
                    htmltext = "X";
                } else if(board[i*3+j]=="O") {
                    htmltext = "O";
                } else {
                    if(play["winner"]) {
                        htmltext = "&nbsp;";
                    } else {
                        htmltext = "<button type=\"button\" class=\"move\" value=\""+ i + j +"\">O?</button>";
                    }
                    
                }
                $("#td"+i+j).html(htmltext);
            }
        }
        $(".move").click(userMove);

    }
    updateBoard(play);
});
        
    
